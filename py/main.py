import discord
from discord.ext import commands
import os
import asyncio
import datetime

def record_message(thattime,userchannel,username,usermessage):
    try:
        with open(os.path.join("..", "info", "message_files", "message.txt"), "a") as file:
            file.write(str(thattime)+" "+userchannel+" "+username+" "+usermessage+"\n")
    except:
        print(username+" have bug")
        

def replace_Joyce_name():
    with open(os.path.join("..", "info", "message_files", "joyce_name.txt"), "r") as f:
        Joyce_name = f.read().strip("\n")
    return Joyce_name

with open(os.path.join("..", "info", "token.txt"), 'r') as f:
    token = f.read().strip("\n")


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='$' , intents = intents)

async def load_cogs():
    try:
        with open(os.path.join("..", "info", "extensions.txt"), 'r') as f:
            for extension in f:
                await bot.load_extension(extension.strip())

    except Exception as e:
        print(f"Error loading cogs: {e}")

with open(os.path.join("..", "info", "extensions.txt"), 'r') as f:
    for extension in f:
        print(extension.strip('\n'))

@bot.event
async def on_ready():
    game = discord.Activity(type=discord.ActivityType.watching, name="缺愛觀察日記")
    await bot.change_presence(status=discord.Status.dnd, activity=game)
    await load_cogs()
    print("Br_? online")
    # 印出 bot 這個 user 的資訊
    print("User name:", bot.user.name)
    print("User ID:", bot.user.id)

@bot.event
async def on_message(message):

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #時間參數
    author_name = message.author.display_name #查詢暱稱
    print(author_name,"say",message.content.lower())
    record_message(current_time,message.channel.name ,message.author.display_name,message.content.lower()) 

    if message.author.id == bot.user.id: #自我ID判斷
        return
    if message.author.id == 893320281442119720 :
        await message.channel.send("#好扯喔東緒")
    
    if "hello" in message.content.lower(): #message.content.lower() = 傳入的訊息，以str的形式
        await message.channel.send("fuck you") # Bot 傳送訊息
    if "allo e" == message.content.lower(): 
        await message.channel.send(author_name+" allo e")
    if "好扯喔" in message.content.lower(): 
        await message.channel.send("#好扯喔東緒")
    if ("班代姐姐" in message.content.lower()) or ("班代姊姊"in message.content.lower()):
        await message.channel.send(replace_Joyce_name())
    # 加這行才可以用 commands
    await bot.process_commands(message)


bot.run(token)