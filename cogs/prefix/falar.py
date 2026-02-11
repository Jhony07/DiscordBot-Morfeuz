import discord
from discord import app_commands
from discord.ext import commands


class falar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def falar(self, ctx, *, texto: str):
        await ctx.send(texto)


async def setup(bot):
    await bot.add_cog(falar(bot))
