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


    @commands.command(pass_context=True)
    async def cat(self, ctx):
        """Grabs a random cat picture"""
        for i in range(0,5):
            # site is buggy and sometimes gives bad images
            # just loop until we get a good one
            try:
                r = requests.get("https://aws.random.cat/meow")
                r = str(r.content)
                r = r.replace("b'","")
                r = r.replace("'","")
                r = r.replace("\\","")
                url = json.loads(r)["file"]
                await self.client.say(url)
                break
            except:
                pass


def setup(client):
    client.add_cog(Animals(client))
