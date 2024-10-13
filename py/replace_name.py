import discord
from discord.ext import commands
import os

class  Replace_name(commands.Cog):
    def __init__(self,bot) :
        self.bot = bot

    @commands.command()
    async def replace_name(self,ctx):
        ID = [855710646171205633,697810500691427358]
        if (ctx.author.id in ID):
            await ctx.send("歡迎"+ctx.author.display_name+"\n現在起你可以更改班代姐姐的暱稱\n請直接輸入")
            while True:
                guess = await self.bot.wait_for("message",timeout=300.0)
                if guess.author.id in ID:
                    with open(os.path.join("..", "info", "message_files", "joyce_name.txt"), "w") as f:
                        f.write(guess.content)
                    break
                else:
                    continue
            print(guess.content)
            await ctx.send("設定完畢")
        else:
            await ctx.send("你暫時沒有使用的權限喔")




async def setup(bot):
    await bot.add_cog(Replace_name(bot))

