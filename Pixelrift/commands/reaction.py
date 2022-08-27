import discord
from discord import app_commands
from discord.ext import commands
import json

class reaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.guildid = 992875838116737165

    @app_commands.command(name="reaction", description="Set a reaction role message!")
    async def embed(self, interaction: discord.Interaction, messageid: str, emoji: str,role: discord.Role) -> None:
        guild = self.bot.get_guild(self.guildid)
        channel = guild.get_channel(interaction.channel_id)
        try:
            message = await channel.fetch_message(messageid)
            try:
                await message.add_reaction(emoji)

                try:
                    self.bot.data3[messageid][emoji] = {"role": role.id}
                        
                except:
                    self.bot.data3[messageid] = {emoji: {"role": role.id}}
            
                with open(self.bot.filename3, "w") as file:
                    json.dump(self.bot.data3,file, indent=2)
                await interaction.response.send_message("Reaction added!")

            except:
                await interaction.response.send_message("Invalid emoji!")
        except:
            await interaction.response.send_message("Invalid message ID!")

        print(message)

async def setup(bot):
    await bot.add_cog(reaction(bot), guilds = [discord.Object(id=992875838116737165)])