import discord
from discord.ext import commands
import os
import random

def what_dinner():
    a = []
    with open(os.path.join("..", "info", "message_files", "dinner.txt"), "r") as f:
        for d in f:
            a.append(d.strip("\n"))
    return a[random.randint(0,len(a)-1)]

class  Dinner(commands.Cog):
    def __init__(self,bot) :
        self.bot = bot

    @commands.command()
    async def dinner(self,ctx):
        await ctx.send(what_dinner())

    
async def setup(bot):
    await bot.add_cog(Dinner(bot))