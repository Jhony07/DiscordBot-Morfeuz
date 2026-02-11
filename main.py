import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)


async def load_cogs():
    if not os.path.exists("cogs"):
        print("Diretório 'cogs' não encontrado.")
        return
    for root, dirs, files in os.walk("cogs"):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                filepath = os.path.join(root, file)
                module_name = filepath.replace(os.path.sep, ".")[:-3]

                try:
                    loaded_count = len(bot.commands)
                    await bot.load_extension(module_name)
                    new_count = len(bot.commands) - loaded_count
                    print(f"Carregado: {file} ({new_count} comandos)")
                except commands.ExtensionAlreadyLoaded:
                    pass
                except Exception as e:
                    print(f"Erro ao carregar {module_name}: {e}")


@bot.event
async def on_ready():
    await load_cogs()
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


TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise ValueError("DISCORD_TOKEN não foi encontrado no arquivo .env")

bot.run(TOKEN)
