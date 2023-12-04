import discord
from discord.ext import commands

from Bot import bot


@bot.bot.command(name='test')
async def _test(ctx):
    await ctx.send("test")