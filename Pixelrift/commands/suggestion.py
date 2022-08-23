import discord
from discord import app_commands, Embed
from discord.ext import commands

class suggestion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guildid = 992875838116737165
        self.channelid = 994614166524534844

    @app_commands.command(name="suggest", description="Create a suggestion!")
    async def suggest(self, interaction: discord.Interaction, suggestion: str) -> None:
        if suggestion is not None:
            guild = self.bot.get_guild(self.guildid)
            channel = guild.get_channel(self.channelid)

            embed = Embed(title="Suggestion", description=suggestion, color=0x4040EC).set_author(name=interaction.user.name)
            message = await channel.send(embed=embed)
            emoji = '✅'
            emoji2 = '❌'
            await message.add_reaction(emoji)
            await message.add_reaction(emoji2)

async def setup(bot):
    await bot.add_cog(suggestion(bot), guilds = [discord.Object(id=992875838116737165)])