## `async` / `await` and Red commands

The bot we will be using to learn Python is asynchronous.  
You don't need to know what that means in order to program for the bot.

**Simple explanation:**

You can think of it like this.  
Making a request to the discord API takes a long time (to a computer).
Whenever something takes a long time, we `await` it.  

If we tell the bot to `self.bot.say('hi')`, it has to send that message to the discord API which posts it to our discord server and then comes back to tell the bot that it was successful.  
That takes a long time, so we `await` it.

Functions with `await`ed things in them must be defined as `async`.  
Here is an example:

```py
@commands.command()
async def hi(self):
    await self.bot.say('hi there')
```

We defined the `hi()` function as async and inside it we `await` for the bot to say "hi there".

**Red commands must be async** but can call other functions that are not async.

```py
...

@commands.command()
async def evenorodd(self, num: int):
    if is_even(num):
        await self.bot.say('even')
    else:
        await self.bot.say('odd')

def is_even(self, num: int):
    return num % 2 == 0

...
```

Notice, we use `@commands.command()` to tell the bot that that function is a command.  
In discord, we can now type `!evenorodd 3` and the bot will say `odd`  

You can also make command groups with subcommands. I'll let you look through the cogs for examples.  
(hint: In Sublime, you can use `ctrl+shift+f` (or `cmd+shift+f` for Mac) to search through all the open folders for `group`)  

[Go back](README.md) and learn about Redbot conventions

### More detailed explanation of `async`

*note: asynchonous != parallelism. tasks != threads

You might remember that I said to use `aiohttp` instead of `requests` because `requests` is blocking.

Here is some code to demonstrate what that means.  
Notice the only difference between these two commands is one uses `await asyncio.sleep(num)`   
and the other uses `time.sleep(num)` (a blocking function)
```py
import asyncio
import time

class Blockexample:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def asleep(self, num: int):
        """async sleeps for a certain amount of time"""
        await self.bot.say('asleeping {} seconds'.format(num))
        await asyncio.sleep(num)
        await self.bot.say('woke up from async sleep')

    @commands.command()
    async def sleep(self, num: int):
        """sleeps for certain amount of time (blocking)"""
        await self.bot.say('sleeping {} seconds'.format(num))
        time.sleep(num)
        await self.bot.say('woke up from blocking sleep')

def setup(bot):
    bot.add_cog(Blockexample(bot))

```
Here is what happens when I try to make the bot do these commands with other commands.  

![](https://cdn.discordapp.com/attachments/206326891752325122/220407111912390656/unknown.png)

Notice the sleep command stops the bot from executing the other commands until the **blocking** code has completed.

----

In asynchronous programming, there is usually an Event loop.  
Tasks are put into the event loop to be completed some time in the future.

How `async` functions work is, when they start executing, they have control up until they hit an `await`.   
Once that happens, the "request" is sent and the control is given back to the event loop.  
The event loop can now start another task while the 1st one waits for a resonse.

![](http://blogs.quovantis.com/wp-content/uploads/2015/08/Synchronous-vs.-asynchronous.jpg)  
*picture from [http://blogs.quovantis.com/asynchronous-programming-understanding-async-await-in-c/](http://blogs.quovantis.com/asynchronous-programming-understanding-async-await-in-c/)


There are various ways to interact with the event loop in python. You can learn about them [here](https://docs.python.org/3/library/asyncio.html).  
If you look in `red.py`, you'll notice that Red uses `loop.run_until_complete(main())` and that it schedules commands with:  
```py
@bot.event
async def on_message(message):
    if user_allowed(message):
        await bot.process_commands(message)
```
All that is saying is on every message from Discord (`on_message`), if the user is allowed to use the bot here (`user_allowed`), process the command (`process_commands`).  

You can still schedule your own tasks if you want. You can access the event loop in the bot via `bot.loop` and you can `create_task`s for it to execute some time in the future.
```py
self.bot.loop(self.bot.say('1 apple'))
self.bot.loop(self.bot.say('2 banana'))
self.bot.loop(self.bot.say('3 orange'))
```
There is no guaranteed order in which they will run though. The output could be:
> 1 apple  
 3 orange  
 2 banana

There are other useful things you might stumble upon also like [asyncio.gather](https://docs.python.org/3/library/asyncio-task.html?highlight=gather#asyncio.gather)



