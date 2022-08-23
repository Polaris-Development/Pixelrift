import discord
from discord import app_commands, Button, ButtonStyle
from discord.ext import commands, tasks
from discord.utils import get
import json



class counting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        global data2
        with open("json/config.json", "r") as file:
            data2 = json.load(file)


    @app_commands.command(name="setcountingchannel", description="set the counting channel!")
    async def setcountingchannel(self, interaction: discord.Interaction, channel: discord.TextChannel):
        role_id = 994590697866936341
        role = interaction.guild.get_role(int(role_id))
        if role in interaction.user.roles:
            data2["countingChannel"] = channel.id
            with open(self.bot.filename2, "w") as file:
                json.dump(data2,file, indent=2)
            embedVar = discord.Embed(description = f":white_check_mark: Channel set to ``{channel}``!")
            await interaction.response.send_message(embed=embedVar)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == data2["countingChannel"]:
            if str(message.content) == str(data2["count"] + 1):
                data2["count"] += 1
                emoji = '✅'
                await message.add_reaction(emoji)

            else:
                emoji = '❌'
                await message.add_reaction(emoji)
                data2["count"] = 0

            with open(self.bot.filename2, "w") as file:
                json.dump(data2,file, indent=2)

async def setup(bot):
    await bot.add_cog(counting(bot), guilds = [discord.Object(id=992875838116737165)])