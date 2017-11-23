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
    await bot.change_presence( game=discord.Game( name=settings["prefix"]+"=prefix ~LIAM",type =0))

@bot.event
async def on_message(message):
    channel = message.channel
    prefix = settings["prefix"]

    if message.content.startswith(prefix+'skid'):
        em = discord.Embed()
        em.set_image(url = "https://static.tumblr.com/28e0158c140f058307c7d6e5a4187ca6/oeev8nw/Fujol130y/tumblr_static_tumblr_static_filename_640.gif")

        await bot.send_message(channel, embed = em)
                
    elif message.content.startswith(prefix+'mika'):
        await bot.send_message(channel, "```Liam's OP Bunny Wifey```")
        
    elif message.content.startswith(prefix+'liamika'):
        await bot.send_message(channel, "**The Best Ship** :wink:")
       
        em = discord.Embed()
        em.set_image(url = "https://media.discordapp.net/attachments/335346728897216512/382472973409320960/32e8d07153aa4d76b80250ac1297f30d.png?width=363&height=438")
        
        await bot.send_message(channel, embed = em)
               
    elif message.content.startswith(prefix+'liam'):
        await bot.send_message(channel, "```Mika's One And Only Little Vampy```")
        
    elif message.content.startswith(prefix+'byakko'):
        await bot.send_message(channel, "```Guarding Your Quarters ROOOOAAAARRRRRR```")
        
    elif message.content.startswith(prefix+'caaga'):
        await bot.send_message(channel, "```I LOVE KELZIII```")
     
    elif message.content.startswith(prefix+'ec'):
        await bot.send_message(channel, "```Warp Drive Wooshing Woosh Woosh```")
        
    elif message.content.startswith(prefix+'ace'):
        await bot.send_message(channel, "```Keels Everyone```")
        
    elif message.content.startswith(prefix+'invite'):
        await bot.send_message(channel, "There you go~ https://discordapp.com/oauth2/authorize?client_id=381111258172227585&scope=bot&permissions=0")
        
    elif message.content.startswith(prefix+'sugar'):
        em = discord.Embed()
        em.set_image(url = "https://cdn.discordapp.com/attachments/274387797140570112/382216656698474506/ScholarlyShamelessHarpseal.gif")
        
        await bot.send_message(channel, embed = em)
        
    elif message.content.startswith(prefix+'lola'):
        em = discord.Embed()
        em.set_image(url = "https://media.discordapp.net/attachments/382198685884481548/382545301765881856/ddef824a36b55e5089f00812c068222f.gif")
        
        await bot.send_message(channel, embed = em)
        
    elif message.content.startswith(prefix+'noble'):        
        em = discord.Embed()
        em.set_image(url = "https://78.media.tumblr.com/1400df496966e9f7ba648f56adbf134b/tumblr_olybb4pNly1sxa95wo4_540.gif")
        
        await bot.send_message(channel, embed = em)
        
    elif message.content.startswith(prefix+'tea'):        
        em = discord.Embed()
        em.set_image(url = "https://cdn.discordapp.com/attachments/300945555658637312/382930382418345984/giphy_5.gif")
        
        await bot.send_message(channel, embed = em)
        
    elif message.content.startswith(prefix+'galactic'):        
        em = discord.Embed()
        em.set_image(url = "https://cdn.discordapp.com/attachments/322410995127549952/383290728333180929/giphy.gif")
        
        await bot.send_message(channel, embed = em)
       
    elif message.content.startswith(prefix+'sparx'):
        em = discord.Embed()
        em.set_image(url = "https://cdn.discordapp.com/attachments/342395530837491726/381679556106518528/TIME_TO_STOP_-GLADE.gif")
        
        await bot.send_message(channel, embed = em)
    
    
    print("Starting......")
bot.run(settings["token"])
#bot.run("")
