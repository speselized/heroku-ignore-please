import discord
import os
from discord.ext import commands
from discord import Permissions
import youtube_dl
import asyncio
import time
import logging
import discord, datetime, time
import random
from datetime import datetime
from discord import Game, InvalidArgument, HTTPException
import json
from os import system
from time import sleep
from discord import opus
from discord.ext import commands
from discord.utils import get

TOKEN = 'NDkwNDQ3NTUzMjIyMTQ4MDk3.Dn6o0g.I87hdy0DJps4vOcFuo34GmFNTt0'
client = commands.Bot(command_prefix = '?')

extensions = ['fun', 'moderations', 'music']

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Made by Rain#0007'))
    print('--------------------------------------------------------------------------------------------------------------')
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('')
    print('685 Lines of code has been loaded to your awesome bot!')
    print('')
    servers = list(client.servers)
    print("Connected on " +str(len(client.servers))+' servers')
    for x in range(len(servers)):
        print(' '+servers[x-1].name)
    print('--------------------------------------------------------------------------------------------------------------')
    
    
    
@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == 'welcome':
            msg = 'Welcome {} I hope you enjoy it at {} have fun.'.format(User.name, Server.name))
            await client.send_message(channel, msg)


@client.command()
async def load(extension):
    try:
        client.load_extension(extension)
        print('Loaded {}'.format(extension))
    except Exception as error:
        print('{} Cannot be loaded. [{}]'.format(extension, error))

@client.command()
async def unload(extension):
    try:
        client.unload_extension(extension)
        print('Unloaded {}'.format(extension))
    except Exception as error:
        print('{} Cannot be unloaded. [{}]'.format(extension, error))

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} Cannot be loaded. [{}]'.format(extension, error))

@client.command(pass_context=True, aliases=['i'])
async def iconify(ctx, *args):
    """(i) turns text into emoji. must have a string following the command"""
    def toNum(x):
        return {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}[x]

    def toIconCode(x):
        try: return ':' + toNum(int(x)) + ':'
        except Exception as e:
            if x == ' ': return '  '
            if x == '?': return ':question:'
            if x == '!': return ':exclamation:'
            else: return ':regional_indicator_' + x + ':'

    def make(s):
        icontext = ''
        for char in s:
            icontext += toIconCode(char)
            icontext += ' '
        return icontext
    iconstring = ''
    if args:
        args = ' '.join(args) # collapse ares to a string
        iconstring = args.lower()
        await client.say(ctx.message.author.mention + ' ' + make(iconstring))
    else:
        await client.say(ctx.message.author.mention + ' `Error: must specify a string`')
    await client.delete_message(ctx.message)
    print('iconify: ' + iconstring)


client.run(os.environ["TOKEN"])
