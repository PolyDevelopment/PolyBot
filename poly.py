import discord
import os
import asyncio

from discord.ext import commands
from datetime import datetime
from utils.constants import PolyConstants
from utils.utils import PolyContext

constants = PolyConstants()

class Poly(commands.AutoShardedBot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.token = None
        self.start_time = datetime.now()
        self.context = PolyContext

    async def get_context(self, message, *, cls=PolyContext):
        return await super().get_context(message, cls=cls)
    
    async def setup_hook(self) -> None:
        for root, _, files in os.walk("./cogs"):
            for file in files:
                if file.endswith(".py"):
                    cog_path = os.path.relpath(os.path.join(root, file), "./cogs")
                    cog_module = cog_path.replace(os.sep, ".")[:-3]

                    await poly.load_extension(f"cogs.{cog_module}")

        print("All cogs loaded successfully!")

        await self.tree.sync(guild=None)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

poly = Poly(
    command_prefix="-",
    intents=intents,
    cls=PolyContext,
)

def run():
    poly.run(constants.token_setup())

if __name__ == "__main__":
    run()