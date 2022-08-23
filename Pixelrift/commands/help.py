import discord
from discord import app_commands
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="The help command!")
    async def help(self, interaction: discord.Interaction) -> None:
        embed=discord.Embed(title="PixelRift Help Menu", description=f"These are the commands for PixelRift!\n``/help`` - Brings this help commands" +
        "\n`/embed (title) (message)` - Creates an embed!\n``/suggestion (suggestion)`` Send a suggestion to the server!\n``/balance`` - Shows your server balance!" +
        "\n``/slots (amount)`` - Gambles your money in slots!"
        , color=0x00ff00)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(help(bot), guilds = [discord.Object(id=992875838116737165)])