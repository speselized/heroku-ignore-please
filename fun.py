import discord
import os
from discord.ext import commands
from discord import Permissions
import youtube_dl
import asyncio
import async_timeout
import aiohttp
import json
import time
import logging
import discord, datetime, time
import random
from datetime import datetime
from discord import Game, InvalidArgument, HTTPException
from os import system
from random import randint
from time import sleep
from discord import opus
from discord.ext import commands
from discord.utils import get

class Fun:
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def banne(self, ctx, member : discord.Member):
        """Fake bans the user you provided in the string"""
            await client.delete_message(ctx.message)
            await client.say("***<:greentick:503040447741165569> {0} has been banned!***".format(member))



    @commands.command(pass_context=True)
    async def bam(self, ctx, member : discord.Member):
        """Fake bans so the bot says you got banned even tho you didn't"""
            await self.client.delete_message(ctx.message)
            await self.client.say("***<:greentick:503040447741165569> {0} has been banned!***".format(member))


        
        
    @commands.command(name="8ball")
    async def _ball(self, ctx):
        """Magic 8ball. SPOOKY"""
        await self.client.say(random.choice(["It is certain"," It is decidedly so","Without a doubt","Yes, definitely","You may rely on it","As I see it, yes"," Most likely","Outlook good","Yes","Signs point to yes"," Reply hazy try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]))
        await self.client.add_reaction("🎱")



    @commands.command(pass_context=True)
    async def slap(self, ctx, member : discord.Member):
        """Slaps the user you provided in the string!"""
        author = ctx.message.author
        if member.id == ctx.message.author.id:
            await self.client.say(ctx.message.author.mention + ", you cannot slap yourself.")
            return
        else:
            await self.client.say("**{0} slaps {1} around a bit with a large, girthy trout** <:fishslap:504195777564770314> :hand_splayed: :dizzy_face: ".format(author, member))



            
            
    @commands.command(pass_context=True, aliases=['d'])
    async def dog(self, ctx):
        """(d) random dog picture"""
        print('dog')
        isVideo = True
        while isVideo:
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://random.dog/woof.json') as r:
                    res = await r.json()
                    res = res['url']
                    cs.close()
            if res.endswith('.mp4'):
                pass
            else:
                isVideo = False
        em = discord.Embed()
        await self.client.send_message(ctx.message.channel, content=ctx.message.author.mention, embed=em.set_image(url=res))
        await self.client.delete_message(ctx.message)
        


    @commands.command(pass_context=True)
    async def spank(self, ctx, member : discord.Member):
        """Naughty Naughty"""
        author = ctx.message.author
        if member.id == ctx.message.author.id:
            await self.client.say(ctx.message.author.mention + ", Oh I mean don\'t spank yourself that\'s just wrong bro I am not getting a belt and whooping your ass sorry.")
            await self.client.delete_message(ctx.message)
            return
        else:
            await self.client.say(random.choice(['{0} spanked {1}', '{0} clobbered {1}', '{0} paddled {1}', '{0} whipped {1}', '{0} punished {1}', '{0} caned {1}', '{0} thrashed {1}', '{0} smacked {1}']).format(author ,member))
            await self.client.delete_message(ctx.message)


    @commands.command(pass_context=True)
    async def hug(self, ctx, member : discord.Member):
        """HUGGY HUGGY"""
        author = ctx.message.author
        if member.id == ctx.message.author.id:
            await self.client.say(ctx.message.author.mention + ", You\'re that lonely? Wow well anyway I give {} a big hug! :hugging: ".format(author))
            return
        else:
            await self.client.say(random.choice(['*{0} Hugs {1}*', '*{0} Licks {1}*', '*{0} Pounces {1}*', '*{0} Jumps on {1}*', '*{0} Wrestles {1}*', '*{0} Falls on {1}*']).format(author ,member))





    @commands.command(pass_context=True)
    async def fight(self, ctx):
        """Fight that stupid cunt you wanna smash his skull in."""
        message = ctx.message
        args = message.content.split()
        if "Staff" in [role.name for role in message.author.roles]:
            loss = 0
            init = message.author.mention
            target = args[1]

            while not loss == 1:
                fight = random.choice(["%s threw a chair at %s" % (init, target), "%s whacked %s with a stick" % (init, target), "%s slapped %s to the floor" % (init, target), "%s threw %s through a wall" % (init, target)])
                await self.client.say(fight)
                await asyncio.sleep(2)
                loss = random.randint(1, 3)
                if loss == 1:
                    await self.client.say("%s accepts defeat! %s has won the fight!" % (target, init))
                else:
                    await self.client.say("%s does not giveup and continues the fight!" % (target))

                temp = target
                target = init
                init = temp
                await asyncio.sleep(4)
        else:
            await self.client.say("[403] You do not have permission to use this command")



    @commands.command(pass_context=True)
    async def reverse(self, ctx, *, message):
        """REVERSE MORE LIKE ESREVER"""
        if 'enoyreve@' in message:
            await self.client.say("Haha nice try but u r gay.")
            await self.client.delete_message(ctx.message)
            return

        elif 'ereh@' in message:
            await self.client.say("Haha nice try but u r gay.")
            await self.client.delete_message(ctx.message)
            return

        elif message == message[::-1]:
            await self.client.say("{} ".format(message) + "(It's a Palindrome)")

        else:
            await self.client.say("{}".format(message)[::-1])





    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """PONG"""
        resp = await self.client.say('Pong! Loading...')
        diff = resp.timestamp - ctx.message.timestamp
        await self.client.edit_message(resp, f'Pong! That took {1000*diff.total_seconds():.1f}ms.')



    @commands.command(pass_context=True)
    async def gay(self, ctx, user: discord.Member):
        """My sir you have 900% gayness"""
        rnd = random.randint(1, 100)
        emb = discord.Embed(title="{} is {}% gay!".format(user.name, rnd), color=0xffffff)
        emb.set_footer(text="Command runned by {}".format(ctx.message.author.name))
        await self.client.say(embed=emb)

    @commands.command(pass_context=True)
    async def pp(self, ctx, user: discord.Member):
        """you got small pp lmao like logan paul and jake paul ew"""
        rnd = random.randint(1, 100)
        emb = discord.Embed(title="{} has {} inch pp!".format(user.name, rnd), color=0xffffff)
        emb.set_footer(text="Command runned by {}".format(ctx.message.author.name))
        await self.client.say(embed=emb)

    @commands.command(pass_context=True)
    async def pong(self, ctx):
        """STOP"""
        msg = await self.client.say('Hey, stop that.')
        await asyncio.sleep(5)
        await self.client.delete_message(msg)


    @commands.command(pass_context=True)
    async def spellout(self, ctx, *, msg:str):
        """S P E L L O U T"""
        await self.client.say(" ".join(list(msg.upper())))


    @commands.command(pass_context=True)
    async def nou(self, ctx):
        """no u"""
        await self.client.say("no u")


    @commands.command(pass_context=True)
    @commands.has_permissions(ban_members=True)
    async def spam(self, ctx, user: discord.Member, amount: int, *, content):
        """SPAM THAT NIGGA"""
        if amount > 20:
            await self.client.say("Can't spam over 20.")
            return
        elif '@everyone' in content:
            await self.client.say("Nice try.")
            return
        elif '@here' in content:
            await self.client.say("Nice try.")
            return

        messages = 0
        while messages < amount:
            await self.client.say('<@{}> {}'.format(user.id, content))
            messages = messages + 1
            await asyncio.sleep(0.2)

        # example of command is '?spam @user 10 wake up'
        # this will make the bot ping the user 10 times and say wake up.

    @spam.error
    async def spam_error(self, error, ctx):
        if isinstance(error, discord.ext.commands.CheckFailure):
            userID = (ctx.message.author.id)
            await self.client.send_message(ctx.message.author,"<@%s>: **You don't have permission to perform this action**" % (userID))
            await self.client.delete_message(ctx.message)

        elif isinstance(error, discord.ext.commands.MissingRequiredArgument):
            await self.client.say('Missing Required Argument. ```?spam @user 10 wake up```')
            await self.client.delete_message(ctx.message)




    @commands.command(pass_context=True)
    async def coinflip(self, ctx):
        """Flips a coin."""
        if random.randint(0, 1): await self.client.say('***Heads***')
        else: await self.client.say('***Tails***')

    @commands.command(pass_context=True)
    async def flip(self, ctx):
        """Flips a coin."""
        if random.randint(0, 1): await self.client.say('***Heads***')
        else: await self.client.say('***Tails***')

    @commands.command(pass_context=True)
    async def coin(self, ctx):
        """Flips a coin."""
        if random.randint(0, 1): await self.client.say('***Heads***')
        else: await self.client.say('***Tails***')




def setup(client):
    client.add_cog(Fun(client))
