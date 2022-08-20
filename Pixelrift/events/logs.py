import discord
from discord.ext import commands, tasks


class logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channelId = 992875838792011909
        channel = await self.bot.fetch_channel(channelId)
        await channel.send(f"{member} has joined the server!")


async def setup(bot):
    await bot.add_cog(logs(bot))