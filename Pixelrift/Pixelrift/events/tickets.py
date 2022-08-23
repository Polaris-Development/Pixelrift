import discord
from discord import app_commands, Button, ButtonStyle
from discord.ext import commands, tasks
from discord.utils import get


class Menu(discord.ui.View):

    @discord.ui.button(label='Support', style=discord.ButtonStyle.blurple)
    async def ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer(ephemeral=True)
        guild = interaction.guild
        role_id = 994590697866936341

        category = discord.utils.get(interaction.guild.categories, name="Text Channels")
        channel = await guild.create_text_channel(f"ticket", category=category)

        role = interaction.guild.get_role(int(role_id))
        await channel.set_permissions(role, read_messages=True, send_messages=True, read_message_history=True)
        await channel.set_permissions(interaction.user, read_messages=True, send_messages=True, read_message_history=True)
        await channel.set_permissions(guild.default_role, read_messages=False, send_messages=False)

        await channel.send(f"<@{interaction.user.id}>")


class tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="setticketchannel", description="set the tickets channel!")
    async def setchannel(self, interaction: discord.Interaction, channel: discord.TextChannel):
        role_id = 994590697866936341
        role = interaction.guild.get_role(int(role_id))
        if role in interaction.user.roles:
            
            try:
                embedVar = discord.Embed(title="Support Ticket", description="Open a ticket to get support!", color=0xfbff00, timestamp=interaction.created_at)
                embedVar.set_thumbnail(url=interaction.user.avatar)  


                view = Menu()
                await channel.send(embed=embedVar, view=view)

                embedVar2 = discord.Embed(description = f":white_check_mark: Channel set to ``{channel}``!")
                await interaction.response.send_message(embed=embedVar2)

            except:
                embedVar = discord.Embed(description = "<:x:926891125808181288> Please enter a valid channel!")
                await interaction.response.send_message(embed=embedVar)


async def setup(bot):
    await bot.add_cog(tickets(bot), guilds = [discord.Object(id=992875838116737165)])