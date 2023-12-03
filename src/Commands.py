import discord
from discord.ext import commands

from main import bot

@bot.bot.event()
async def on_ready():
    print('test')
    print('Logged in as: {0.user.name}\nApplication id : {0.user.id}'.format(bot.bot))
    print(f'discord version : {discord.__version__}\n')
    await bot.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"!help"))