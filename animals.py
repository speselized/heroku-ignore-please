import discord
from discord.ext import commands

import json
from random import randint

import aiohttp
import asyncio
import async_timeout

class Animals():
    shib = ''
    def __init__(self, client):
        self.client = client




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


    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def cat(self, ctx):
        """ Posts a random cat """
        await self.client.randomimageapi(ctx, 'https://nekos.life/api/v2/img/meow', 'url')
        await self.client.delete_message(ctx.message)


    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def duck(self, ctx):
        """ Posts a random duck """
        await self.client.randomimageapi(ctx, 'https://random-d.uk/api/v1/random', 'url')
        await self.client.delete_message(ctx.message)


def setup(client):
    client.add_cog(Animals(client))
