# Third party libraries
import discord
from discord.ext import commands


class Info:

    """Info is a class within Pixie that is only for accessing data from discords built in things (Although we add Pixie's status command here)"""

    def __init__(self, client):
        self.client = client

    @commands.command(name="userinfo", pass_context=True)
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
    async def guild_info(self, ctx):
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

    @commands.command(name="infostatus")
    async def status(self):
        """Gives some general information about Pixie's current situation"""
        await self.client.say("```xl\n"
                           "I'm in {0} servers\n"
                           "I can currently see {1} people, {2} of which are unique\n"
                           "I'm also in {3} voice channels"
                           "```".format(len(self.client.servers),
                                        sum(1 for x in self.client.get_all_members()),
                                        len(set(self.client.get_all_members())),
                                        len(self.client.voice_clients)))



def setup(client):
    client.add_cog(Info(client))
