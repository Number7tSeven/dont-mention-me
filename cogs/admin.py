import sys
import discord
from discord.ext import commands


class admin:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        '''Shuts the bot down :( (BOT OWNER ONLY)'''
        await ctx.send('Shuting down. :sleeping:')
        await self.bot.logout()

    @commands.command(hidden=True)
    @commands.is_owner()
    async def changestatus(self, ctx, status: str):
        '''Changes the online status of the Bot (BOT OWNER ONLY)'''
        status = status.lower()
        if status == 'offline' or status == 'off' or status == 'invisible':
            discordStatus = discord.Status.invisible
        elif status == 'idle':
            discordStatus = discord.Status.idle
        elif status == 'dnd' or status == 'disturb':
            discordStatus = discord.Status.dnd
        else:
            discordStatus = discord.Status.online
        await self.bot.change_presence(status=discordStatus)
        await ctx.send(f'Changed bot status to: **{discordStatus}**')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def echo(self, ctx, channel: str, *message: str):
        '''Returns a message as a bot on a particular channel (BOT OWNER ONLY)'''
        ch = self.bot.get_channel(int(channel))
        msg = ' '.join(message)
        await ch.send(msg)
        await ctx.message.delete()

    # @commands.command(hidden=True)
    # @commands.is_owner()
    # async def geninvite(self, ctx, serverid: str):
    #     '''Generate an Invite for a Guild if possible (BOT OWNER ONLY)'''
    #     guild = self.bot.get_guild(int(serverid))
    #     invite = await self.bot.create_invite(guild, max_uses=1, unique=False)
    #     msg = f'Invite für **{guild.name}** ({guild.id})\n{invite.url}'
    #     await ctx.author.send(msg)

    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def cog_load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.admin"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def cog_unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.admin"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def cog_reload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.admin"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')


def setup(bot):
    bot.add_cog(admin(bot))
