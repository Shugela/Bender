import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from colorama import Fore

from Bot import bot
from commands.games import games

@bot.bot.event
async def on_ready():
    print(f'[INFO] Logged in as: {bot.bot.user.name}\n'f'[INFO] Application id : {bot.bot.user.id}')
    print(f'[INFO] discord version : {discord.__version__}\n')
    await bot.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"If you don't know shit, type !help"))

if __name__ == '__main__':
    bot.launch()