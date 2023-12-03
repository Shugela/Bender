import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

from Bot import Bot

bot = Bot()

if __name__ == '__main__' :
    bot.launch()

