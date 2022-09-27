import discord
from discord.ext import commands

import json

from DiscordColoBot.core.classes import CogExtension


class Message(CogExtension):
        
    @commands.Cog.listener()
    async def on_message(self, msg):
        with open('message.json', mode='r', encoding='utf8') as jsonFile:
            jsonMessage = json.load(jsonFile)
            
        if msg.author != self.bot.user:
            if msg.content in jsonMessage:
                await msg.channel.send(jsonMessage[msg.content])
    
    
async def setup(bot):
    await bot.add_cog(Message(bot))