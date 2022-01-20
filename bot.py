from operator import truediv
import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='|', intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is Online <<")
    
@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    channel = bot.get_channel(933657649713647627)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')
    channel = bot.get_channel(933657680751493181)
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)}(ms)')

bot.run('OTMzNjIzOTMzOTYwMzM1NDAw.YekPCw.jp2-fgGv7MIGtVK2L0qx92munJ4')