import os

import dotenv
from discord.ext import commands

dotenv.load_dotenv()


class GuppiBot(commands.Cog):
    prefix = '/'
    bot = commands.Bot(prefix)

    def __init__(self, token):
        self.token = token
        self.bot.run(self.token)


if __name__ == '__main__':
    bot = GuppiBot(os.getenv('TOKEN'))
