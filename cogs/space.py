import json
import requests
from discord.ext import commands


class space:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def iss(self, ctx):
        """Responds with the location of the ISS."""

        loc_response = requests.get("http://api.open-notify.org/iss-now.json")
        loc_data = loc_response.json()
        
        with open("Nation_data.json") as json_data:
            nat_data = json.load(json_data)
        
        lat = loc_data['iss_position']['latitude']
        long = loc_data['iss_position']['longitude']

        with open("map_quest_key.txt") as mapfile:
            mapquest_key = mapfile.read()

        map_string = ("https://www.mapquestapi.com/geocoding/v1/reverse?key={}"
                      + "&location={}%2C{}&outFormat=json" + "&thumbMaps=false"
                      ).format(mapquest_key, str(lat), str(long))
        map_response = requests.get(map_string)
        map_data = map_response.json()

        nat_dict = {}
        for entry in nat_data:
            nat_dict[entry['Code']] = entry['Name']

        loc = nat_dict[map_data["results"][0]["locations"][0]["adminArea1"]]

        await ctx.send("The current location of the International Space Station"
                       + " is `%s°N %s°W`, which is above `%s`." % (lat, long, loc))

    @commands.command()
    async def astronauts(self, ctx):
        """Responds with the number of astronauts in space."""

        astro_response = requests.get("http://api.open-notify.org/astros.json")
        astro_data = astro_response.json()

        astro_list = [astro["name"] for astro in astro_data["people"]]
        astro_num = astro_data["number"]

        if astro_num > 1:
            astro_string = "Their names are %s"
            for _ in range(astro_num-2):
                astro_string = astro_string + ", %s"
            astro_string = astro_string + ", and %s."

        elif astro_num == 1:
            astro_string = "His/her name is %s."

        elif astro_num == 0:
            astro_string = "There are no astronauts in space. %s"
        
        await ctx.send("There are %s astronauts currently in space." % astro_num 
                       + "\n" + astro_string % tuple(astro_list))


def setup(bot):
    bot.add_cog(space(bot))
