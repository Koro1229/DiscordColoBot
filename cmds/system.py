import discord
from discord.ext import commands

from DiscordColoBot.core.classes import CogExtension

class System(CogExtension):
        
    @commands.command()
    async def ping(self, ctx):
        lat = self.bot.latency * 1000
        await ctx.send(f'{round(lat)}(ms)')
    
    @commands.command()
    async def clean(self, ctx, num : int):
        await ctx.channel.purge(limit=num + 1)
        
        
        
async def setup(bot):
    await bot.add_cog(System(bot))