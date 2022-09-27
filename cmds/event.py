import discord
from discord.ext import commands

import json
import random
import asyncio

from DiscordColoBot.core.classes import CogExtension

with open('setting.json', mode='r', encoding='utf8') as jsonFile:
    jsonData = json.load(jsonFile)


class Event(CogExtension):
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        # print(f'{member} join!')
        channel = self.bot.get_channel(int(jsonData["JOIN_CHANNEL_ID"]))
        # await channel.send(f'{member} join!')
        # pic = member.avatar
        # await channel.send(pic)
        await channel.send("https://i.imgur.com/ieAqYis.png")
        
        await asyncio.sleep(1)
        
        embed=discord.Embed(title="歡迎加入", color=0xff0505)
        embed.set_author(name="錢伯爾")
        embed.set_thumbnail(url=member.avatar)
        memberName = f'{member}'
        memberName = memberName.split('#')[0]
        title = "To " + memberName + ":"
        embed.add_field(name=title, value="You wanna play", inline=False)
        embed.add_field(name="Let's play", value="", inline=False)
        embed.set_footer(text="被我抓到了你在打手槍")
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} leave!')
        channel = self.bot.get_channel(int(jsonData["LEAVE_CHANNEL_ID"]))
        await channel.send(f'{member} leave!')
    
    
async def setup(bot):
    await bot.add_cog(Event(bot))