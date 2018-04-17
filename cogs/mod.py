import discord
from discord.ext import commands

class mod:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.has_permissions(manage_nicknames = True)
    @commands.bot_has_permissions(manage_nicknames = True)
    async def nickname(self, ctx, *name):
        '''Changes the Server Nickname for the Bot (MOD ONLY)'''
        nickname = ' '.join(name)
        await ctx.me.edit(nick=nickname)
        if nickname:
            msg = f'Changed my nickname to: **{nickname}**'
        else:
            msg = f'Reset my nickname to: **{ctx.me.name}**'
        await ctx.send(msg)

    @commands.command(hidden=True, aliases=['setrole', 'sr'])
    @commands.has_permissions(manage_roles = True)
    @commands.bot_has_permissions(manage_roles = True)
    async def setrank(self, ctx, member: discord.Member=None, *rankName: str):
        '''Gives a rank to a user
        Example:
        -----------
        :setrole @user#0000 Rank
        '''
        rank = discord.utils.get(ctx.guild.roles, name=' '.join(rankName))
        if member is not None:
            await member.add_roles(rank)
            await ctx.send(f'Roll **{rank.name}** was assigned to **{member.name}**')
        else:
            await ctx.send('No user specified!')

    @commands.command(pass_context=True, hidden=True, aliases=['rmrole', 'removerole', 'removerank'])
    @commands.has_permissions(manage_roles = True)
    @commands.bot_has_permissions(manage_roles = True)
    async def rmrank(self, ctx, member: discord.Member=None, *rankName: str):
        '''Removes a rank from a user
        Example:
        -----------
        :removerole @user#0000 Rank
        '''
        rank = discord.utils.get(ctx.guild.roles, name=' '.join(rankName))
        if member is not None:
            await member.remove_roles(rank)
            await ctx.send(f'Roll **{rank.name}** was removed from **{member.name}**')
        else:
            await ctx.send('No user specified!')

def setup(bot):
    bot.add_cog(mod(bot))
