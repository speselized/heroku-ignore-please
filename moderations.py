import discord
import os
import traceback
import sys
import re
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



time_regex = re.compile("(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h":3600, "s":1, "m":60, "d":86400}

class TimeConverter(commands.Converter):

    async def convert(self):

        args = self.argument.lower()

        matches = re.findall(time_regex, args)

        time = 0

        for v, k in matches:

            try:

                time += time_dict[k]*float(v)

            except KeyError:

                raise commands.BadArgument("{} is an invalid time-key! h/m/s/d are valid!".format(k))

            except ValueError:

                raise commands.BadArgument("{} is not a number!".format(v))

        return time

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
        
        
    @commands.command(name="whois", pass_context=True)
    async def user_info(self, ctx, user: discord.Member = None):
        """Gets information about the desired user (defaults to the message sender)"""
        if user is None:
            await self.client.say("```xl\n"
                               "User: {0}\n"
                               "Nickname: {0.nick}\n"
                               "ID: {0.id}\n"
                               "Avatar: {0.avatar_url}\n"
                               "Created At: {0.created_at}\n"
                               "Joined On: {0.joined_at}\n"
                               "Game: {0.game}\n"
                               "Roles: {1}\n"
                               "```".format(ctx.message.author, ", ".join([x.name for x in ctx.message.author.roles if x.name != "@everyone"])))
        else:
            await self.client.say("```xl\n"
                               "User: {0}\n"
                               "Nickname: {0.nick}\n"
                               "ID: {0.id}\n"
                               "Avatar: {0.avatar_url}\n"
                               "Created At: {0.created_at}\n"
                               "Joined On: {0.joined_at}\n"
                               "Game: {0.game}\n"
                               "Roles: {1}\n"
                               "```".format(user, ", ".join([x.name for x in user.roles if x.name != "@everyone"])))

    @commands.command(name="serverinfo", pass_context=True)
    async def server_info(self, ctx):
        """Gets information about the current server"""
        await self.client.say("```xl\n"
                           "Guild: {0}\n"
                           "ID: {0.id}\n"
                           "Region: {0.region}\n"
                           "Member Count: {1}\n"
                           "Owner: {0.owner}\n"
                           "Icon: {0.icon_url}\n"
                           "Roles: {2}"
                           "```".format(ctx.message.server, sum(1 for x in ctx.message.server.members),
                                        ", ".join([x.name for x in ctx.message.server.roles])))


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
    @commands.has_role('Staff')
    async def warn(self, ctx, user: discord.User, reason):
        msg = ctx.message.content.split(" ")
        msg2 = " ".join(msg[2:])
        await self.client.send_message(user, f"You have been warned in **{ctx.message.server.name}** by **{ctx.message.author.name}**. Reason: **{msg2}**")
        await self.client.say(f"{user.name} has been warned Reason: {msg2}")
        if ctx.message.server.id == "502034450692177921":
            channel = self.client.get_channel("502068770039136257")
            embed = discord.Embed(title="Warn", color=discord.Color.red())
            embed.add_field(name="User", value=user.mention)
            embed.add_field(name="Moderator", value=ctx.message.author.mention)
            embed.add_field(name="Reason", value=reason)
            embed.set_footer(text=self.client.user.name, icon_url=self.client.user.avatar_url)
            embed.set_thumbnail(url=user.avatar_url)
            await self.client.send_message(channel, embed=embed)
            
            
            
    @commands.command(pass_context=True)
    @commands.has_role('Staff')
    async def mute(self, ctx, user: discord.User, *, time:TimeConverter = None):
        if ctx.message.server.id == "502034450692177921":
            msg = ctx.message.content.split(" ")
            msg2 = " ".join(msg[2:])
            await self.client.send_message(user, f"You have been muted in **{ctx.message.server.name}** by **{ctx.message.author.name}**. Reason: **{msg2}**")
            await self.client.say(f"{user.name} has been muted for {time}s, Reason: {msg2}" if time else "Muted {user.name}. Reason: {msg2}")
            if time:
                await asyncio.sleep(time)
                await self.client.remove_roles(user, role)
                return
            else:
                channel = self.client.get_channel("502068770039136257")
                embed = discord.Embed(title="Mute", color=discord.Color.red())
                embed.add_field(name="User", value=user.mention)
                embed.add_field(name="Moderator", value=ctx.message.author.mention)
                embed.add_field(name="Reason", value=reason)
                embed.set_footer(text=self.client.user.name, icon_url=self.client.user.avatar_url)
                embed.set_thumbnail(url=user.avatar_url)
                role = discord.utils.get(ctx.message.server.roles, id="502057487252455424")
                await self.client.add_roles(user, role)
                overwrite = discord.PermissionOverwrite()
                overwrite.speak = False
                overwrite.send_messages = False
                for channel in ctx.message.server.channels:
                    await self.client.edit_channel_permissions(channel, role, overwrite)
                channel = self.client.get_channel("502068770039136257")
                await self.client.send_message(channel, embed=embed)
                
                

    @mute.error
    async def mute_error(self, error, ctx):
        if isinstance(error, commands.CheckFailure):
            pass
        if isinstance(error, commands.BadArgument):
            await self.client.send_message(ctx.message.channel, error)
        else:
            error = getattr(error, 'original', error)
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)               
                


    @commands.command(pass_context=True)
    @commands.has_role('Staff')
    async def unmute(self, ctx, user: discord.User, reason):
        if ctx.message.server.id == "502034450692177921":
            msg = ctx.message.content.split(" ")
            msg2 = " ".join(msg[2:])
            await self.client.send_message(user, f"You have been unmuted in **{ctx.message.server.name}** by **{ctx.message.author.name}**. Reason: **{msg2}**")
            await self.client.say(f"{user.name} has been unmuted Reason: {msg2}")
            channel = self.client.get_channel("502068770039136257")
            embed = discord.Embed(title="Unmute", color=discord.Color.red())
            embed.add_field(name="User", value=user.mention)
            embed.add_field(name="Moderator", value=ctx.message.author.mention)
            embed.add_field(name="Reason", value=reason)
            embed.set_footer(text=self.client.user.name, icon_url=self.client.user.avatar_url)
            embed.set_thumbnail(url=user.avatar_url)
            role = discord.utils.get(ctx.message.server.roles, id="502057487252455424")
            await self.client.remove_roles(user, role)
            overwrite = discord.PermissionOverwrite()
            overwrite.speak = False
            overwrite.send_messages = False
            for channel in ctx.message.server.channels:
                await self.client.edit_channel_permissions(channel, role, overwrite)
            channel = self.client.get_channel("502068770039136257")
            await self.client.send_message(channel, embed=embed)

    @commands.command(pass_context = True)
    @commands.has_role('Staff')
    async def echo(self, ctx, *, mg = None):
        await self.client.delete_message(ctx.message)

        if not mg: await self.client.say("Please specify a message to send")
        else: await self.client.say(mg)









def setup(client):
    client.add_cog(Moderations(client))
