import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot {bot.user} online ✅")

@bot.event
async def on_member_join(member: discord.Member):
    channel = bot.get_channel(1470161243909390477)
    if channel:
        await channel.send(f"{member.mention} entrou no servidor 👋")


@bot.event
async def on_member_remove(member: discord.Member):
    channel = bot.get_channel(1470216407353655367)
    if channel:
        await channel.send(f"{member.mention} saiu do servidor 😢")


@bot.command()
async def ola(ctx: commands.Context):
    await ctx.reply(f"Olá! {ctx.author.mention} Tudo bem?")


@bot.command()
async def falar(ctx: commands.Context, *, texto: str):
    await ctx.send(texto)


TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise ValueError("DISCORD_TOKEN não foi encontrado no arquivo .env")

bot.run(TOKEN)
