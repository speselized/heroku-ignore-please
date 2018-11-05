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
from discord.ext.commands import has_permissions
from discord.utils import get

class Moderations:
    def __init__(self, client):
        self.client = client


    @commands.command(pass_context=True)
    @commands.has_role('Staff')
    async def permit(self, ctx, user: discord.Member):
        role = discord.utils.get(user.server.roles, name="Image Perms")
        await self.client.delete_message(ctx.message)
        await self.client.add_roles(user, role)
        embed= discord.Embed(title="Permit.", description="***{} has been given permission to post images / links!*** ".format(user.mention), color=0xF35353)
        await self.client.say(embed=embed)


    @commands.command(pass_context=True)
    @commands.has_role('Staff')
    async def approve(self, ctx, user: discord.Member):
        role = discord.utils.get(user.server.roles, name="Image Perms")
        await self.client.delete_message(ctx.message)
        await self.client.add_roles(user, role)
        embed= discord.Embed(title="Permit.", description="***{} has been given permission to post images / links!*** ".format(user.mention), color=0xF35353)
        await self.client.say(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_role('Staff')
    async def perm(self, ctx, user: discord.Member):
        role = discord.utils.get(user.server.roles, name="Image Perms")
        await self.client.delete_message(ctx.message)
        await self.client.add_roles(user, role)
        embed= discord.Embed(title="Permit.", description="***{} has been given permission to post images / links!*** ".format(user.mention), color=0xF35353)
        await self.client.say(embed=embed)


    @commands.command(pass_context=True)
    @commands.has_role('Staff')
    @commands.has_permissions(ban_members=True)


    async def bans(self, ctx):
        ban_list = await self.client.get_bans(ctx.message.server)

        # Show banned users
        await self.client.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

        # Unban last banned user
        if not ban_list:

            await self.client.say('Ban list is empty.')
            return







    @commands.command(pass_context=True)
    async def invite(self, ctx):
            invitelinknew = await self.client.create_invite(destination = ctx.message.channel, xkcd = True, max_uses = 100)
            embedMsg=discord.Embed(color=0xf41af4)
            embedMsg.add_field(name="Discord Invite Link", value=invitelinknew)
            embedMsg.set_footer(text="Discord server invited link.")
            await self.client.delete_message(ctx.message)
            await self.client.send_message(ctx.message.channel, embed=embedMsg)


    @commands.command(pass_context=True)
    async def google(self, ctx,*args):
        """Searches Google"""
        await self.client.delete_message(ctx.message)
        await self.client.say('https://encrypted.google.com/search?hl=en&q={}'.format(" ".join(args).replace(' ', '+')))

    @commands.command(pass_context = True)
    @commands.has_role('Staff')
    async def dm(self, ctx, member: discord.Member,*, message = ""):
        await self.client.send_message(member, '{}'.format(message))
        await self.client.say('***Message sent!***')
        await self.client.delete_message(ctx.message)


    @commands.command(pass_context = True)
    @commands.has_role('Staff')
    async def message(self, ctx, member: discord.Member,*, message = ""):
        await self.client.send_message(member, '{}'.format(message))
        await self.client.say('***Message sent!***')
        await self.client.delete_message(ctx.message)



    @commands.command(pass_context=True)
    @commands.has_role('Staff')
    async def avatar(self, ctx, user: discord.Member):
        embed = discord.Embed(title="Here's {}s avatar :".format(user.name), color=0xF35353)
        embed.set_image(url=user.avatar_url)
        await self.client.delete_message(ctx.message)
        await self.client.say(embed=embed)


    @commands.command(pass_context = True)
    async def id(self, ctx, user: discord.Member):
       embed = discord.Embed(name="Users ID!", description=" ", color=0xff00f6)
       embed.set_author(name="{}'s ID.".format(user.name))
       embed.add_field(name="There :slight_smile: ", value=user.id, inline=True)
       await self.client.say(embed=embed)



    @commands.command(pass_context=True)
    @commands.has_permissions(ban_members=True)
    @commands.has_role('Staff')
    async def ban(self, ctx, user: discord.Member = None):
        if user is None:
            await self.client.say('Please provied a user to ban!')
        else:
            embed=discord.Embed(title="User Banned!", description="**{0}** was banned by **{1}**!".format(user, ctx.message.author), color=0xff00f6)
            await self.client.say(embed=embed)
            await self.client.ban(user)





    @commands.command(pass_context = True)
    async def unban(self, ctx, user_id):
        banned = await self.client.get_user_info(user_id)
        embed=discord.Embed(title="User Unbanned!", description="**{0}** was unbanned by **{1}**!".format(banned, ctx.message.author), color=0xff00f6)
        await self.client.unban(ctx.message.server, banned)
        await self.client.say(embed=embed)


    @commands.command(name='kick', description="kicks people", brief="Kicks people.", aliases=['kick that guy\'s booty','delete'], pass_context=True)
    async def kick(self, ctx, user:discord.Member, *, reason:str=None):
        """Kicks someone from the server"""
        if reason is None:
            reason = "You have been banned by {ctx.message.author}. No reason was given."
        else:
            reason = "You have been banned by {ctx.message.author}. Reason:" + reason

        try:
            await self.client.kick(user)
        except discord.errors.Forbidden:
                await self.client.say("Permission denied. Check if you and I have sufficent permission to kick users.")
                return



        
    @commands.command(pass_context=True)
    async def mute(self, ctx, user: discord.Member, time=None, *, reason=None):
        if ctx.message.author.server_permissions.mute_members:
            MutedRole = discord.utils.get(ctx.message.server.roles, name='Muted')
            if reason == None:
                await self.client.say('**You need a reason to proceed this process.**')
            else:
                if time == None:
                await self.client.say('**You need a time to proceed this process.**')
            else:
                embed = discord.Embed(
                    colour = discord.Colour.purple()
                )
                embed.set_author(name='{} Has been muted'.format(user.name))
                embed.add_field(name='Reasoning', value='reason: {0}'.format(reason), inline=True)
                embed.add_field(name='Mute Time', value='Mute Time: {0}'.format(time), inline=True)
                await self.client.say(embed=embed)
                await self.client.add_roles(user, MutedRole)
                await asyncio sleep(time)
                await self.client.remove_roles(user, role)
        else:
            await self.client.say('**You do not have permission to use this command.** ``Mute Members Permission Required``')


    @commands.command(pass_context = True)
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, user: discord.Member=None):
        if not user:
            await self.client.say("Please provide user.")
        else:
            msg = "{} has been unmuted by {}".format (user.mention, ctx.message.author.mention)
            role = discord.utils.get(user.server.roles, name='Muted')
            await self.client.remove_roles(user, role)
            await self.client.say(msg)

    @commands.command(pass_context = True)
    @commands.has_role('Staff')
    async def echo(self, ctx, *, mg = None):
        await self.client.delete_message(ctx.message)

        if not mg: await self.client.say("Please specify a message to send")
        else: await self.client.say(mg)









def setup(client):
    client.add_cog(Moderations(client))
