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

extensions = ['fun', 'info', 'members', 'moderations', 'music', 'animals']

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

@client.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)
    
    await update_data(users, member)
    
    with open ('users.json', 'w') as f:
        json.dump(users, f)
  
@client.event
async def on_message(message):
    with open('users.json', 'r') as f:
        users = json.load(f)
        
    await update_data(users, message.author)
    await add_experience(users, message.author, 5)
    await level_up(users, message.author, message.channel)
                        
    
    with open ('users.json', 'w') as f:
        json.dump(users, f)
        
async def update_data(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]['experience'] = 0
        users[user.id]['level'] = 1
    
async def add_experience(users, user, exp):
    users[user.id]['experience'] += exp
    
async def level_up(users, user, channel):
    experience = users[user.id]['experience']
    lvl_start = users[user.id]['level']
    lvl_end = int(experience ** (1/4))
    
    if lvl_start < lvl_end:
        await client.send_message(channel, '{} has leveled up to level {}'.format(user.mention, lvl_end))
        users[user.id]['level'] = lvl_end
        await client.process_commands(message)

client.run(TOKEN)
