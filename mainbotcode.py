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


#your code shouldn't cross this line!
client.run('token here')
