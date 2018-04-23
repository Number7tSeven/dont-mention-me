import discord
from discord.ext import commands
import random

__version__ = '0.0.0'


def get_prefix(bot, message):
    """A callable prefix."""

    prefixes = ['!Don\'t Mention Me ', '!don\'t mention me ', '!Don\'t Mention ', '!don\'t mention ', "!Mention ",
                "!mention "]

    return prefixes


description = ("a template Discord bot to be used with the rewrite version of "
               + "discord.py")

bot = commands.Bot(command_prefix=get_prefix, description=description)

cogs = ['rng', 'math', 'mod', 'joke', 'admin']

if __name__ == '__main__':
    for cog in cogs:
        try:
            bot.load_extension('cogs.' + cog)
        except (discord.ClientException, ModuleNotFoundError):
            print(f'Couldn\'t load cog {cog}')


@bot.event
async def on_ready():
    
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}')
    print(f'Version: {__version__}')
    print(f'Discord.py Version: {discord.__version__}\n')
    print('I live!\n')


@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message) and message.mention_everyone is False:
        responses = ('What the fuck did you just fucking say about me, you little '
                     + 'bitch? I’ll have you know I graduated top of my class in '
                     + 'the Navy Seals, and I’ve been involved in numerous secret '
                     + 'raids on Al-Quaeda, and I have over 300 confirmed kills. I '
                     + 'am trained in gorilla warfare and I’m the top sniper in '
                     + 'the entire US armed forces. You are nothing to me but just '
                     + 'another target. I will wipe you the fuck out with '
                     + 'precision the likes of which has never been seen before on '
                     + 'this Earth, mark my fucking words. You think you can get '
                     + 'away with saying that shit to me over the Internet? Think '
                     + 'again, fucker. As we speak I am contacting my secret '
                     + 'network of spies across the USA and your IP is being '
                     + 'traced right now so you better prepare for the storm, '
                     + 'maggot. The storm that wipes out the pathetic little thing '
                     + 'you call your life. You’re fucking dead, kid. I can be '
                     + 'anywhere, anytime, and I can kill you in over seven '
                     + 'hundred ways, and that’s just with my bare hands. Not only '
                     + 'am I extensively trained in unarmed combat, but I have '
                     + 'access to the entire arsenal of the United States Marine '
                     + 'Corps and I will use it to its full extent to wipe your '
                     + 'miserable ass off the face of the continent, you little '
                     + 'shit. If only you could have known what unholy retribution '
                     + 'your little “clever” comment was about to bring down upon '
                     + 'you, maybe you would have held your fucking tongue. But '
                     + 'you couldn’t, you didn’t, and now you’re paying the price, '
                     + 'you goddamn idiot. I will shit fury all over you and you '
                     + 'will drown in it. You’re fucking dead, kiddo.',
                     "Can you even read?",
                     "Dude. Stop.",
                     "Haha. Real funny. :angry:",
                     "Go away!",
                     ":rage:")
        await message.channel.send(random.choice(responses))

    if bot.user.mentioned_in(message) and message.mention_everyone is True:
        await message.channel.send('https://youtu.be/D1VqrwEyL5k')

    await bot.process_commands(message)


with open('key.txt') as keyfile:
    key = keyfile.read()

bot.run(key)
