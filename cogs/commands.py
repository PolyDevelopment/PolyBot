import os
import discord
import time
import datetime

from dotenv import load_dotenv
from datetime import datetime
from discord import Interaction, Embed
from discord.ext import commands
from utils.constants import PolyConstants
from utils.utils import PolyContext

from utils.embeds import PingCommandEmbed

constants = PolyConstants()

class CommandsCog(commands.Cog):
    def __init__(self, poly):
        self.poly = poly

    @commands.hybrid_command(
        name="ping",
        description="Check the bot's latency, uptime and shard info.",
        with_app_command=True,
    )
    async def ping(self, ctx: PolyContext):
        latency = self.poly.latency
        uptime = self.poly.start_time

        current_shard_id = ctx.guild.shard_id if ctx.guild else 0
        total_shards = self.poly.shard_count or 1

        shard_info = []
        for shard_id, shard in self.poly.shards.items():
            shard_info.append(
                {
                    "id": shard_id,
                    "latency": round(shard.latency * 1000),
                    "guilds": len([g for g in self.poly.guilds if g.shard_id == shard_id]),
                }
            )

        embed = PingCommandEmbed.create_ping_embed(
            latency=latency,
            uptime=uptime,
            current_shard_id=current_shard_id,
            total_shards=total_shards,
            shard_info=shard_info,
        )

        await ctx.reply(embed=embed, mention_author=False)


async def setup(poly):
    await poly.add_cog(CommandsCog(poly))