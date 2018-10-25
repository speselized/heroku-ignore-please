import discord
from discord.ext import commands

class Members():
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def joined(self, member : discord.Member):
        """Says when a member joined."""
        await self.client.say('{0.name} joined in {0.joined_at}'.format(member))

    @commands.group(pass_context=True)
    async def cool(self, ctx):
        """Says if a user is cool.
        In reality this just checks if a subcommand is being invoked.
        """
        if ctx.invoked_subcommand is None:
            await self.client.say('No, {0.subcommand_passed} is not cool'.format(ctx))



def setup(client):
    client.add_cog(Members(client))
