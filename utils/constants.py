import os
import discord
from dotenv import load_dotenv

load_dotenv()

class PolyConstants:
    def __init__(self):
        self.nothing = None

    def token_setup(self):
        token: str = os.getenv("DISCORD_TOKEN")
        if not isinstance(token, str):
            raise TypeError(
                f"expected token to be a str, received {type(token).__name__} instead"
            )
        return token