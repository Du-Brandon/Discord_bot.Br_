import discord
from discord.ext import commands
import os

class  Add_meal(commands.Cog):
    def __init__(self,bot) :
        self.bot = bot

    @commands.command()
    async def add_meal(self,ctx):
        ID = []
        if (ctx.author.id in ID):
            await ctx.send("歡迎"+ctx.author.display_name+"\n現在起你可以加入菜單\n請直接輸入")
            while True:
                guess = await self.bot.wait_for("message",timeout=300.0)
                if guess.author.id == ctx.author.id:
                    with open(os.path.join("..", "info", "message_files", "dinner.txt"), "a") as f:
                        f.write(guess.content+"\n")
                    break
                else:
                    continue
            print(guess.content)
            await ctx.send("設定完畢")
        else:
            await ctx.send("你暫時沒有使用的權限喔")




async def setup(bot):
    await bot.add_cog(Add_meal(bot))

