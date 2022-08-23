import discord
from discord.ext import commands, tasks


class stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.servermembers.start()

    @tasks.loop(seconds=300)
    async def servermembers(self):
        channelid = 992875838792011910
        serverid =992875838116737165

        await self.bot.wait_until_ready()
        vc = await self.bot.fetch_channel(channelid)

        guild = self.bot.get_guild(serverid)
        servermembers = len(guild.members)

        rename = f"Server Members: {servermembers}"
        await vc.edit(name=rename)
        print("Server members changed")


async def setup(bot):
    await bot.add_cog(stats(bot))