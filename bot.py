import asyncio
import discord
from discord.ext import commands
import json
from discord import *
import os

with open('setting.json', mode='r', encoding='utf8') as jsonFile:
    jsonData = json.load(jsonFile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix = jsonData["PREFIX"], intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is Online <<")

@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done')
    
@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un - Loaded {extension} done')
    
@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re - Loaded {extension} done')
    
async def load_extensions():  
    for filename in os.listdir('./cmds'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cmds.{filename[:-3]}')
        
async def main():
    async with bot:
        await load_extensions()
        await bot.start(jsonData['BOT_TOKEN'])
        

if __name__ == "__main__":    
    asyncio.run(main())