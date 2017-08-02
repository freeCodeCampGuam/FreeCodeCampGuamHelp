##[Red-DiscordBot](https://github.com/Twentysix26/Red-DiscordBot)  
Is an open source modular all-purpose chatbot for Discord servers. It uses a Discord API wrapper called [discord.py](https://github.com/Rapptz/discord.py) and its command module as the core bot.  
Because of this bot's modular design and friendly community, it is a great tool to use to learn Python.

Install it with the appropriate installation process [here](https://twentysix26.github.io/Red-Docs/)

Once you've started it up it should give you a link. 
You can use that link with the `=addbot` command in our server to add it to our server.  

![](https://cdn.discordapp.com/attachments/206326891752325122/220085257553182720/addbot.gif)

Once you've added your bot, spend some time getting familiar with it. The [Docs](https://twentysix26.github.io/Red-Docs/) can be outdated so..  

Use `[p]help` to get information about your bot's commands (where [p] is your prefix)

![](https://cdn.discordapp.com/attachments/206326891752325122/220086640763338752/help.gif)

Use `[p]cog` to manage 3rd party cogs. You can view the approved published repos [here](https://twentysix26.github.io/Red-Docs/red_cog_approved_repos/)

You will want to get RoboDanny's repl cog. RoboDanny is a bot made by the creator of discord.py. Because the core bot is the same, RoboDanny's cogs can be used in Red.

To get the repl cog, click the Raw button [here](https://github.com/Rapptz/RoboDanny/blob/master/cogs/repl.py) and copy paste the contents into a new file in your `Red-DiscordBot/cogs/` directory and name it `repl.py`.

I've made a few edits to the cog to allow printing of large messages. If you would like, you can use [that version](https://cogs.red/cogs/irdumbs/Dumb-Cogs/repl/) instead.  

Once you've added the file to your `cogs` folder, you'll need to load it in discord by typing `[p]load repl`. Now you can execute arbitrary Python code within Discord.  

![](https://cdn.discordapp.com/attachments/206326891752325122/220095271831339008/repl.gif)

Now [go back](README.md) and start making cogs! 
