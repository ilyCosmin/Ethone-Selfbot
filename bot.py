#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__v__ = 1.2
count = 0
from aiohttp.helpers import TOKEN
import discord
import random
import string
import time
import sys
import os
import youtube_dl
from datetime import datetime, timedelta
from discord import message
from discord.ext import commands
from discord import Member
import asyncio
import json
import psutil
import requests
import pyfade
import ctypes
colorevery = 0xD302F4
cmd = "mode 90, 45"
os.system(cmd)
start = time.time()
if os.path.isfile("LICENSE") is True:
  os.remove("LICENSE")
if os.path.isfile("README.md") is True:
  os.remove("README.md")

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
    input("Press enter to exit...")
    os._exit(0)


ctypes.windll.kernel32.SetConsoleTitleW(f"Ethone | {__v__} | Commands used: {count} | Prefix: {prefix}")


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

    

def pfpUrl(id, pfp):
        url = ""
        if not str(pfp).startswith("http"):
            if str(pfp).startswith("a_"):
                url =  f"https://cdn.discordapp.com/avatars/{id}/{pfp}.gif?size=1024"
            else:
                url =  f"https://cdn.discordapp.com/avatars/{id}/{pfp}.png?size=1024"

            return url
        else:
            return pfp

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
    print_e(f"{prefix}{et.command.name}")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Ethone | {__v__} | Commands used: {count} | Prefix: {prefix}")


@Ethone.event
async def on_command_error(et, error):
    try:
        await et.message.delete()
    except:
        pass
    if isinstance(error, commands.CommandNotFound):
        print_e(f"Unknown command: {error}")
    elif isinstance(error, commands.CheckFailure):
        print_e(f"No embed perms")
    elif isinstance(error, commands.MissingRequiredArgument):
        print_e(f"Missing arguments: {error}")
    else:
        print_e(f"Error: {error}")

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
        embed.description = f"**`GENERAL COMMANDS`**\n`{prefix}help <category>` - returns all commands of that category\n`{prefix}ping` - return the bot's latency\n`{prefix}lockpc` - locking the pc\n`{prefix}shutdown` - shutdown the selfbot\n`{prefix}uptime` - returns the bot runtime\n`{prefix}sbinfo` - returns info about the selfbot"
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
        embed.description = f"**`TEXT COMMANDS`**\n`{prefix}kanye` - return random kanye west quote\n`{prefix}embed <message>` - return embed with your message\n`{prefix}firstmessage` - returns link to the first message\n`{prefix}sus <@user>` - returns sussymeter or user"
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
        await et.send(embed=embed, delete_after=delete_timer)
    
    
    elif str(category).lower() == "image":
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
        embed.description = f"**`IMAGE COMMANDS`**\n`{prefix}pfp <@user>` - return profile picture\n`{prefix}userbanner <@user>` - return profile banner\n`{prefix}ytthumbnail <yturl>` - returns high res thumbnail\n`{prefix}slap` - returns slap anime gif\n`{prefix}cuddle` - returns cuddle anime gif\n`{prefix}feed` - returns feed anime gif\n`{prefix}pat` - returns patpat anime uwu gif\n`{prefix}iphonex <@user>` - puts pfp in iphone\n`{prefix}awooify <@user>` - puts pfp in awooify\n`{prefix}baguette <@user>` - puts pfp in baguette\n`{prefix}cry` - returns cry anime gif\n`{prefix}clyde <message>` - returns clyde with message\n`{prefix}phcomment <@user> <comment>` - returns pornhub comment\n`{prefix}trumptweet <message>` - returns trumptweet\n`{prefix}mcachievment <message>` - returns minecraft achievment"
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
        embed.description = f"**`MISC COMMANDS`**\n`{prefix}newyear <year>` - return countdown till the year you want\n`{prefix}realping <ping>` - return fake ping\n`{prefix}nitrogen <amount>` - return fake nitro codes\n`{prefix}poll <poll>` - create pall with yes/no\n`{prefix}namemc <name>` - return list of mc names\n`{prefix}ytvideo <link>` - downloads youtube video to folder\n`{prefix}createserver` - creates server"
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
        await et.send(embed=embed, delete_after=delete_timer)
    
    
    elif str(category).lower() == "troll":
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
        embed.description = f"**`TROLL COMMANDS`**\n`{prefix}typing <seconds>` - typing nothing\n`{prefix}purgehack <number>` - return blank icons\n`{prefix}ghostping <@user>` - ghostping user\n`{prefix}nchannel` - deletes and clones the channel\n`{prefix}spamcategory <name> <number>` - create categories "
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
    await et.message.delete()
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


#image


@Ethone.command()
async def pfp(et, *, user: discord.User = None):
    if not user:
        user = et.author
    embed = discord.Embed(color=0xD302F4)
    embed.set_author(name="Ethone Selfbot", icon_url=f"")
    embed.add_field(name=("Profile picture"), value=f"`of {user}`", inline=False)
    embed.set_image(url=pfpUrl(user.id, user.avatar))
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


@Ethone.command()
async def uptime(et):
    embed = discord.Embed(color=0xD302F4)
    embed.set_author(name="Ethone Selfbot",icon_url=f"")
    embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
    embed.add_field(name=("Uptime"), value=f"`{str(timedelta(seconds=int(round(time.time() - start))))}`", inline=False)
    embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def poll(et, poll):
    embed = discord.Embed(color=0xD302F4)
    embed.set_author(name="Ethone Selfbot",icon_url=f"")
    embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
    embed.add_field(name=("Poll"), value=f"{poll}", inline=False)
    embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    message = await et.send(embed=embed, delete_after=delete_timer)
    await message.add_reaction("👍")
    await message.add_reaction("👎")


@Ethone.command()
async def namemc(et, username: str = None):
    embed = discord.Embed(color=0xD302F4)
    embed.set_author(name="Ethone Selfbot",icon_url=f"")
    request = requests.get(f"https://some-random-api.ml/mc?username={username}")
    data = request.json()
    history = data["name_history"]
    for i in range(len(history)):
        date_mc = history[i]["changedToAt"]
        embed.add_field(name=history[i]["name"], value=f"`{date_mc}`", inline=False)
    embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
    embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def phcomment(et, user: discord.User, *, comment):
    embed = discord.Embed(color=0xD302F4)
    embed.set_author(name="Ethone Selfbot", icon_url=f"")
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=phcomment&text={comment}&username={user.name}&image={str(user.avatar_url_as(format='png'))}".replace(" ", "%20"))
    res = r.json()
    embed.set_image(url=res["message"])
    embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def trumptweet(et, *, text):
    embed = discord.Embed(color=0xD302F4)
    embed.set_author(name="Ethone Selfbot", icon_url=f"")
    p = requests.get(f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}")
    embed.set_image(url=p.json()["message"])
    embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def sbinfo(et):
    global count
    embed = discord.Embed(color=0xD302F4)
    embed.set_author(name="Ethone Selfbot",icon_url=f"")
    embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
    embed.add_field(name=("Total Commands:"), value=f"`{int(len(Ethone.commands))}`", inline=False)
    embed.add_field(name=("Commands used in current session:"), value=f"`{count}`", inline=False)
    embed.add_field(name=("Version:"), value=f"`{__v__}`", inline=False)
    embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)
    
    
@Ethone.command()
async def mcachievment(et, *, text):
    embed = discord.Embed(color=0xD302F4)
    embed.set_author(name="Ethone Selfbot", icon_url=f"")
    embed.set_image(url=f"https://api.iapetus11.me/mc/achievement/{text.replace(' ', '%20')}")
    embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def ytvideo(et, youtube_url: str):
    try:
        with youtube_dl.YoutubeDL({}) as download:
            download.download([f"{youtube_url}"])
        embed = discord.Embed(color=0xD302F4)
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed.add_field(name="Success", value="Youtube video has been downloaded!\nCheck your selfbot folder!")
        embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
        await et.send(embed=embed, delete_after=delete_timer)
    except:
        embed.set_author(name="Ethone Selfbot", icon_url=f"")
        embed = discord.Embed(color=0xD302F4)
        embed.add_field(name="Error", value="Could not download video.")
        embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
        embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
        await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def firstmessage(et, channel: discord.TextChannel = None):
    channel = channel or et.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(title="Ethone Selfbot", description=f"[ First Message ]({first_message.jump_url})", color=0xD302F4)
    embed.set_thumbnail(url=f"https://media.discordapp.net/attachments/926206753203429468/926957919877079100/eth.png")
    embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def nchannel(et, channel: discord.TextChannel = None):
    channel = channel if channel else et.channel
    newchannel = await channel.clone()
    await channel.delete()


@Ethone.command()
async def sus(et, user: discord.User = None):
    user = user or et.author
    embed = discord.Embed(title="Ethone Selfbot", description=f"`{user} is {random.randrange(0, 100)}% sus`", color=0xD302F4)
    embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/927215390415798282/927233675689619496/ffdsff.png")
    embed.set_footer(text=f"{et.author} | Prefix: {prefix}", icon_url=et.author.avatar_url)
    await et.send(embed=embed, delete_after=delete_timer)


@Ethone.command()
async def spamcategory(et, name, amount: int):
    for i in range(amount):
        await et.guild.create_category(name=name)
        

@Ethone.command()
async def createserver(et, server_name="Ethone"):
    await Ethone.create_guild(name=server_name)
# Important!
Ethone.run(token, bot=False)
