import discord
from discord import app_commands
from discord.ext import commands

class embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="embed", description="Create an embed from a command!")
    async def embed(self, interaction: discord.Interaction, title: str, message: str) -> None:
        if title is not None or message is not None:
            embed=discord.Embed(title=title, description=message, color=0x00ff00)
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Please use the correct format!")

async def setup(bot):
    await bot.add_cog(embed(bot), guilds = [discord.Object(id=992875838116737165)])