import os
import sys
from dotenv import load_dotenv
from twitchio.ext import commands
import irc.bot
import requests
import time
import random


class TwitchQuizBot(commands.Bot):
    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        load_dotenv()
        super().__init__(token=os.getenv('TOKEN'), prefix='!',initial_channels=[os.getenv('CHANNEL')])


    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')

    async def event_message(self, message):
        #messages with echo set to True are messages sent by the bot
        #for now, let's ignore them
        if message.echo:
            return

        #print our message to console
        print(message.content)

        await self.handle_commands(message)

    #TODO: RATE LIMITING????
    @commands.command()
    async def pun(self, ctx: commands.Context):
        pun_list = ["Hal: How did you get hit on the head with a book? Sal: I only have my shelf to blame.",
                    "How much did the pirate pay to get their ears pierced? A buck an ear.",
                    "My favorite drink? Purr-secco",
                    "What do you call an alligator in a vest?.....AN INVESTIGATOR!!",
                    "How does a penguin build its house? Igloos it together."]
        pun = random.choice(pun_list)
        #time.sleep(2)
        await ctx.send(pun)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'Hello {ctx.author.name}!')


    """
    Quiz is started.
    Bot pushes message with question
    Bot waits for response
    First returned correct response add 'point'


    TODO:
    point tracker?
    question list
    async waiting for answer
    
    
    
    
    
    """

bot = TwitchQuizBot()
bot.run()
