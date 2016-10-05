#!/usr/local/bin/tclsh8.6

# This takes a list of compressed DHCP log files and writes out three seperate files for data in lines
# containing "Address:" in the 6th word of the line.  Data is buffered in hash tables to cut down the number of
# file open's and closes, but written periodically to manage the amount of memory used as some of these files are big.

# I started converting this to python to see if it would run faster but then found the gzip library
# was available in tcl 8.6 so I finished it in TCL, a language I'm more familier with.

### Log sample ####################
#May 28 04:12:30 dhcp100 dhcpd: DHCPACK on 121.55.235.173 to 94:44:52:5b:ed:99 via eth1
#May 28 04:12:30 dhcp100 dhcpd: Address: 121.55.227.172 to CPE: 1:34:12:98:4:a:86 from CM: 34:bd:fa:ad:96:b
###################################

# As a learning experience I'd like to see it in Python as I'm trying to get more comfortable with it.  Please
# help me to learn python by converting this code.  Thanks.

# File Hierarchy
# YYYY
#    IP
#    CM
#    CPE

set basedir "/data/dhcp"
set buffsize 500

if {$argc <1} {
	puts "Usage: splitdhcp <file_list>"
	exit
}
#########################################

## Create directory structures if they don't exist
proc createDir {year} {
	global basedir
	if {![file exists $basedir/$year]} {file mkdir $basedir/$year}
	if {![file exists $basedir/$year/IP]} {file mkdir $basedir/$year/IP}
	if {![file exists $basedir/$year/CM]} {file mkdir $basedir/$year/CM}
	if {![file exists $basedir/$year/CPE]} {file mkdir $basedir/$year/CPE}
}

## Sanitize MAC address
proc macit {itin} {
	global line logfile
	if {![regexp {\((.*)\)} $itin b mac]} { set mac $itin }
	set mac [split $mac ":"]
	# sometimes MAC addresses are reported longer then 6 bytes
	if {[llength $mac] > 6} {
		set mac [lrange $mac [expr [llength $mac] - 6] end]
	}
	scan $mac "%02x %02x %02x %02x %02x %02x" m1 m2 m3 m4 m5 m6
	if {![info exists m6]} { set m6 "00" }
	if {![info exists m5]} { set m5 "00" }
	if {![info exists m4]} { set m4 "00" }
	if {![info exists m3]} { set m3 "00" }
	if {![info exists m2]} { set m2 "00" }
	if {![info exists m1]} { set m1 "00" }
	return [format "%02x:%02x:%02x:%02x:%02x:%02x" $m1 $m2 $m3 $m4 $m5 $m6]
}

## Writes a buffered hash table to disk
proc write {log target buff} {
	upvar $buff array
	set year [clock format [lindex [lindex $array($target) 0] 0] -format "%Y"]
	set ouf [open "$year/$log/$target" "a"]
	foreach l [lsort $array($target)] {
		puts $ouf $l
	}
	catch { unset $array($target) }
	close $ouf
}
###############################
# MAIN
## takes a list of files specified on the command line and loops on each one
foreach logfile $argv {
	puts -nonewline "$logfile - "
	flush stdout

	## Not neseccery but wanted to track how long each file took
	set open_t [clock seconds]

	# Open "gzip'd log file and prep it for decompression"
	set inf [open "$logfile" "r"]
	zlib push gunzip $inf

  ## Iterate on each line of the decompressed file
	while {[gets $inf line]>=0} {
	  # See example line on the top of file.  lindex returns the nth word of string starting at 0
		set it [lindex $line 5]
		if {$it == "Address:" || $it == "DHCPACK"} {
		  # Convert the date stamp to seconds
			set dateStamp [clock scan [lrange $line 0 2]]

			# a tricky way (frowned upon) to set multiple variables at once
			foreach {year month day} [clock format $dateStamp -format "%Y %m %d"] {}

			# If there is no directory for the current year then create one
			if {![file exists "$basedir/$year"] || ![file exists "$basedir/$year/IP"]} {createDir $year}

			# adjust for line differences
			if {[lindex $line 8] == "to" || [lindex $line 8] == "CPE:"} {
				set cpeMAC [macit [lindex $line 9]]
			} else {
				set cpeMAC [macit [lindex $line 8]]
			}

			# split up the line and output it to the three hash tables IP, CM & CPE
			if {[lindex $line 5] == "Address:"} {
				set ip [lindex $line 6]
				set cmMAC [macit [lindex $line [expr [llength $line] - 1]]]
				lappend IP($ip) [format "%s %s Assign %s %s" $dateStamp [lindex $line 3] $cpeMAC $cmMAC]
				if {[catch {incr IPc($ip)}]} {set IPc($ip) 1}
				lappend CM($cmMAC) [format "%s %s %s" $dateStamp $ip $cpeMAC]
				if {[catch {incr CMc($cmMAC)}]} {set CMc($cmMAC) 1}
				lappend CPE($cpeMAC) [format "%s %s %s" $dateStamp $ip $cmMAC]
				if {[catch {incr CPEc($cpeMAC)}]} {set CPEc($cpeMAC) 1}

				# Check if this Cable modem buffer should be flushed to disk
				if {$CMc($cmMAC) > $buffsize} {
					write "CM" $cmMAC "CM"
					unset CM($cmMAC)
					unset CMc($cmMAC)
				}

				# Check if this CPE buffer should be flushed to disk
				if {$CPEc($cpeMAC) > $buffsize} {
					write "CPE" $cpeMAC "CPE"
					unset CPE($cpeMAC)
					unset CPEc($cpeMAC)
				}
			}

			# Check if this CPE buffer should be flushed to disk
			if {$IPc($ip) > $buffsize} {
				write "IP" $ip "IP"
					unset IP($ip)
					unset IPc($ip)
			}
		}
	}
	catch {close $inf}

	# Done with the main loop, now flush the bufferes to disk.
	foreach ip [array names IP] {
		write "IP" $ip "IP"
		unset IP($ip)
		unset IPc($ip)
	}
	foreach cmMAC [array names CM] {
		write "CM" $cmMAC "CM"
		unset CM($cmMAC)
		unset CMc($cmMAC)
	}
	foreach cpeMAC [array names CPE] {
		write "CPE" $cpeMAC "CPE"
		unset CPE($cpeMAC)
		unset CPEc($cpeMAC)
	}

	# output how long it took to process the last file.
	set dur [expr [clock seconds] - $open_t]
	puts "Duration: [clock format $dur -format "%M:%S"]"
}
