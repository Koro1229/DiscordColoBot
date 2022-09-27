import discord
from discord.ext import commands

from DiscordColoBot.core.classes import CogExtension

class React(CogExtension):
        
    @commands.command()
    async def hi(self, ctx):
        await ctx.send("hello")
        
    @commands.command()
    async def repeat(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)
        
    @commands.command()
    async def senpai(self, ctx):
        await ctx.message.delete()
        await ctx.send("https://i.imgur.com/ecHhy1S.gif")
        
async def setup(bot):
    await bot.add_cog(React(bot))