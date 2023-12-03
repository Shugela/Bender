import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

import Bot

@Bot.bot.event
async def on_ready():
    print('Logged in as: {0.user.name}\nApplication id : {0.user.id}'.format(Bot.bot))
    print(f'discord version : {discord.__version__}\n')
    await Bot.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"!help"))




if __name__ == '__main__':
    bot = Bot()
    bot.launch()
    
    