import discord
from discord.ext import commands

from Bot import bot
from ..dropdown.games_view import GamesView

@bot.bot.command(name='games')
async def _games(ctx):
    await ctx.send(view=GamesView())