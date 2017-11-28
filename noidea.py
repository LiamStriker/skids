import discord
import asyncio
import json
import random
from cleverwrap import CleverWrap
import re
import datetime
bot = discord.Client()

cw = CleverWrap("CC5le3Skr2_bMWSnfcMNKvy_tOA")

try:
    file = open("settings/credentials.json",'r+')
    file = file.read()
    settings = json.loads(file)
except Exception as e:
    print(e)

def kiss_gif():
    links = ["http://i.imgur.com/0D0Mijk.gif", "http://i.imgur.com/TNhivqs.gif", "http://i.imgur.com/3wv088f.gif", "http://i.imgur.com/7mkRzr1.gif", "http://i.imgur.com/8fEyFHe.gif"]
    choice_made= random.choice(links)
    return choice_made

def slap_gif():
    links = ["http://imgur.com/Lv5m6cb.gif", "http://i.imgur.com/BsbFQtz.gif", "http://i.imgur.com/hyygFya.gif", "http://i.imgur.com/XoHjIlP.gif"]
    choice_made= random.choice(links)
    return choice_made

def hug_gif():
    links = ["http://i.imgur.com/sW3RvRN.gif", "http://i.imgur.com/gdE2w1x.gif", "http://i.imgur.com/zpbtWVE.gif", "http://i.imgur.com/ZQivdm1.gif", "http://i.imgur.com/MWZUMNX.gif"]
    choice_made= random.choice(links)
    return choice_made

def bite_gif():
    links = ["https://media.giphy.com/media/Qisbk5TesHmjC/giphy.gif","https://cdn.discordapp.com/attachments/383492139901911044/384283524355719168/hmmsu.gif", "https://cdn.discordapp.com/attachments/383492139901911044/384293280898088960/bitesu.gif"]
    choice_made= random.choice(links)
    return choice_made

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

        em = discord.Embed()
        em = discord.Embed(description = "The Best Ship :wink:")
        em.set_image(url = "https://media.discordapp.net/attachments/335346728897216512/382472973409320960/32e8d07153aa4d76b80250ac1297f30d.png?width=363&height=438")

        await bot.send_message(channel, embed = em)

    elif message.content.startswith(prefix+'liam'):
        await bot.send_message(channel, "```Mika's One And Only Little Vampy```")

    elif message.content.startswith(prefix+'byakko'):
        await bot.send_message(channel, "```Guarding Your Quarters ROOOOAAAARRRRRR```")

    elif message.content.startswith(prefix+'anna'):
        await bot.send_message(channel, "**Anna Says No**")

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

    elif message.content.startswith(prefix+'deadneko'):
         em = discord.Embed()
         em.set_image(url = "https://cdn.discordapp.com/attachments/365168714947231744/383867183488303111/giphy.gif")

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

    elif message.content.startswith('ami') or message.content.startswith('Ami'):
        query = message.content[3:].strip()
        k = cw.say("%s"%(query))
        await bot.send_message(channel, k)
        cw.reset()

    elif message.content.startswith(prefix+'user'):
        try:
            if message.content == prefix+'user':
                author = message.author
                discord.Member = author
                data = "\n"
                data += "Name: {}\n".format((str(discord.Member)))
                data += "ID: {}\n".format(discord.Member.id)
                passed = (message.timestamp - discord.Member.created_at).days
                data += "Created: {} days ago.\n".format(passed)
                passed = (message.timestamp - discord.Member.joined_at).days
                data += "Joined: {} days ago.\n".format(passed)
                data += "Server: {}\n".format(discord.Member.server)
                data += "Status: {}\n".format(discord.Member.status)
                self_info = data
                self_info_embed = discord.Embed(description = self_info)
                self_info_embed.set_author(name = "Info:")
                self_info_embed.colour = discord.Colour.red()
                self_info_embed.set_footer(text = "Helped By OP Noble ~ Liam", icon_url = bot.user.avatar_url)
                try:
                    await bot.send_message(message.channel,embed = self_info_embed)
                except Exception as e:
                    await bot.send_message(channel,str(e))
            else:
                tagged_user_id = message.content[len(prefix+'user'):].strip()
                user_id_numbers = ' '.join(tagged_user_id)
                user_id_space = re.sub(r'[^\w]', ' ', user_id_numbers)
                user_id_no_space = user_id_space.replace(' ','')
                member_id = message.author.server.get_member(user_id = user_id_no_space)
                discord.Member = member_id
                data = "\n"
                data += "Name: {}\n".format((str(discord.Member)))
                data += "ID: {}\n".format(discord.Member.id)
                passed = (message.timestamp - discord.Member.created_at).days
                data += "Created: {} days ago.\n".format(passed)
                passed = (message.timestamp - discord.Member.joined_at).days
                data += "Joined: {} days ago.\n".format(passed)
                data += "Server: {}\n".format(discord.Member.server)
                data += "Status: {}\n".format(discord.Member.status)
                other_info = data
                other_info_embed = discord.Embed(description = other_info)
                other_info_embed.set_author(name = "Info:")
                other_info_embed.colour = discord.Colour.red()
                self_info_embed.set_footer(text = "Helped By OP Noble ~ Liam", icon_url = bot.user.avatar_url)
                try:
                    await bot.send_message(message.channel,embed = other_info_embed)
                except Exception as e:
                    fmt = "`None`"
                    await bot.send_message(channel,"{}".format(fmt))
        except Exception as e:
            fmt = "`None`"
            await bot.send_message(channel,"{}".format(fmt))

    kiss = kiss_gif()
    if message.content.startswith('opkiss'):
        text= message.content[len('opkiss'):].split()
        em = discord.Embed()
        em.set_image(url = "{}".format(kiss))
        await bot.send_message(message.channel,content = "{0} **Has Been Kissed By** {1.mention}".format(text[0], message.author),embed = em)

    slap = slap_gif()
    if message.content.startswith('opslap'):
        text= message.content[len('opslap'):].split()
        em = discord.Embed()
        em.set_image(url = "{}".format(slap))
        await bot.send_message(message.channel,content = "{0} **Got Slapped By** {1.mention}".format(text[0], message.author),embed = em)

    hug = hug_gif()
    if message.content.startswith('ophug'):
        text= message.content[len('ophug'):].split()
        em = discord.Embed()
        em.set_image(url = "{}".format(hug))
        await bot.send_message(message.channel,content = "{0} **Has Been Hugged By** {1.mention}".format(text[0], message.author),embed = em)

    bite = bite_gif()
    if message.content.startswith('opbite'):
        text= message.content[len('opbite'):].split()
        em = discord.Embed()
        em.set_image(url = "{}".format(bite))
        await bot.send_message(message.channel,content = "{0} **Just Got Bitten By** {1.mention}".format(text[0], message.author),embed = em)



    print("Starting......")
bot.run(settings["token"])
#bot.run("")
