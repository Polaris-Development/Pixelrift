import discord
from discord.ext import commands, tasks
from discord import Embed


class logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guildid = 992875838116737165
        self.channelid = 1011665754569056392

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channelId = 992875838792011909
        channel = await self.bot.fetch_channel(channelId)
        await channel.send(f"{member} has joined the server!")

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        guild = self.bot.get_guild(self.guildid)
        channel = guild.get_channel(self.channelid)

        deleted = Embed(description=f"Message deleted in {message.channel.mention}", color=0x4040EC).set_author(name=message.author, icon_url=message.author.avatar)

        deleted.add_field(name="Message", value=message.content)
        deleted.timestamp = message.created_at
        await channel.send(embed=deleted)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        guild = self.bot.get_guild(self.guildid)
        channel = guild.get_channel(self.channelid)

        deleted = Embed(
            description=f"Message edited in {before.channel.mention}", color=0x4040EC).set_author(name=before.author, icon_url=before.author.avatar)

        deleted.add_field(name="Before", value=before.content)
        deleted.add_field(name="After", value=after.content)
        deleted.timestamp = after.created_at
        await channel.send(embed=deleted)

    @commands.Cog.listener()
    async def on_bulk_message_delete(self, messages):
        guild = self.bot.get_guild(self.guildid)
        channel = guild.get_channel(self.channelid)

        deleted = Embed(
            description=f"Bulk messages deleted {messages[1].channel.mention}", color=0x4040EC).set_author(name=messages.author, icon_url=messages.author.avatar)

        deleted.add_field(name="Message", value=messages[1].content)
        deleted.timestamp = messages.created_at
        await channel.send(embed=deleted)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = self.bot.get_guild(self.guildid)
        channel = guild.get_channel(self.channelid)

        deleted = Embed(description=f"Member joined the server!", color=0x4040EC).set_author(name=str(member))
        await channel.send(embed=deleted)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = self.bot.get_guild(self.guildid)
        channel = guild.get_channel(self.channelid)

        deleted = Embed(description=f"Member left the server.", color=0x4040EC).set_author(name=str(member))
        await channel.send(embed=deleted)

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        guild = self.bot.get_guild(self.guildid)
        channel = guild.get_channel(self.channelid)

        deleted = Embed(description=f"Member was banned from the server.", color=0x4040EC).set_author(name=str(user))
        await channel.send(embed=deleted)

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        guild = self.bot.get_guild(self.guildid)
        channel = guild.get_channel(self.channelid)

        deleted = Embed(description=f"Member was unbanned from the server.", color=0x4040EC).set_author(name=str(user))
        await channel.send(embed=deleted)

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        guild = self.bot.get_guild(self.guildid)
        channel = guild.get_channel(self.channelid)

        deleted = Embed(description=f"Role was created.", color=0x4040EC).set_author(name=str(role))
        await channel.send(embed=deleted)

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        guild = self.bot.get_guild(self.guildid)
        channel = guild.get_channel(self.channelid)

        deleted = Embed(description=f"Role was deleted.", color=0x4040EC).set_author(name=str(role))
        await channel.send(embed=deleted)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.nick != after.nick and after.nick is not None:
            guild = self.bot.get_guild(self.guildid)
            channel = guild.get_channel(self.channelid)

            deleted = Embed(description=f"Users info has changed.", color=0x4040EC).set_author(name=str(after))

            deleted.add_field(name="Before", value=before.nick)
            deleted.add_field(name="After", value=after.nick)
            deleted.timestamp = after.created_at
            await channel.send(embed=deleted)


async def setup(bot):
    await bot.add_cog(logs(bot))