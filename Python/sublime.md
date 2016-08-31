##Setting up Sublime.

Get [Package Control](https://packagecontrol.io/). You will want to bookmark that page as well. With package control, you can install and manage your packages with simple keystrokes.

The installation is pretty straight forward. In sublime, press <kbd>ctrl+`</kbd> and paste in the code given to you on the installation page. You may need to restart your sublime to make sure the changes have taken place.

![](https://cdn.discordapp.com/attachments/206277423120121857/220051241806331904/pck_ctrl.gif)

Now that you have Package Control installed, you can press `ctrl+shift+p` (or `cmd+shift+p` on Mac) to open up your "Command Pallete". You can access many of Sublime's commands through here as well as commands from packages you install.

Sublime uses `fuzzy` search. That means if you want to get to the command, `Package Control: Install Package`, instead of typing out the whole thing, you can just type `pki` and it'll be the selected command.

Try it. Press `ctrl+shift+p` / `cmd+shift+p` and type `pki`.

![](https://cdn.discordapp.com/attachments/206277423120121857/220060441475416064/pci.gif)


###Packages:
Before moving on, you might want to take a look at some of the packages available on [https://packagecontrol.io/](https://packagecontrol.io/).  

[Here](https://scotch.io/bar-talk/best-of-sublime-text-3-features-plugins-and-settings) is a little overview of sublime and some of it's packages  
[Anaconda](https://packagecontrol.io/packages/Anaconda) - Python IDE  
[Floobits](https://packagecontrol.io/packages/Floobits) - real-time collaborative coding (think google docs)  
[SublimeREPL](https://packagecontrol.io/packages/SublimeREPL) - REPLs in many langauges


**Web Dev:** (I'll let you [search](https://packagecontrol.io/) for these.)

Color Highlighter  
ColorPicker  
Emmet - autocomplete and expanding html/css shortcuts  
LiveStyle - Live css editing  
OmniMarkupPreviewer - What I used to write this

Theme Recommendation: [Monokai Extended](https://packagecontrol.io/packages/Monokai%20Extended)


##Get subl
[Windows](https://scotch.io/tutorials/open-sublime-text-from-the-command-line-using-subl-exe-windows) / [Mac](http://olivierlacan.com/posts/launch-sublime-text-3-from-the-command-line/) (if you don't have it)  
The Mac guide says to name it sublime. I use subl. I recommend you do as well for consistency sake.  
With subl/subl.exe (or atom/atom.exe) you can do things like this:
![](https://cdn.discordapp.com/attachments/206326891752325122/220075883094999051/subl.gif)

That's it with Sublime for now. Go [back](README.md) and install the bot.


###Extras
After you've set up your bot (ie. installed Python3), there are a few things you may want to do.

* add Python3 build system  
if you are on a mac, you will now have Python 2.7 and Python 3.5. You may want a Python3 build system so that you can run your Python3 code within Sublime.  
	* `cmd+shift+p` then type `new build` until the option comes up and press enter. 
	* Copy paste the following into it and save it.
```json
{
    "cmd": ["/usr/local/bin/python3", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python",
    "encoding": "utf8",
    "path": "/usr/local/Frameworks/Python.framework/Versions/3.5/bin/"
}

```  
![](https://cdn.discordapp.com/attachments/206326891752325122/220100066994552834/build.gif)


* add a Python3 repl.  
(if you only have 1 Python version installed, you may not need to do this)  
REPL stands for read–eval–print loop which is just a fancy way of saying it's an interactive code interpreter.  
Go to your sublime preferences and open these two files in sublime.  
`Sublime Text 3/Packages/SublimeREPL/config/Python/Main.sublime-menu`  
`Sublime Text 3/Packages/SublimeREPL/config/Python/Default.sublime-commands`  
![](https://cdn.discordapp.com/attachments/206326891752325122/220109129652371456/sublrepla.gif)  
**You should make backups of these files before you edit them.**  
**You should also know how to edit JSON files**  

We'll want to add a few new menu options to our Command Pallete.  
	In `Default.sublime-commands` add this group of 2 commands:
```json
{
    "caption": "SublimeREPL: Python3",
    "command": "run_existing_window_command", "args":
    {
        "id": "repl_python3",
        "file": "config/Python/Main.sublime-menu"
    }
},
{
    "caption": "SublimeREPL: Python3 - RUN current file",
    "command": "run_existing_window_command", "args":
    {
        "id": "repl_python3_run",
        "file": "config/Python/Main.sublime-menu"
    }
},
```
Now in `Main.sublime-menu`, add these:  
```json
{"command": "repl_open",
 "caption": "Python3",
 "id": "repl_python3",
 "mnemonic": "3",
 "args": {
    "type": "subprocess",
    "encoding": "utf8",
    "cmd": ["python3", "-i", "-u"],
    "cwd": "$file_path",
    "syntax": "Packages/Python/Python.tmLanguage",
    "external_id": "python",
    "extend_env": {"PYTHONIOENCODING": "utf-8"}
    }
},
{"command": "repl_open",
 "caption": "Python3 - RUN current file",
 "id": "repl_python3_run",
 "mnemonic": "d",
 "args": {
    "type": "subprocess",
    "encoding": "utf8",
    "cmd": ["python3", "-u", "$file_basename"],
    "cwd": "$file_path",
    "syntax": "Packages/Python/Python.tmLanguage",
    "external_id": "python",
    "extend_env": {"PYTHONIOENCODING": "utf-8"}
    }
},
```
That will add the `SublimeREPL: Python3` and `SublimeREPL: Python3 - RUN current file` commands to your Command Pallete (`cmd+shift+p`)
![](https://cdn.discordapp.com/attachments/206326891752325122/220116976922656768/sublreplb.gif)

* Customize your Anaconda IDE (if you plan on using it)  
Open Anaconda's Default and User settings. The default settings get reset every time you restart sublime, so you will want to make your changes in the user settings.  
If you have more than one Python version installed, you will want to specify which one Anaconda will lint for.  
![](https://cdn.discordapp.com/attachments/206326891752325122/220336067147071488/anaconda.gif)

