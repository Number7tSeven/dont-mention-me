*NOTE: Much of this code was taken from [Der-Eddy's discord bot](https://github.com/Der-Eddy/discord_bot) and modified. You should check it out.*

![picture](https://raw.githubusercontent.com/Number7tSeven/dont-mention-me/master/pic/strike%401.png)

# Don't Mention Me
A simple Discord bot that responds negatively to being mentioned.

## Commands
Commands can be invoked using one of the following prefixes at the beginning of a discord message. *(NOTE: The space at the end of the prefix must be used.)*
* "!Don't Mention Me "
* "!don't mention me "
* "!Don't Mention "
* "!don't mention "
* "!Mention "
* "!mention "

### General commands

Command Name | Description
-| -
hello | Responds with a simple greeting.
praise | Praise the sun!
potato | Posts potato related gifs.
add | Adds two numbers.
subtract | Subtracts two numbers.
multiply | Multiplies two numbers.
divide | Divides two numbers.
roll | Roll a dice. Imput must match "NdN" format.
coinflip | Flips a coin.

### Mod Commands
Commands for server moderators only. These commands are hidden from the help dialogue and can only be invoked by users with the appropriate permissions.

Command Name | Description
-| -
nickname |  Changes the nickname of the bot on the server.
setrank | Sets a rank/role of a member of the server.
rmrank | Removes a rank/role from a member of the server.
kick | Kicks a server member from the server.
ban | Bans a member.
unban| Un-bans a member.

### Admin Commands
Commands for the bot owner only. These commands are hidden from the help dialogue and can only be invoked by the owner of the Discord bot.

Command Name | Description
-| -
shutdown |  Shuts down the bot.
changestatus | changes the status of the bot.
echo | Echos a message in another channel
cog_load | Loads a cog.
cog_unload | Unloads a cog.
cog_reload | Unloads and then reloads a cog.