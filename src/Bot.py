import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

class Bot:

    def __init__(self) -> None:
        intents = discord.Intents().all()
        self.bot = commands.Bot(command_prefix='!', intents=intents)
        load_dotenv()

    def launch(self):
        self.bot.run(os.getenv('TOKEN'))

    