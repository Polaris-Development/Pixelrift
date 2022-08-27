import discord
from discord.ext import commands, tasks
from discord import Embed


class reactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guildid = 992875838116737165
        self.channelid = 1011665754569056392

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        print(payload)
        guild = await self.bot.fetch_guild(payload.guild_id)
        channel = await self.bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = await self.bot.fetch_user(payload.user_id)
        emoji = payload.emoji

        if user.id != 942067188611829780:
                roleid = self.bot.data3[str(message.id)][emoji.name]["role"]
                role = guild.get_role(roleid)
                await payload.member.add_roles(role)


async def setup(bot):
    await bot.add_cog(reactions(bot))