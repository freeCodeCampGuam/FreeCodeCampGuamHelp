##My First Cog
*This guide is a work in progress. Feel free to suggest or PR changes.

In Red, modules are called cogs. They represent groups of related commands or functions.

You can make a bunch of cogs, put them in a repo (repository - place to put code), and publish them for the public to install and enjoy.

[Here is a tutorial](https://twentysix26.github.io/Red-Docs/red_guide_make_cog/) to get you started on your first cog.
Ignore the 2nd part about "Getting info from webpages".
There is a much easier way to get info and that is through APIs.

###Simple request from an API
We will build off of the previous tutorial's boilerplate:
```py
import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("I can do stuff!")

def setup(bot):
    bot.add_cog(Mycog(bot))
```

API stands for Application program interface. An API allows for applications to talk with each other.

Many web APIs return results in JSON format like this result from the [Chuck Norris Jokes API](http://www.icndb.com/api/). We will be using this API for this tutorial.
```json
{ "type": "success", "value": { "id": 233, "joke": "When Bruce Banner gets mad, he turns into the Hulk. When the Hulk gets mad, he turns into Chuck Norris.", "categories": [] } }
```
Responses like this are much easier to deal with because we don't have to go digging through all the html that may change when the webpage changes.

In order to make a call to an API we will need to import aiohttp (not requests because that blocks).
```py
import discord
from discord.ext import commands
import aiohttp

...
```
This is the basic structure of an aiohttp request:
```py

async with aiohttp.get(url) as response:
    result = await response.json()
```
Let's use this to make a request to the Chuck Norris API: [http://api.icndb.com/jokes/random/](http://api.icndb.com/jokes/random/)
```py
async with aiohttp.get("http://api.icndb.com/jokes/random/") as response:
    result = await response.json()
```
`response.json()` returns the JSON response as a dict which we store in result. You can worry about dicts later.  
Again, the response comes back structured like this `{"type": "success", `**`"value"`**`: {"id": 233, `**`"joke"`**`: "blah blah blah", "categories": []}}`  

Let's get the **`"joke"`** part of the response within **`"value"`**. To do that we do this:  
```py
async with aiohttp.get("http://api.icndb.com/jokes/random/") as response:
    result = await response.json()
joke = result["value"]["joke"]
```
`result["value"]` gets `{"id": 233,"joke": "blah blah blah", "categories": []}}`  
and `result["value"]["joke"]` gets `"blah blah blah"`

Finally, we make the bot say the joke.
```py
await self.bot.say(joke)
```

All together that's:
```py
import discord
from discord.ext import commands
import aiohttp

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """This does stuff!"""
        async with aiohttp.get("http://api.icndb.com/jokes/random/") as response:
            result = await response.json()
        joke = result["value"]["joke"]
        await self.bot.say(joke)

def setup(bot):
    bot.add_cog(Mycog(bot))
```

Now just save it as `mycog.py` and load it with `!load mycog` in discord.  
Now when you type `!mycom`, your bot should spit out a Chuck Norris joke

![](https://cdn.discordapp.com/attachments/206326891752325122/220333306359709696/unknown.png)

What now? [Some explanations](PythonIntro.md)

