import discord
from discord import app_commands
from discord.ext import commands

class cheese(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="The help command!")
    async def help(self, interaction: discord.Interaction, name: str, age: int) -> None:
        await interaction.response.send_message("Test")

async def setup(bot):
    await bot.add_cog(cheese(bot), guilds = [discord.Object(id=992875838116737165)])