import discord
from discord import app_commands
from discord.ext import commands

class suggestion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="suggest", description="Create a suggestion!")
    async def suggest(self, interaction: discord.Interaction, suggestion: str) -> None:
        if suggestion is not None:
            embedVar = discord.Embed(timestamp=ctx.message.created_at)
            embedVar.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
            embedVar.add_field(name="Suggestion", value=f"{suggestion}", inline=False)
            embedVar.set_thumbnail(url=client.user.avatar)
            message = await client.get_channel(793894831914090506).send(embed=embedVar)
            emoji = '✅'
            emoji2 = '❌'
            await message.add_reaction(emoji)
            await message.add_reaction(emoji2)
            embedVar = discord.Embed(description="<:white_check_mark:950558819279310868> Suggestion has been sent!")
            await ctx.send(embed=embedVar)
        else:
            embed = discord.Embed(description="<:x:937000558177447986> To make a suggestion, use ``s!suggest (suggestion)``!")
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(suggestion(bot), guilds = [discord.Object(id=992875838116737165)])