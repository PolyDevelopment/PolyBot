import discord
import platform
from datetime import datetime
from discord.ext import commands
from utils.constants import PolyConstants
from typing import List

constants = PolyConstants()

class PingCommandEmbed:
    @staticmethod
    def create_ping_embed(
        latency: float,
        uptime,
        current_shard_id: int,
        total_shards: int,
        shard_info: List[dict],
    ):
        embed = discord.Embed(
            title="Poly Status",
            timestamp=datetime.now(),
        )

        embed.add_field(
            name="Information",
            value=(
                f"> **Latency:** `{round(latency * 1000)}ms` \n"
                f"> **Uptime:** <t:{int(uptime.timestamp())}:R>\n"
                f"> **Python Version:** `{platform.python_version()}` \n"
                f"> **Discord.py Version:** `{discord.__version__}` \n"
            ),
            inline=False,
        )

        embed.set_footer(
            text=f"Shard {current_shard_id + 1}/{total_shards}"
        )
        
        return embed