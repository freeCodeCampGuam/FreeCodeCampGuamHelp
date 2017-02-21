#Red-DiscordBot Conventions

*this guide is under construction and conventions are always changing. The best way to get a feel for the conventions is to spend time in the Red server and take a look at the most accepted cogs.

Try to keep everything PEP8.

You can find a style guide [here](https://www.python.org/dev/peps/pep-0008/). You could also install a linter or IDE to tell you when you deviate from the standard.

The bot's conventions deviate from PEP8 in some cases. This guide will describe those cases as well as some commonly used snippets of code.

[PEP8 condones this behavior](https://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds):
> However, know when to be inconsistent -- sometimes style guide recommendations just aren't applicable. When in doubt, use your best judgment. Look at other examples and decide what looks best. And don't hesitate to ask! 

##Deviations

###File names and Class names

The `!load` command uses filenames and the `!help` command uses classnames.

When programming for this bot, to avoid confusion, please make sure your filenames and classnames follow this format:  

| filename | classname |
| -------- | --------- | 
| multiplewords.py | Multiplewords |

In the near future we may make both `!help` and `!load` use the filename but towards the user we'll refer to the cogs with a capitalized 1st letter.

###Command names

Commands are registered into the bot using their function names.

Over time, the convention for commands seem to be the following:
```py
!ping
!economyset
!modset
!editrole

!addsong  
!delsong  
or  
!addcom  
!removecom 
``` 

This would mean that you would have to name your command functions accordingly.
```py
@commands.command()
async def addsong(self):
    pass
```
instead of
```py
@commands.command()
async def add_song(self):
    pass
```

Alternatively, you could use `command`'s optional parameter `name` to set the command's actual name. This is useful when a function is the same name as a Python builtin.

```py
@commands.command(name='set')
async def _set(self):
    pass
```

The convention is to use the `name` parameter in subcommands also.

```py
@commands.group()
async def economyset(self)
    pass

...

@economyset.command(name='payout')
async def economyset_payout(self):
    pass

or

@economyset.command(name='payout')
async def _economyset_payout(self):
    pass
```

##Useful Snippets

###context

`command` has an option parameter `pass_context`. You will almost always want to set it to `True`. In fact, there is no reason why you shouldn't.

With it set to `True`, the command's context will be passed in as the second argument.  
By convention, we name it `ctx`.

```py
@commands.command(pass_context=True)
async def cmdname(self, ctx):
    pass
```

Use `help()` and `dir()` to see what you can get with it.

The most common uses for it is getting the command's author, channel, and server.
```py
@commands.command(pass_context=True)
async def cmdname(self, ctx):
    server = ctx.message.server
    channel = ctx.message.channel
    author = ctx.message.author
```

###Cogs and `n = Cog(bot)`

A cog is a collection of related commands and/or functionalities.  
A cog does not need to have any commands.  
Our typical cog structure is:

```py
# imports
import discord
from discord.ext import commands

# class def
class Cog:
    """help string"""

    def __init__(self, bot)
        self.bot = bot

	# command defs
	...

# outer_functions
check_folders():
    pass

# setup
def setup(bot):
	check_folders()
    n = Cog(bot)
    # add listeners
    ...
    # add cog
    bot.add_cog(n)
```

If no listeners need to be added `n = Cog(bot)` and `bot.add_cog(n)`  
could be combined in one line: `bot.add_cog(Cog(bot))`   
We tend to leave them as separate lines though. ¯\\\_(ツ)_/¯  

###Storing data

*under construction

We use the utils class `dataIO` to store our data in JSON files.
By convention we use JSON. If you have data large enough to merit using a DB, feel free to use it.

Cogs are not allowed to read or write outside of their own data folders. Repos found with cogs that are doing this may be considered malicious and taken down.  

Up until recently, we used dataIO's `fileIO`. You will see a lot of cogs using this.  
`fileIO` is deprecated now though, so please use `dataIO`. You will find that it is easier to use.

This is the general structure of a cog with persistant settings using `dataIO`.  
You will use it so often, you might as well make a snippet out of it.  
*self-advertising: there's an IDE cog in my repo with some useful bot snippets. It is not updated to use dataIO yet though.
```py
import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO

class Mycog:
    """description"""

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json("data/mycog/settings.json")
    
    # commands
    # save self.settings with dataIO.save_json(path, self.settings) whenever a change is made.
    ...
        
# makes sure the data/mycog folder exists
# notice we print any changes to the bot's computer to the console.
# things like adding files/folders and any noteworthy data-related information   
# should be logged in some way
def check_folders():
    folder = "data/mycog"
    if not os.path.exists(folder):
        print("Creating {} folder...".format(folder))
        os.makedirs(folder)

# makes sure the settings.json file exists and makes sure all default fields exist. 
# (this is important when we want to update the cog later with more default fields)
def check_files():
    default = {}
    settings_path = "data/mycog/settings.json"

    if not os.path.isfile(settings_path):
        print("Creating default mycog settings.json...")
        dataIO.save_json(settings_path, default)
    else:  # consistency check
        current = fileIO(settings_path, "load")
        if current.keys() != default.keys():
            for key in default.keys():
                if key not in current.keys():
                    current[key] = default[key]
                    print(
                        "Adding " + str(key) + " field to mycog settings.json")
            dataIO.save_json(settings_path, current)

# check folder and files before loading the cog
def setup(bot):
    check_folders()
    check_files()
    n = Mycog(bot)
    bot.add_cog(n)
```

TODO: parameters, consuming rest  

TODO: convert tabs to spaces  

TODO: how to ask in #support  

TODO: if you want to publish cogs, you should join the server and try to be a part of the community. You will learn new things including new conventions and you will gain trust with the members of the community.  

TODO: how to publish cogs + how to use git  

TODO: rate limits and spam

TODO: on_message
