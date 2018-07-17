import random
from discord.ext import commands


class Joke:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['Praise', 'praise!', 'Praise!'])
    async def praise(self, ctx,):
        """Praise the Sun!"""
        # if args.lower() == 'the sun' or 'the sun!':
        gifs = ['https://i.imgur.com/Qo8KipS.gif',
                'https://media.tenor.com/images/a5cd5616d867a576cdf257e1dd5430f'
                'b/tenor.gif',
                'https://media1.tenor.com/images/27b4d0102ce4f843a2a8c241cff421'
                'de/tenor.gif',
                'https://i.imgur.com/cxgWdSI.gif',
                'https://i.imgur.com/2Bz7bUE.gif']
        msg = f'Praise the Sun!\n{random.choice(gifs)}'
        await ctx.send(msg)

    @commands.command()
    async def potato(self, ctx,):
        """PO-TAY-TOES! Boil 'em, mash 'em, stick 'em in a stew!"""
        gifs = ['https://media0.giphy.com/media/U1rlk8zdcAwbm/giphy.gif',
                'https://media.giphy.com/media/ccedUarzoWBuo/giphy.gif',
                'https://media.giphy.com/media/bPShx901m0HHG/giphy.gif',
                'https://media1.tenor.com/images/8252b26bea33c12da5a28605176493'
                'a4/tenor.gif?itemid=7672866',
                'https://78.media.tumblr.com/tumblr_m81s2eZTp51r04hw7o1_500.gif'
                ]
        msg = random.choice(gifs)
        await ctx.send(msg)


def setup(bot):
    bot.add_cog(Joke(bot))
