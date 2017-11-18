import discord
import asyncio
import json
bot = discord.Client()

try:
    file = open("settings/credentials.json",'r+')
    file = file.read()
    settings = json.loads(file)
except Exception as e:
    print(e)

@bot.event
async def on_ready():
    print(bot.user.id)
    print(bot.user.name)
    await bot.change_presence( game=discord.Game( name=settings["prefix"]+"=prefix ~LIAM",type = 0))

@bot.event
async def on_message(message):
    channel = message.channel
    prefix = settings["prefix"]

    if message.content.startswith(prefix+'skid'):
        await bot.send_message(channel, "**OP**")
        
    elif message.content.startswith(prefix+'mika'):
        await bot.send_message(channel, "Liams OP Bunny Wifey")
        
    elif message.content.startswith(prefix+'noble'):
        await bot.send_message(channel, "**THE OP PYTHON PRO NOOB**")

        
      print("Starting......")
bot.run(settings["token"])
#bot.run("")
