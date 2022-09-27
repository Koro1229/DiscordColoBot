import discord
from discord.ext import commands

from DiscordColoBot.core.classes import CogExtension

class Poyoyo(CogExtension):
        
    @commands.command()
    async def poyoyo(self, ctx):
        embed=discord.Embed(title="PoYoYo 使用工具箱", description="Please using commands below with prefix '|'", color=0xcd2d2d)
        embed.set_author(name="PoYoYo", icon_url="https://i.imgur.com/dAepOaF.jpg")
        embed.set_thumbnail(url="https://i.imgur.com/dAepOaF.jpg")
        embed.add_field(name="poyoyo", value="Call this good message block", inline=False)
        embed.add_field(name="load (function)", value="Load functions", inline=True)
        embed.add_field(name="unload (function)", value="Un - Load functions", inline=False)
        embed.add_field(name="reload (function)", value="Re - Load functions", inline=True)
        embed.set_footer(text="Provided by Koro#4359")
        await ctx.send(embed=embed)
        
async def setup(bot):
    await bot.add_cog(Poyoyo(bot))