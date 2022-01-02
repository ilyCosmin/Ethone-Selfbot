#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__v__ = 1.0
count = 0
import discord
import random
import string
import sys
import os
import subprocess
import logging
from datetime import datetime
from pause import time
from discord import Member
import json
import requests
import asyncio
import pyfade
import ctypes
colorevery = 0xD302F4
cmd = "mode 90, 45"
os.system(cmd)
try:
    from pause import sleep
except ModuleNotFoundError:
    os.system('cmd /c "pip install pause"')
try:
    from rich import box
except ModuleNotFoundError:
    os.system('cmd /c "pip install rich"')
try:
    from rich.console import Console
except ModuleNotFoundError:
    os.system('cmd /c "pip install rich"')
try:
    from rich.table import Table
except ModuleNotFoundError:
    os.system('cmd /c "pip install rich"')
try:
    from rich.text import Text
except ModuleNotFoundError:
    os.system('cmd /c "pip install rich"')
try: 
    import requests
except ModuleNotFoundError:
    os.system('cmd /c "pip install requests"')
try: 
    from sty import fg, bg, ef, rs, Style, RgbFg
except ModuleNotFoundError:
    os.system('cmd /c "pip install sty"')
try:
    from discord.ext import commands
except ModuleNotFoundError:
    os.system('cmd /c "pip install discord.py"')
try: 
    import asyncio
except ModuleNotFoundError:
    os.system('cmd /c "pip install asyncio"')
import json


def print_e(txt):
    time=datetime.now().strftime("%H:%M")
    print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_purple, text=f"[{time} | Ethone] {txt}"))


def cls():
    os.system("cls")


with open("config.json") as f:
    config = json.load(f)
    prefix = config["Main"]["Prefix"]
    delete_timer = config["Main"]["Delete timer"]
    token = config["Login"]["Token"]
__headers__={'authorization': token, "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36"}
Ethone = commands.Bot(command_prefix=prefix, self_bot=True, case_insensitive=True)
api="https://discord.com/api/v9/"
r = requests.get('https://discord.com/api/v6/users/@me', headers=__headers__)
cls()
if r.status_code == 200:
    pass
else:
    print_e("Failed to connect to token in config.json! Please enter a valid one and restart.")
    sleep(2)
    os._exit(0)


def friends():
    request = requests.get("https://discord.com/api/users/@me/relationships", headers={"Authorization": token})
    json = request.json()
    friends = []
    for item in json:
        if item["type"] == 1:
            friends.append(item["user"])
    return friends


@Ethone.event
async def on_ready():
    print(pyfade.Fade.Vertical(pyfade.Colors.blue_to_purple, text = f"""

                   ███████╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗███████╗                                   
                   ██╔════╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║██╔════╝                                   
                   █████╗     ██║   ███████║██║   ██║██╔██╗ ██║█████╗                                     
                   ██╔══╝     ██║   ██╔══██║██║   ██║██║╚██╗██║██╔══╝                                     
                   ███████╗   ██║   ██║  ██║╚██████╔╝██║ ╚████║███████╗                                   
                   ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝                   """))
    print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_purple, text = f"""┌────────────────────────────────────────────────────────────────────────────────────────┐"""))
    print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_purple, text = f"Connected: {Ethone.user.name}#{Ethone.user.discriminator} | Servers: {len(Ethone.guilds)} | Friends: {len(friends())}".center(os.get_terminal_size().columns)))
    print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_purple, text = f"""└────────────────────────────────────────────────────────────────────────────────────────┘"""))

    

Ethone.remove_command("help") 

## help


@Ethone.event
async def on_command(et):
    global count
    count += 1
    try:
        await et.message.delete()
    except:
        pass
    print_e(et.command.name)
    ctypes.windll.kernel32.SetConsoleTitleW(f"Ethone | {__v__} | Commands used: {count}")

@Ethone.event
async def on_command_error(et, error):
    if isinstance(error, commands.CommandNotFound):
        try:
            await et.message.delete()
        except:
            pass
    else:
        print_e(f"Error: {error}")
        try:
            await et.message.delete()
        except:
            pass


@Ethone.command()
async def help(et, category=None):
    await et.message.delete()
    if category is None:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot",
                         icon_url=f"")
        embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
        embed.add_field(name=f"`{prefix}HELP GENERAL`", value="Shows all general commands", inline=False)
        embed.add_field(name=f"`{prefix}HELP ACCOUNT`", value="Shows all account commands", inline=False)
        embed.add_field(name=f"`{prefix}HELP TEXT`", value="Shows all text commands", inline=False)
        embed.add_field(name=f"`{prefix}HELP IMAGE`", value="Shows all image manipulation commands", inline=False)
        embed.add_field(name=f"`{prefix}HELP NSFW`", value="Shows all nsfw commands", inline=False)
        embed.add_field(name=f"`{prefix}HELP MISC`", value="Shows all miscellaneous commands", inline=False)
        embed.add_field(name=f"`{prefix}HELP TROLL`", value="Shows all troll commands", inline=False)
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
        await et.send(embed=embed, delete_after=delete_timer)
    
    
    elif str(category).lower() == "general":
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
        embed.description = f"**`GENERAL COMMANDS`**\n`{prefix}help <category>` - returns all commands of that category\n`{prefix}uptime` - return how long the selfbot has been running\n`{prefix}prefix <prefix>` - changes the bot's prefix\n`{prefix}ping` - return the bot's latency\n`{prefix}lockpc` - locking the pc\n`{prefix}shutdown` - shutdown the selfbot"
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
        await et.send(embed=embed, delete_after=delete_timer)
    
    
    elif str(category).lower() == "account":
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
        embed.description = f"**`ACCOUNT COMMANDS`**\n`{prefix}hypesquad <house>` - Bravery, Brilliance, Balance, Clear\n`{prefix}leaveallservers` - leaving all servers\n`{prefix}dmallf <message>` - dming all friends\n`{prefix}Lightmode / Darkmode` - Changing Discord theme"
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
        await et.send(embed=embed, delete_after=delete_timer)
    
    
    elif str(category).lower() == "text":
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
        embed.description = f"**`TEXT COMMANDS`**\n`{prefix}kanye` - return random kanye west quote\n`{prefix}embed <message>` - return embed with your message"
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
        await et.send(embed=embed, delete_after=delete_timer)
    
    
    elif str(category).lower() == "image":
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
        embed.description = f"**`IMAGE COMMANDS`**\n`{prefix}pfp <@user>` - return profile picture\n`{prefix}userbanner <@user>` - return profile banner\n`{prefix}ytthumbnail <yturl>` - returns high res thumbnail\n`{prefix}slap` - returns slap anime gif\n`{prefix}cuddle` - returns cuddle anime gif\n`{prefix}pat` - returns patpat anime uwu gif\n`{prefix}iphonex <@user>` - puts pfp in iphone\n`{prefix}awooify <@user>` - puts pfp in awooify\n`{prefix}baguette <@user>` - puts pfp in baguette\n`{prefix}cry` - returns cry anime gif\n`{prefix}clyde <message>` - returns clyde with message"
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
        await et.send(embed=embed, delete_after=delete_timer)
    
    
    elif str(category).lower() == "nsfw":
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
        embed.description = f"**`NSFW COMMANDS`**\n`{prefix}floydsus` - returns sussy floyd\n`{prefix}hthigh` - returns hentai thighs\n`{prefix}thigh` - returns real thighs\n`{prefix}paizuri` - returns tiddy fuck\n`{prefix}boobs` - returns hentai boobs\n`{prefix}ass` - returns real ass\n`{prefix}lewdkemo` - idfk what this is\n`{prefix}gasm` - just gasm\n`{prefix}avatar` - avatar (could be nsfw)\n`{prefix}les` - hentai I guess\n`{prefix}bj` - Just blowjob\n`{prefix}pwankg` - sussy pwankging\n`{prefix}lick` - ligma\n`{prefix}lesbian` - gey"
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
        await et.send(embed=embed, delete_after=delete_timer)
    
    
    elif str(category).lower() == "misc":
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
        embed.description = f"**`MISC COMMANDS`**\n`{prefix}newyear <year>` - return countdown till the year you want\n`{prefix}realping <ping>` - return fake ping\n`{prefix}nitrogen <amount>` - return fake nitro codes"
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
        await et.send(embed=embed, delete_after=delete_timer)
    
    
    elif str(category).lower() == "troll":
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
        embed.description = f"**`TROLL COMMANDS`**\n`{prefix}typing <seconds>` - typing nothing\n`{prefix}purgehack <number>` - return blank icons\n`{prefix}ghostping <@user>` - ghostping user"
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
        await et.send(embed=embed, delete_after=delete_timer)

## help


@Ethone.command()
async def newyear(et, year: int):
    def dateDiffInSeconds(date1, date2):
        timedelta = date2 - date1
        return timedelta.days * 24 * 3600 + timedelta.seconds

    def daysHoursMinutesSecondsFromSeconds(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        return (days, hours, minutes, seconds)

    req = datetime.strptime(f"{year}-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    now = datetime.now()
    embed = discord.Embed(color=0xD302F4)
    embed.set_author(name="Ethone Selfbot",icon_url=f"")
    embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
    embed.add_field(name=("%dd %dh %dm %ds" % daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, req))), value=f"`Till year: {year}`", inline=False)
    embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def kanye(et):
    res = requests.get(f"https://api.kanye.rest/")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot",icon_url=f"")
        embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
        embed.add_field(name=("Kanye"), value=(res.json()["quote"])+" ~ Kanye", inline=False)
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
        await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def shutdown(et):
    sys.exit()


@Ethone.command()
async def embed(et, message):
    embed = discord.Embed(color=0xD302F4, description=f"{message}")
    await et.send(embed=embed, delete_after=delete_timer)


#nsfw

@Ethone.command()
async def floydsus(et):
    embed = discord.Embed(color=0xD302F4)
    embed.set_author(name="Floyd sussy baka Selfbot",
                        icon_url=f"")
    embed.set_image(url="https://cdn.discordapp.com/attachments/926206753203429468/926544053275869195/0gimTIB_-_Imgur.gif")
    embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def hthigh(et):
    res = requests.get(f"https://nekobot.xyz/api/image?type=hthigh")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_image(url=res.json()["message"])
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def thigh(et):
    res = requests.get(f"https://nekobot.xyz/api/image?type=thigh")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_image(url=res.json()["message"])
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def paizuri(et):
    res = requests.get(f"https://nekobot.xyz/api/image?type=paizuri")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_image(url=res.json()["message"])
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def boobs(et):
    res = requests.get(f"https://nekos.life/api/v2/img/boobs")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_image(url=res.json()["url"])
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def ass(et):
    res = requests.get(f"https://nekobot.xyz/api/image?type=ass")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_image(url=res.json()["message"])
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def lewdkemo(et):
    res = requests.get(f"https://nekos.life/api/v2/img/lewdkemo")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_image(url=res.json()["url"])
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def gasm(et):
    res = requests.get(f"https://nekos.life/api/v2/img/gasm")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_image(url=res.json()["url"])
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def avatar(et):
    res = requests.get(f"https://nekos.life/api/v2/img/avatar")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_image(url=res.json()["url"])
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def les(et):
    res = requests.get(f"https://nekos.life/api/v2/img/les")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_image(url=res.json()["url"])
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def bj(et):
    res = requests.get(f"https://nekos.life/api/v2/img/bj")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_image(url=res.json()["url"])
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def pwankg(et):
    res = requests.get(f"https://nekos.life/api/v2/img/pwankg")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_image(url=res.json()["url"])
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def lick(et):
    res = requests.get(f"http://api.nekos.fun:8080/api/lick")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_image(url=res.json()["image"])
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def lesbian(et):
    res = requests.get(f"http://api.nekos.fun:8080/api/lesbian")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_image(url=res.json()["image"])
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


#nsfw

#@Ethone.command()
#async def cloneprofile(et, member: Member = None):
#    if not member:
#        member = et.author
#    with open (f"{member.avatar_url}") as f:
#        image = f.read()
#        await Ethone.user.edit(avatar=image)

#image

@Ethone.command()
async def pfp(et, member: Member = None):
    if not member:
        member = et.author
    embed = discord.Embed(color=0xD302F4)
    embed.set_author(name="Ethone Selfbot",
                        icon_url=f"")
    embed.add_field(name=("Profile picture"), value=f"`of {member}`", inline=False)
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def slap(et):
    res = requests.get(f"https://nekos.life/api/v2/img/slap")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_image(url=res.json()["url"])
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def cuddle(et):
    res = requests.get(f"https://nekos.life/api/v2/img/cuddle")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_image(url=res.json()["url"])
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def pat(et):
    res = requests.get(f"https://nekos.life/api/v2/img/pat")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_image(url=res.json()["url"])
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def iphonex(et, user: discord.User):
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=iphonex&url={user.avatar_url}")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_image(url=res.json()["message"])
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def awooify(et, user: discord.User):
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=awooify&url={user.avatar_url}")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_image(url=res.json()["message"])
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def cry(et):
    res = requests.get(f"http://api.nekos.fun:8080/api/cry")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_image(url=res.json()["image"])
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def feed(et):
    res = requests.get(f"http://api.nekos.fun:8080/api/feed")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_image(url=res.json()["image"])
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def baguette(et, user: discord.User):
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=baguette&url={user.avatar_url}")
    if res.status_code == 200:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_image(url=res.json()["message"])
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def clyde(et, message):
    res = requests.get(f"https://nekobot.xyz/api/imagegen?type=clyde&text={message}")
    if res.status_code == 200:
        return await et.send(res.json()["message"])


#image

@Ethone.command()
async def realping(et, number: int):
    embed = discord.Embed(color=0xD302F4)
    embed.set_author(name="Ethone Selfbot", icon_url=f"")
    embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
    embed.add_field(name="Ping", value=f"`{number}ms`")
    embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def ping(et):
    embed = discord.Embed(color=0xD302F4)
    embed.set_author(name="Ethone Selfbot", icon_url=f"")
    embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
    embed.add_field(name="Ping", value=f"`{round(Ethone.latency * 1000)}ms`")
    embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def hypesquad(et, hype_house: str):
    houses = {"bravery": 1, "brilliance": 2, "balance": 3}
    hype_house = hype_house.lower()
    if hype_house in houses:
        h={'house_id': houses[hype_house]}
        r=requests.post("https://discord.com/api/v9/hypesquad/online", headers=__headers__, json=h)
        house_value=f"`Changed hypesquad to {hype_house}`"
    elif hype_house == "clear":
        r=requests.delete("https://discord.com/api/v9/hypesquad/online", headers=__headers__)
        house_value=f"`Cleared hypesquad house`"
    else:
        house_value=f"`Invalid option, please pick one of these: bravery, brilliance, balance, clear`"
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
        embed.add_field(name="Hypesquad", value=house_value)
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
        await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def nitrogen(et, num: int):
    with open("nitrocodes.txt", "w") as f:
        for i in range(num): 
            code = "".join(random.choices(
                string.ascii_uppercase + string.digits + string.ascii_lowercase,
                k = 16
            )) 
            f.write(f"https://discord.gift/{code}\n")
    with open("nitrocodes.txt", "rb") as file:
        await et.send(file=discord.File(file, "nitrocodes.txt"))
    os.remove("nitrocodes.txt")
    print_e("nitrogen: Sent nitrocodes.txt")


@Ethone.command()
async def typing(et, time: int):
    print_e(f"typing: Starting typing for {time} seconds")
    async with et.typing():
        await asyncio.sleep(time)
    print_e(f"typing: Finished typing")


@Ethone.command()
async def purgehack(et, amount=1):
    for i in range(amount):
        await et.send("ﾠ"+"\n" * 400 + "ﾠ")
        await asyncio.sleep(1)


@Ethone.command()
async def ytthumbnail(et, yt_url):
    if "https://youtu.be/" in yt_url:
        a,b,c,d=yt_url.split("/")
        video_id=d
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.add_field(name=("Ytthumbnail"), value=f"`of {yt_url}`", inline=False)
        embed.set_image(url=f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg")
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
        await et.send(embed=embed, delete_after=delete_timer)
    elif "youtube.com/watch?v" in yt_url:
        a,b=yt_url.split("=")
        video_id=b
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.add_field(name=("Ytthumbnail"), value=f"`of {yt_url}`", inline=False)
        embed.set_image(url=f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg")
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
        await et.send(embed=embed, delete_after=delete_timer)
    else:
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
        embed.add_field(name="Ytthumbnail", value=f"`Invalid url: {yt_url}`")
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
        await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def leaveallservers(et):
    try:
        leave_all_servers_request = requests.get(
            "https://canary.discord.com/api/v9/users/@me/guilds", headers=__headers__
        ).json()
        for guild in leave_all_servers_request:
            requests.delete(
                f"https://canary.discord.com/api/v9/users/@me/guilds/{guild['id']}",
                headers=__headers__,
            )
        print_e("leaveallservers: Left all servers")
    except:
        pass


@Ethone.command()
async def dmallf(et, message):
    r=requests.get(
        "https://canary.discord.com/api/v9/users/@me/channels", headers=__headers__
    ).json()
    for channel in r:
        json = {"content": message}
        r = requests.post(
            f"https://canary.discord.com/api/v9/channels/{channel['id']}/messages",
            headers=__headers__,
            data=json,
        )
        await asyncio.sleep(2)


@Ethone.command()
async def lockpc(et):
	os.system("rundll32.exe user32.dll,LockWorkStation")


@Ethone.command()
async def lightmode(et):
    requests.patch("https://canary.discordapp.com/api/v9/users/@me/settings",headers=__headers__, json={'theme': "light"})


@Ethone.command()
async def darkmode(et):
    requests.patch("https://canary.discordapp.com/api/v9/users/@me/settings",headers=__headers__, json={'theme': "dark"})


@Ethone.command()
async def userbanner(et, user:discord.Member=None):
    if user == None:
        user = et.author
    req = await Ethone.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
    banner_id = req["banner"]
    if banner_id:
        banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}.gif"
        is_a_gif = requests.get(banner_url, timeout=3)
        if is_a_gif.status_code != 200:
            banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}.png"
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.add_field(name=("Profile Banner"), value=f"`of {user}`", inline=False)
        embed.set_image(url=f"{banner_url}?size=1024")
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
        await et.send(embed=embed, delete_after=delete_timer)
    else:
        req = await Ethone.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
        banner_hex = req["banner_color"]
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.add_field(name=("Profile Banner"), value=f"`of {user}`\n`Hex code: {banner_hex}`", inline=False)
        embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
        await et.send(embed=embed, delete_after=delete_timer)
        

@Ethone.command(aliases=["reboot", "reload"])
async def restart(et):
    await et.message.delete()
    python = sys.executable
    os.execl(python, python, * sys.argv)


@Ethone.command()
async def ghostping(et, msg):
    await et.message.delete()

# Important!
Ethone.run(token, bot=False)


