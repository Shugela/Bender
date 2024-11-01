import discord
from discord.ext import commands
from dotenv import load_dotenv
import os


"""
"""

class Bot(commands.Bot):

    def __init__(self) -> None:
        intents = discord.Intents().all()
        super().__init__(
            command_prefix=commands.when_mentioned_or('!'),
            intents=intents,
            help_command=None,
        )
        self.bot = commands.Bot(command_prefix='!', intents=intents)
        load_dotenv()

    def launch(self) -> None:
        load_dotenv()
        self.bot.run(os.getenv('TOKEN'))


bot = Bot()

