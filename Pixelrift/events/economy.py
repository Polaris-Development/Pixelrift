import discord
from discord import app_commands, Button, ButtonStyle
from discord.ext import commands, tasks
from discord.utils import get
import json
from typing import Optional
import random
import asyncio



class economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if str(message.author.id) not in self.bot.data:

            self.bot.data[f'{message.author.id}'] = {"name": message.author.name,"balance": 0}

            with open(self.bot.filename, "w") as file:
                json.dump(self.bot.data,file, indent=2)

        else:
            self.bot.data[f'{message.author.id}']["balance"] = self.bot.data[f'{message.author.id}']["balance"] + 5

            with open(self.bot.filename, "w") as file:
                json.dump(self.bot.data,file, indent=2)

    @app_commands.command(name="balance", description="Shows your balance!")
    async def balance(self, interaction: discord.Interaction) -> None:
        if str(interaction.user.id) not in self.bot.data:
            embed=discord.Embed(title="You do not have a profile!", description="Type any message to automatically create a profile", color=0x335af5)
            await interaction.response.send_message(embed=embed)
        else:
            balance = self.bot.data[f'{interaction.user.id}']["balance"]
            embed=discord.Embed(title="Profile Statistics!", description=f"Balance: ${balance}", color=0x335af5)
            await interaction.response.send_message(embed=embed)
        
    @app_commands.command(name="slots", description="Plays slots!")
    async def slots(self, interaction, amount: Optional[str] = None):
        if str(interaction.user.id) in self.bot.data:
            if amount == "all" or amount == "max":
                amount = self.bot.data[f'{interaction.user.id}']["balance"]
            try:
                if amount == None:
                    embedVar = discord.Embed(color=0xfbff00)
                    embedVar.add_field(name="<:game_die:942940518747365416> **Slots Rewards**", value="2 of the same = 1.5x \n 3 of the same = 5x", inline=False)
                    embedVar.set_footer(text=f"PixelRift")
                    await interaction.response.send_message(embed=embedVar)
                elif int(amount) <= 0:
                    amount = int(amount)
                    embedVar = discord.Embed(description = "<:x:942398335975829504> Invalid amount!")
                    await interaction.response.send_message(embed=embedVar)
                elif int(amount) > 0:
                    if int(amount) <= self.bot.data[f'{interaction.user.id}']["balance"]:
                        amount = int(amount)
                        emote1 = "<:moneybag:920516033104724078>"
                        emote2 = "<:gem:920516033104724078>"
                        emote3 = "<:100:920516033104724078>"
                        emote4 = "<:first_place:920516033104724078>"
                        emote5 = "<:dollar:920516033104724078>"
                        emotes = [emote1, emote2, emote3, emote4, emote5]
                        choice1 = random.choice(emotes)
                        choice2 = random.choice(emotes)
                        choice3 = random.choice(emotes)

                        embedVar = discord.Embed(color=0xfbff00)

                        self.bot.data[f'{interaction.user.id}']["balance"] = self.bot.data[f'{interaction.user.id}']["balance"] - amount

                        with open(self.bot.filename, "w") as file:
                            json.dump(self.bot.data,file, indent=2)

                        embedVar.add_field(name="<:slot_machine:920499434993897472> **SLOTS** <:slot_machine:920499434993897472>", 
                        value="--------------\n| <a:slots:920500602654588938> <a:slots:920500602654588938> <a:slots:920500602654588938> |\n--------------\n**Spinning...**", inline=False)

                        embedVar.set_footer(text=f"PixelRift")
                        await interaction.response.send_message(embed=embedVar)

                        await asyncio.sleep(1.5)

                        embedVar.set_field_at(index=0, name="<:slot_machine:920499434993897472> **SLOTS** <:slot_machine:920499434993897472>", 
                        value="--------------\n| " + str(choice1) + " <a:slots:920500602654588938> <a:slots:920500602654588938> |\n--------------\n**Spinning...**", inline=False)

                        await interaction.edit_original_message(embed=embedVar)

                        await asyncio.sleep(1.5)

                        embedVar.set_field_at(index=0, name="<:slot_machine:920499434993897472> **SLOTS** <:slot_machine:920499434993897472>", 
                        value="--------------\n| " + str(choice1) + str(choice2) +  " <a:slots:920500602654588938> |\n--------------\n**Spinning...**", inline=False)

                        await interaction.edit_original_message(embed=embedVar)

                        await asyncio.sleep(1.5)

                        embedVar.set_field_at(index=0, name="<:slot_machine:920499434993897472> **SLOTS** <:slot_machine:920499434993897472>", 
                        value="--------------\n| " + str(choice1) + str(choice2) + str(choice3) +  " |\n--------------\n**Spinning...**", inline=False)

                        await interaction.edit_original_message(embed=embedVar)

                        if choice1 == choice2 == choice3:

                            embedVar.set_field_at(index=0, name="<:slot_machine:920499434993897472> **SLOTS** <:slot_machine:920499434993897472>", 
                            value="--------------\n| " + str(choice1) + str(choice2) + str(choice3) +  " |\n--------------\n**WINNER** You have won $" + str("{:,}".format(amount*5)) + "!", inline=False)
                            await interaction.edit_original_message(embed=embedVar)

                            self.bot.data[f'{interaction.user.id}']["balance"] = self.bot.data[f'{interaction.user.id}']["balance"] + int(amount*5)

                            with open(self.bot.filename, "w") as file:
                                json.dump(self.bot.data,file, indent=2)

                        elif choice1 == choice2 or choice2 == choice3 or choice3 == choice1:

                            embedVar.set_field_at(index=0, name="<:slot_machine:920499434993897472> **SLOTS** <:slot_machine:920499434993897472>", 
                            value="--------------\n| " + str(choice1) + str(choice2) + str(choice3) +  " |\n--------------\n**WINNER** You have won $" + str("{:,}".format(amount*1.5)) + "!", inline=False)
                            await interaction.edit_original_message(embed=embedVar)

                            self.bot.data[f'{interaction.user.id}']["balance"] = self.bot.data[f'{interaction.user.id}']["balance"] + int(amount*1.5)

                            with open(self.bot.filename, "w") as file:
                                json.dump(self.bot.data,file, indent=2)

                        else:
                            embedVar.set_field_at(index=0, name="<:slot_machine:920499434993897472> **SLOTS** <:slot_machine:920499434993897472>", 
                            value="--------------\n| " + str(choice1) + str(choice2) + str(choice3) +  " |\n--------------\n**LOST** You have not won any money!", inline=False)
                            await interaction.edit_original_message(embed=embedVar)


                    elif int(amount) > self.bot.data[f"{interaction.user.id}"]["balance"]:
                        embedVar = discord.Embed(description = "<:x:927596575407079504> You can not gamble more than you have!")
                        await interaction.response.send_message(embed=embedVar)
            except ValueError:
                embedVar = discord.Embed(description = f"<:x:927596575407079504> Invalid Parameters entered! Use /slots [amount]")
                await interaction.response.send_message(embed=embedVar)
        else:
            embed=discord.Embed(title="You do not have a profile!", description="Type any message to automatically create a profile", color=0x335af5)
            await interaction.response.send_message(embed=embed)

        

async def setup(bot):
    await bot.add_cog(economy(bot), guilds = [discord.Object(id=992875838116737165)])