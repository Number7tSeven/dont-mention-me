import random
from discord.ext import commands


class rng:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, dice: str):
        """Rolls a dice in NdN format."""

        if dice == 'initiative' or 'Initiative':
            dice = '1d20'

        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @commands.command()
    async def coinflip(self, ctx):
        """Flips a coin"""
        
        result = random.randint(1, 2)

        if result == 1:
            await ctx.send('Heads!')
        elif result == 2:
            await ctx.send('Tails!')


def setup(bot):
    bot.add_cog(rng(bot))
