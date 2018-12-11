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
    @commands.has_role('The Queen')
    async def reactrole(self, ctx):
        channel = self.client.get_channel('521937059212951552')
        role = discord.utils.get(user.server.roles, name="NSFW")
        message = await self.client.send_message(channel, "React with the :thumbsup: to get access to NSFW content! <#521926119155302427>")
        reaction, reactor = await self.client.wait_for_reaction(emoji="👍", message=message)
        await self.client.add_roles(reactor, role)
    
    
    @commands.command(pass_context=True)
    @commands.has_role('The Queen')
    async def nsfw(self, ctx):
        role = discord.utils.get(ctx.message.server.roles, name="NSFW")
        await self.client.say('you has been permitted to access NSFW content! <#521926119155302427>')
        await self.client.add_roles(member, role)


        
        
    @commands.command(name="whois", pass_context=True)
    @commands.has_role('Staff')
    async def user_info(self, ctx, user: discord.Member = None):
        """Gets information about the desired user (defaults to the message sender) (STAFF ONLY)"""
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
    @commands.has_role('Staff')
    async def server_info(self, ctx):
        """Gets information about the current server"""
        await self.client.say("```xl\n"
                           "Server: {0}\n"
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


    async def bans(self, ctx):
        """Shows how many bans are in the server. (STAFF ONLY)"""
        ban_list = await self.client.get_bans(ctx.message.server)

        # Show banned users
        await self.client.say("Ban list:\n{}".format("\n".join([user.name for user in ban_list])))

        # Unban last banned user
        if not ban_list:

            await self.client.say('Ban list is empty.')
            return







    @commands.command(pass_context=True)
    async def invite(self, ctx):
        """Makes an invite for the server. Max uses is 100."""
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
        """Direct messages the user you pinged. (STAFF ONLY)"""
        
        await self.client.send_message(member, '{}'.format(message))
        await self.client.say('***Message sent!***')
        await self.client.delete_message(ctx.message)


    @commands.command(pass_context = True)
    @commands.has_role('Staff')
    async def message(self, ctx, member: discord.Member,*, message = ""):
        """The bot direct messages the user you provided in the string. (STAFF ONLY)"""
        await self.client.send_message(member, '{}'.format(message))
        await self.client.say('***Message sent!***')
        await self.client.delete_message(ctx.message)

        
    @commands.command(pass_context = True)
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        """Clear amount of messages you entered in the string"""
        deleted = await self.channel.purge(limit=amount)
        embed=discord.Embed(color=0xffffff)
        embed.add_field(name="✅ Success", value=f"Cleared {amount} Messages!", inline=False)
        await self.client.say(embed=embed)
        
        
    @commands.command(pass_context = True)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        """Clear amount of messages you entered in the string"""
        deleted = await self.channel.purge(limit=amount)
        embed=discord.Embed(color=0xffffff)
        embed.add_field(name="✅ Success", value=f"Cleared {amount} Messages!", inline=False)
        await self.client.say(embed=embed)


    @commands.command(pass_context=True)
    async def avatar(self, ctx, user: discord.Member):
        """Gets the users avatar you provided in the string. (STAFF ONLY)"""
        embed = discord.Embed(title="Here's {}s avatar :".format(user.name), color=0xF35353)
        embed.set_image(url=user.avatar_url)
        await self.client.delete_message(ctx.message)
        await self.client.say(embed=embed)


    @commands.command(pass_context = True)
    @commands.has_role('Staff')
    async def id(self, ctx, user: discord.Member):
        """Gets their id. (STAFF ONLY)"""
        embed = discord.Embed(name="Users ID!", description=" ", color=0xff00f6)
        embed.set_author(name="{}'s ID.".format(user.name))
        embed.add_field(name="There :slight_smile: ", value=user.id, inline=True)
        await self.client.say(embed=embed)



    @commands.command(pass_context=True)
    @commands.has_permissions(ban_members=True)
    @commands.has_role('Staff')
    async def ban(self, ctx, user: discord.Member, reason):
        """BAN THE NAUGHTY KIDS. (STAFF ONLY)"""
        msg = ctx.message.content.split(" ")
        msg2 = " ".join(msg[2:])
        await self.client.ban(user)
        await self.client.send_message(user, f"You have been banned in **{ctx.message.server.name}** by **{ctx.message.author.name}**. Reason: **{msg2}**")
        await self.client.say(f"{user.name} has been banned Reason: {msg2}")
        if ctx.message.server.id == "511148640710950933" or ctx.message.server.id == "516944111010578443":
            channel = discord.utils.get(client.get_all_channels(), name='logs')
            embed = discord.Embed(title="Ban", color=discord.Color.red())
            embed.add_field(name="User", value=user.mention)
            embed.add_field(name="Moderator", value=ctx.message.author.mention)
            embed.add_field(name="Reason", value=msg2)
            embed.set_footer(text=self.client.user.name, icon_url=self.client.user.avatar_url)
            await self.client.send_message(channel, embed=embed)





    @commands.command(pass_context = True)
    @commands.has_permissions(ban_members=True)
    @commands.has_role('Staff')
    async def unban(self, ctx, user_id, reason):
        """Unbans the nice and beautiful kids. (STAFF ONLY)"""
        banned = await self.client.get_user_info(user_id)
        msg = ctx.message.content.split(" ")
        msg2 = " ".join(msg[2:])
        await self.client.unban(ctx.message.server, banned)
        await self.client.say(f"User Unbanned. Reason: {msg2}")
        if ctx.message.server.id == "511148640710950933" or ctx.message.server.id == "516944111010578443":
            channel = discord.utils.get(client.get_all_channels(), name='logs')
            embed = discord.Embed(title="Unban", color=discord.Color.red())
            embed.add_field(name="Moderator", value=ctx.message.author.mention)
            embed.add_field(name="Reason", value=msg2)
            await self.client.send_message(channel, embed=embed)


    @commands.command(pass_context=True)
    @commands.has_role('Staff')
    async def kick(self, ctx, user:discord.Member, reason):
        """Kicks someone from the server (STAFF ONLY)"""
        msg = ctx.message.content.split(" ")
        msg2 = " ".join(msg[2:])
        await self.client.kick(user)
        await self.client.send_message(user, f"You have been kicked in **{ctx.message.server.name}** by **{ctx.message.author.name}**. Reason: **{msg2}**")
        await self.client.say(f"{user.name} has been kicked Reason: {msg2}")
        if ctx.message.server.id == "511148640710950933" or ctx.message.server.id == "516944111010578443":
            channel = discord.utils.get(client.get_all_channels(), name='logs')
            embed = discord.Embed(title="Kick", color=discord.Color.red())
            embed.add_field(name="User", value=user.mention)
            embed.add_field(name="Moderator", value=ctx.message.author.mention)
            embed.add_field(name="Reason", value=reason)
            embed.set_footer(text=self.client.user.name, icon_url=self.client.user.avatar_url)
            embed.set_thumbnail(url=user.avatar_url)
            await self.client.send_message(channel, embed=embed)



        
    @commands.command(pass_context=True)
    @commands.has_role('Staff')
    async def warn(self, ctx, user: discord.User, reason):
        """Warns the user. (STAFF ONLY)"""
        msg = ctx.message.content.split(" ")
        msg2 = " ".join(msg[2:])
        await self.client.send_message(user, f"You have been warned in **{ctx.message.server.name}** by **{ctx.message.author.name}**. Reason: **{msg2}**")
        await self.client.say(f"{user.name} has been warned Reason: {msg2}")
        if ctx.message.server.id == "511148640710950933" or ctx.message.server.id == "516944111010578443":
            channel = discord.utils.get(client.get_all_channels(), name='logs')
            embed = discord.Embed(title="Warn", color=discord.Color.red())
            embed.add_field(name="User", value=user.mention)
            embed.add_field(name="Moderator", value=ctx.message.author.mention)
            embed.add_field(name="Reason", value=reason)
            embed.set_footer(text=self.client.user.name, icon_url=self.client.user.avatar_url)
            embed.set_thumbnail(url=user.avatar_url)
            await self.client.send_message(channel, embed=embed)
            
            
            
               
                    
                    
                    
                    
                    
    @commands.command(pass_context=True)
    @commands.has_role('Staff')
    async def mute(self, ctx, member:discord.Member, time:TimeConverter = None, *, reason:str):
        """Mutes the user. Requires time and reason! (STAFF ONLY)"""
        if ctx.message.server.id == "511148640710950933" or ctx.message.server.id == "516944111010578443":
            role = discord.utils.get(ctx.message.server.roles, name="Muted")
            await self.client.add_roles(member, role)
            await self.client.say(f"{member.name} has been Muted Reason: {reason} For {time}s")
            await self.client.send_message(member, f"You have been Muted in **{ctx.message.server.name}** by **{ctx.message.author.name}**. Reason: **{reason}** For {time}s.")
            bembed = discord.Embed(title="User Muted.", color=16202876)
            bembed.add_field(name="User:", value=str(member), inline=False)
            bembed.add_field(name="Moderator:", value=str(ctx.message.author), inline=False)
            bembed.add_field(name="Reason:", value=str(reason), inline=False)
            bembed.add_field(name="Lasts for:", value=str(time), inline=False)
            bembed.set_footer(text=self.client.user.name, icon_url=self.client.user.avatar_url)
            bembed.set_thumbnail(url=member.avatar_url)
            bchannel = discord.utils.get(client.get_all_channels(), name='logs')
            await self.client.send_message(bchannel, embed=bembed)
            if time:
                await asyncio.sleep(time)
                await self.client.remove_roles(member, role)
                    
                


    @commands.command(pass_context=True)
    @commands.has_role('Staff')
    async def unmute(self, ctx, user: discord.User, reason):
        """Unmutes the naughty bad child. (STAFF ONLY)"""
        if ctx.message.server.id == "511148640710950933" or ctx.message.server.id == "516944111010578443":
            msg = ctx.message.content.split(" ")
            msg2 = " ".join(msg[2:])
            await self.client.send_message(user, f"You have been unmuted in **{ctx.message.server.name}** by **{ctx.message.author.name}**. Reason: **{msg2}**")
            await self.client.say(f"{user.name} has been unmuted Reason: {msg2}")
            embed = discord.Embed(title="Unmute", color=discord.Color.red())
            embed.add_field(name="User", value=user.mention)
            embed.add_field(name="Moderator", value=ctx.message.author.mention)
            embed.add_field(name="Reason", value=msg2)
            embed.set_footer(text=self.client.user.name, icon_url=self.client.user.avatar_url)
            embed.set_thumbnail(url=user.avatar_url)
            role = discord.utils.get(ctx.message.server.roles, name="Muted")
            await self.client.remove_roles(user, role)
            overwrite = discord.PermissionOverwrite()
            overwrite.speak = False
            overwrite.send_messages = False
            for channel in ctx.message.server.channels:
                await self.client.edit_channel_permissions(channel, role, overwrite)
            channel = discord.utils.get(client.get_all_channels(), name='logs')
            await self.client.send_message(channel, embed=embed)

    @commands.command(pass_context=True)
    @commands.has_role('Staff')
    async def say(self, ctx, *, message):
        """Makes the bot say something magical (STAFF ONLY)"""
        if '@everyone' in message: # Checking to make sure the user isn't trying to ping everyone or here
            await self.client.say('Nice try.')
            await self.client.delete_message(ctx.message)
            return
        elif '@here' in message:
            await self.client.say('Nice try.')
            await self.client.delete_message(ctx.message)
            return
        else:
            await self.client.send_message(ctx.message.channel, message)
            await self.client.delete_message(ctx.message)
            
            
            
            
    @commands.command(pass_context=True)
    @commands.has_role('Staff')
    async def echo(self, ctx, *, message):
        """Makes the bot say something magical (STAFF ONLY)"""
        if '@everyone' in message: # Checking to make sure the user isn't trying to ping everyone or here
            await self.client.say('Nice try.')
            await self.client.delete_message(ctx.message)
            return
        elif '@here' in message:
            await self.client.say('Nice try.')
            await self.client.delete_message(ctx.message)
            return
        else:
            await self.client.send_message(ctx.message.channel, message)
            await self.client.delete_message(ctx.message)









def setup(client):
    client.add_cog(Moderations(client))
