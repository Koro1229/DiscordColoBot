import discord
from discord.ext import commands
import json
from discord import *

with open('json/setting.json', mode='r', encoding='utf8') as jsonFile:
    jsonData = json.load(jsonFile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix = jsonData["PREFIX"], intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is Online <<")
    
@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    channel = bot.get_channel(int(jsonData["JOIN_CHANNEL_ID"]))
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')
    channel = bot.get_channel(int(jsonData["LEAVE_CHANNEL_ID"]))
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)}(ms)')
    
@bot.command()
async def 老婆(ctx):
    ayamePic = discord.File('C:\\Users\\joker\\Desktop\\Discord Bot\\DiscordColoBot\\pic\\AYAME.jpg')
    await ctx.send(">_<  我在洗澡拉")
    await ctx.send(file=ayamePic)
bot.run(jsonData['BOT_TOKEN'])