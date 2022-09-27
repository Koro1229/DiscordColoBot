import asyncio
from datetime import datetime
import json
import discord
from discord.ext import commands

from DiscordColoBot.core.classes import CogExtension

class Task(CogExtension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.counter = 0
        
        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(844258283678203916)
            while not self.bot.is_closed():
                now_time = datetime.now().strftime('%H%M')
                with open('setting.json', mode='r', encoding='utf8') as jsonFile:
                    jsonData = json.load(jsonFile)
                
                if now_time == jsonData['time'] and self.counter == 0:
                    self.counter = 1
                    await self.channel.send('Task Working!')
                else:
                    pass
                
                await asyncio.sleep(1)
                
                
        self.bg_task = self.bot.loop.create_task(time_task())

    @commands.command()
    async def set_channel(self, ctx, ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel: {self.channel.mention}')
        
    @commands.command()
    async def set_time(self, ctx, time):
        self.counter = 0
        with open('setting.json', mode='r', encoding='utf8') as jsonFile:
            jsonData = json.load(jsonFile)
        
        jsonData['time'] = time
        with open('setting.json', mode='w', encoding='utf8') as jsonFile:
            json.dump(jsonData, jsonFile, indent=4)
        


async def setup(bot):
    await bot.add_cog(Task(bot))