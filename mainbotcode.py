#discord imports - pip install discord
import discord
import discord.ext.commands
from discord.ext.commands import bot
from discord import Game
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.commands import errors
import discord.utils
from discord.utils import find, get
import asyncio
import aiohttp

#necessary imports
import platform
import os
import random
import string
import requests #pip install requests
#feel free to add more

ownerdude = () #add your discord id here - not token, discord id
#main code starts here!
client = commands.Bot(command_prefix='$')#thats your command prefix
#whatever code you want to add, do it after this line

@client.event
async def on_ready():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(Fore.LIGHTCYAN_EX +"""
████████╗████████╗  ░░░░░░  ██████╗░░█████╗░████████╗
╚══██╔══╝╚══██╔══╝  ░░░░░░  ██╔══██╗██╔══██╗╚══██╔══╝
░░░██║░░░░░░██║░░░  █████╗  ██████╦╝██║░░██║░░░██║░░░
░░░██║░░░░░░██║░░░  ╚════╝  ██╔══██╗██║░░██║░░░██║░░░
░░░██║░░░░░░██║░░░  ░░░░░░  ██████╦╝╚█████╔╝░░░██║░░░
░░░╚═╝░░░░░░╚═╝░░░  ░░░░░░  ╚═════╝░░╚════╝░░░░╚═╝░░░""")
    print(Fore.MAGENTA +"======================================================")
    print(Fore.RED +"Logged in as:", client.user.name, "| ID:", client.user.id)
    print(Fore.MAGENTA +"======================================================")
    kioas = str(len(client.guilds))
    print(Fore.CYAN + "Present In The Tog6 Server!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("I am TOG Mate, DM me, not anyone else XD!"))
    print(Fore.BLUE + "I am TOG Mate, DM me, not anyone else XD!")
    print(Fore.LIGHTYELLOW_EX + "TT - BOT was started at: " + current_time)
    print(" ")
    print(Fore.GREEN +"Built by TOG6")
    print("Welcome!")
    print(Fore.LIGHTCYAN_EX +" ")

#your code shouldn't cross this line!
client.run('token here')
