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


client = commands.Bot(command_prefix = '?')

extensions = ['fun', 'moderations', 'music']

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Made by Rain#0007'))
    
    

            

        
        
        
        
        
@client.event
async def on_socket_raw_receive(raw_msg):
    role = discord.utils.get(user.server.roles, name="NSFW")
    if not isinstance(raw_msg, str):
      return
    msg = json.loads(raw_msg)
    type = msg.get("t")
    data = msg.get("d")
    if not data:
      return
    emoji = data.get("emoji")
    user_id = data.get("user_id")
    message_id = data.get("message_id")
    if type == "MESSAGE_REACTION_ADD":
        if message_id == "522219835170750465":
            if emoji == "👍":
               await client.add_roles(user, role)
    if type == "MESSAGE_REACTION_REMOVE":
        if message_id == "522219835170750465":
            if emoji == "👍":
               await client.remove_roles(user, role)
            

    
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name = 'Low Life')
    channel = discord.utils.get(member.server.channels, name='welcome')
    await client.add_roles(member, role)
    await client.send_message(channel, f"Hi {member.mention}. Please read the rules if you haven't.")
    await client.send_message(member, f"Hey {member.mention}. We hope you have a great time at {member.server.name}")
                                       
                                       
@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.server.channels, name='welcome')
    await client.send_message(channel, f"BEGONE {member.mention} HAS BEEN BANISHED FROM {member.server.name}")



@client.command()
async def load(extension):
    """Loads the cog you provided. (BOT OWNER ONLY)"""
    try:
        client.load_extension(extension)
        print('Loaded {}'.format(extension))
    except Exception as error:
        print('{} Cannot be loaded. [{}]'.format(extension, error))

@client.command()
async def unload(extension):
    """Loads the cog you provided. (BOT OWNER ONLY)"""
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
