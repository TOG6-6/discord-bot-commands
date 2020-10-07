# DISCORD BOT COMMANDS
**I AM TRYING TO MAKE A PROJECT WHERE PEOPLE CAN MAKE DISCORD.PY BOTS WITH 0% KNOWLEDGE WITH PYTHON OR DISCORD.PY!**

Every Command You Would Ever Need For Your Discord.py Bot!

If You Need Any Help, Please Feel Free To DM Me: TOG6#6666
It Would Greatly Support Me If You Joined The Coolest Discord Server Ever: https://discord.gg/vSxuAbq

Also, Feel Free To Donate, If You Actually Do, I'll Make You A Custom Discord Bot XD - https://paypal.me/togs66

**ALSO, I'm always wanting to add more stuff to the bot, so feel free to tell me if you want me to add something, ill do it asap!**

# Notes
Ok, Let Me Explain...
For This Bot, You don't at all need any python experience, you just have to grab the necessary codes from each file into your main file!

For Example `mainbotcode.py` has the following code:
```
#main code starts here!
client = commands.Bot(command_prefix='$')#thats your command prefix
#whatever code you want to add, do it after this line


#your code shouldn't cross this line!
client.run('token here')
```
You just have to add your code in between!
You can get the necessary code from the py files in each folder just by copy pasting the codes!

# HOW TO START
**I'm going to assume you have 0% python knowledge for this one!**
[1] First things first, go to https://python.org and install python!
[2] In the Python installer, make sure enable `ADD PYTHON TO PATH` or `ADD PYTHON TO ENVIRONMENT VARIABLES`!
[3] You now need a compiler or an editor! - I personally use Visual Studio Code (https://code.visualstudio.com) But feel free to use whatever you like!
--- Good options are Codeblocks, Visual Studio, Pycharm, Atom, Anaconda Navigator, Sublime Text etc!
[4] Now open cmd and type pip - it will show you pip info!
--- If it doesn't contact me and I'll be happy to help! - https://discord.gg/vSxuAbq
[5] Type in the following commands 1 by 1:
```
pip install discord
pip install requests
pip install asyncio
pip install aiohttp
pip install urllib
pip install colorama
```
[6] Now that you have the necessary libraries, just install these source codes to your computer so you can start editing!

# HOW TO USE
It's something like how you try clothes in a store, but just that it's free XD, unless you want to donate!
Just open `mainbotcode.py` and keep it ready
Thennnn open the folders and add the necessary codes!

**FOR EXAMPLE:**
Taking Code From `moderator commands/kick.py`:
```
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        #await member.kick(reason=reason)
        await ctx.send("**`" + str(member) + "` was kicked from `" + str(ctx.guild.name) + "` by `" + (ctx.author.mention) + "` with reason: `" + str(reason) + "` succesfully!**")
    except:
        await ctx.send("** I don't thing you can kick `" + str(member) + "` " + ctx.author.mention + "**")
```
Adding it `mainbotcode.py`:
```
#main code starts here!
client = commands.Bot(command_prefix='$')#thats your command prefix
#whatever code you want to add, do it after this line

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        #await member.kick(reason=reason)
        await ctx.send("**`" + str(member) + "` was kicked from `" + str(ctx.guild.name) + "` by `" + (ctx.author.mention) + "` with reason: `" + str(reason) + "` succesfully!**")
    except:
        await ctx.send("** I don't thing you can kick `" + str(member) + "` " + ctx.author.mention + "**")

#your code shouldn't cross this line!
client.run('token here')
```
# NECESSARY IMPORTS YOU MAY WANNA ADD:
```
#discord imports                                                                          #pip install discord
import discord
import discord.ext.commands
from discord.ext.commands import bot
from discord import Game
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.commands import errors
import discord.utils
from discord.utils import find, get
import asyncio                                                                            #pip install asyncio
import aiohttp                                                                            #pip install aiohttp

#necessary imports
import platform
import os
import random
import string
import requests                                                                           #pip install requests
import math
import colorama                                                                           #pip install colorama
import steam                                                                              #pip install steam
import binascii
import subprocess
import json
import sys
import colorsys                                                                           #pip install colorsys
import time
import urllib, urllib3                                                                    #pip install urllib
import datetime                                                                           #pip install datetime
import webbrowser                                                                         #pip install webbrowser
import collections                                                                        #pip install collections
import art                                                                                #pip install art/ pip install text2art
#feel free to add more
```

**That's all! - NO PYTHON KNOWLEDGE REQUIRED XD! - THIS SHOULD LITERALLY TAKE YOU 15 Minutes!**

**AGAIN, IF YOU NEED HELP: https://discord.gg/vSxuAbq
IF YOU WANT TO DONATE: https://paypal.me/togs66 **
