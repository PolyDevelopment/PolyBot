import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

class PolyContext(commands.Context):
    @property
    def poly(self):
        return self.bot