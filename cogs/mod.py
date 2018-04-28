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

    @commands.command(hidden=True)
    @commands.has_permissions(kick_members = True)
    @commands.bot_has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member = None, *reason):
        '''Kicks a member with a reason (MOD ONLY)
        Example:
        -----------
        :kick @user#000
        '''
        if member is not None:
            if reason:
                reason = ' '.join(reason)
            else:
                reason = None
            await member.kick(reason=reason)
        else:
            await ctx.send('No user specified!')

    @commands.command(hidden=True)
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member=None, *reason):
        '''Bans a member with a reason (MOD ONLY)
        Example:
        -----------
        :ban @user#0000
        '''
        if member is not None:
            if reason:
                reason = ' '.join(reason)
            else:
                reason = None
            await member.ban(reason=reason)
        else:
            await ctx.send('No user specified!')

    @commands.command(hidden=True)
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_permissions(ban_members = True)
    async def unban(self, ctx, user: int=None, *reason):
        '''Unbans a member with a reason (MOD ONLY)
         The user ID must be specified, name + discriminator is not enough
        Example:
        -----------
        :unban 102815825781596160
        '''
        user = discord.User(id=user)
        if user is not None:
            if reason:
                reason = ' '.join(reason)
            else:
                reason = None
            await ctx.guild.unban(user, reason=reason)
        else:
            await ctx.send('No user specified!')


def setup(bot):
    bot.add_cog(mod(bot))
