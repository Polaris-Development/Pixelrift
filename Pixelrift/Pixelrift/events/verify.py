import discord
from discord import app_commands, Button, ButtonStyle
from discord.ext import commands, tasks
from discord.utils import get

class Menu(discord.ui.View):

    def __init__(self) -> None:
        super().__init__(timeout= None)

    @discord.ui.button(label='Verify', style=discord.ButtonStyle.blurple)
    async def verification(self, interaction: discord.Interaction, button: discord.ui.Button):
        roleid = 994590697866936341

        member = interaction.user
        role = interaction.guild.get_role(roleid)
        await member.add_roles(role)
        embed = discord.Embed(title="Success!", description="You have been verified.")
        await interaction.response.send_message(embed=embed, ephemeral=True)

class verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.role = 994590697866936341
        self.added = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.added:
            self.bot.add_view(Menu())
            self.added = True


    @app_commands.command(name="verify", description="Send the verify message!")
    async def embed(self, interaction: discord.Interaction) -> None:
        e = discord.Embed(title="Verification", description="Click the verify button to get verified.")
        view = Menu()
        await interaction.response.send_message(embed=e, view=view)


async def setup(bot):
    await bot.add_cog(verify(bot), guilds = [discord.Object(id=992875838116737165)])