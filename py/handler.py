# handler
import discord
from discord.ext import commands
import os

class  Handler(commands.Cog):
    def __init__(self,bot) :
        self.bot = bot

    @commands.command()
    async def handler(self,ctx):
        if (ctx.author.id == 785074383944548363 or ctx.author.id == 855710646171205633):
            await ctx.send("歡迎"+ctx.author.display_name+"\n新增管理者?\n請直接輸入")
        while True:
                guess = await self.bot.wait_for("message",timeout=300.0)
                if guess.author.id == ctx.author.id:
                    with open(os.path.join("..", "info", "ID.txt"), "a") as f:
                        f.write(guess.content+"\n")
                    break
                else:
                    continue
        await ctx.send("設定完畢")

async def setup(bot):
    await bot.add_cog(Handler(bot))