# Standard Library
import inspect
import io
import utils
import traceback
from contextlib import redirect_stdout

import discord
from discord.ext import commands
from utils import is_owner


class Owner:
    """A set of commands only for the owner of the bot"""

    def __init__(self, client):
        self.client = client
        self.sessions = set()

    @commands.check(is_owner)
    @commands.command(pass_context=True, name="announcement")
    async def announcement(self, ctx, message: str):
        for x in ctx.client.servers:
            await self.client.send_message(x.default_channel, message)

    @commands.check(is_owner)
    @commands.command(name="namechange")
    async def name_change(self, *, name: str):
        """Lets the bot owner change the name of the bot"""
        await self.client.edit_profile(username=name)
        await self.client.say("```Bot name has been changed to: {}```".format(name))




    @commands.check(is_owner)
    @commands.command(pass_context=True, hidden=True)
    async def debug(self, ctx, *, code: str):
        """Lets the bot owner evaluate code."""
        code = code.strip('` ')
        python = '```py\n{}\n```'
        result = None

        env = {
            'bot': self.client,
            'ctx': ctx,
            'message': ctx.message,
            'server': ctx.message.server,
            'channel': ctx.message.channel,
            'author': ctx.message.author
        }

        env.update(globals())

        try:
            result = eval(code, env)
            if inspect.isawaitable(result):
                result = await result
        except Exception as e:
            await self.client.say(python.format(type(e).__name__ + ': ' + str(e)))
            return

        await self.client.say(python.format(result))

    def cleanup_code(self, content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')

    def get_syntax_error(self, e):
        return '```py\n{0.text}{1:>{0.offset}}\n{2}: {0}```'.format(e, '^', type(e).__name__)

    @commands.check(is_owner)
    @commands.command(pass_context=True, hidden=True)
    async def repl(self, ctx):
        msg = ctx.message

        variables = {
            'ctx': ctx,
            'bot': self.client,
            'message': msg,
            'server': msg.server,
            'channel': msg.channel,
            'author': msg.author,
            'last': None,
        }

        if msg.channel.id in self.sessions:
            await self.client.say('Already running a REPL session in this channel. Exit it with `quit`.')
            return

        self.sessions.add(msg.channel.id)
        await self.client.say('Enter code to execute or evaluate. `exit()` or `quit` to exit.')
        while True:
            response = await self.client.wait_for_message(author=msg.author, channel=msg.channel,
                                                       check=lambda m: m.content.startswith('`'))

            cleaned = self.cleanup_code(response.content)

            if cleaned in ('quit', 'exit', 'exit()'):
                await self.client.say('Exiting.')
                self.sessions.remove(msg.channel.id)
                return

            executor = exec
            if cleaned.count('\n') == 0:
                # single statement, potentially 'eval'
                try:
                    code = compile(cleaned, '<repl session>', 'eval')
                except SyntaxError:
                    pass
                else:
                    executor = eval

            if executor is exec:
                try:
                    code = compile(cleaned, '<repl session>', 'exec')
                except SyntaxError as e:
                    await self.client.say(self.get_syntax_error(e))
                    continue

            variables['message'] = response

            fmt = None
            stdout = io.StringIO()

            try:
                with redirect_stdout(stdout):
                    result = executor(code, variables)
                    if inspect.isawaitable(result):
                        result = await result
            except Exception as e:
                value = stdout.getvalue()
                fmt = '```py\n{}{}\n```'.format(value, traceback.format_exc())
            else:
                value = stdout.getvalue()
                if result is not None:
                    fmt = '```py\n{}{}\n```'.format(value, result)
                    variables['last'] = result
                elif value:
                    fmt = '```py\n{}\n```'.format(value)

            try:
                if fmt is not None:
                    if len(fmt) > 2000:
                        await self.client.send_message(msg.channel, 'Content too big to be printed.')
                    else:
                        await self.client.send_message(msg.channel, fmt)
            except discord.Forbidden:
                pass
            except discord.HTTPException as e:
                await self.client.send_message(msg.channel, 'Unexpected error: `{}`'.format(e))


def setup(client):
    client.add_cog(Owner(client))
