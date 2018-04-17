from discord.ext import commands


class math:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, *args):
        """Adds an arbitrary number of values
        Usage: {prefix}add 1 2 3 etc...
        """

        if len(args) == 0:
            await ctx.send('You didn\'t give any numbers.')
            return
        if len(args) == 1:
            await ctx.send('You only gave one number.')
            return

        try:
            await ctx.send(sum([float(x) for x in args]))
        except ValueError:
            await ctx.send('Invalid input. Please use numbers with spaces '
                           + 'between each.')
    
    @commands.command(aliases=['minus'])
    async def subtract(self, ctx, *args):
        """Subtracts and arbitrary number of values
        Usage: {prefix}subtract 1 2 3 etc...
        """

        if len(args) == 0:
            await ctx.send('You didn\'t give any numbers.')
            return
        if len(args) == 1:
            await ctx.send('You only gave one number.')
            return

        try:
            nums = [float(arg) for arg in args]
            await ctx.send(nums[0]-sum(nums[1:]))
        except ValueError:
            await ctx.send('Invalid input. Please use numbers with spaces '
                           + 'between each.')

    @commands.command(aliases=['prod'])
    async def multiply(self, ctx, *args):
        """Multiplies an arbitrary number of values
        Usage: {prefix}multiply 1 2 3 etc...
        """

        if len(args) == 0:
            await ctx.send('You didn\'t give any numbers.')
            return
        if len(args) == 1:
            await ctx.send('You only gave one number.')
            return
        
        try:
            nums = [float(arg) for arg in args]
            product = 1
            for num in nums:
                product *= num
            await ctx.send(product)
        except ValueError:
            await ctx.send('Invalid input. Please use numbers with spaces '
                           + 'between each.')

    @commands.command()
    async def divide(self, ctx, *args):
        """Divides an arbitrary number of values
        Usage: {prefix}multiply 1 2 3 etc...
        """

        if len(args) == 0:
            await ctx.send('You didn\'t give any numbers.')
            return
        if len(args) == 1:
            await ctx.send('You only gave one number.')
            return
        
        try:
            nums = [float(arg) for arg in args]
            quo = nums[0]
            for num in nums[1:]:
                quo /= num
            await ctx.send(quo)
        except ValueError:
            await ctx.send('Invalid input. Please use numbers with spaces '
                           + 'between each.')
        except ZeroDivisionError:
            await ctx.send(':expressionless: You want me to divide by zero? '
                           + 'Really?')


def setup(bot):
    bot.add_cog(math(bot))
