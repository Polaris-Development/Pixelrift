import asyncio
import os
import discord
from discord.ext import commands
import asyncpg
import json


discord_token = "" # Discord bot token
server_id = 992875838116737165 # Place serverid to make commands work instantly in the guild

intents = discord.Intents.all()
intents.members = True

filename = "json/players.json"
filename2 = "json/config.json"
filename3 = "json/reactions.json"

async def load():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            await client.load_extension(f'commands.{filename[:-3]}')
    for filename in os.listdir('./events'):
        if filename.endswith('.py'):
            await client.load_extension(f'events.{filename[:-3]}')


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents, application_id=942067188611829780)

    async def setup_hook(self):
        await load()
        await client.tree.sync(guild = discord.Object(id = server_id))

        global data
        with open(filename, "r") as file:
            data = json.load(file)
        global data2
        with open(filename2, "r") as file:
            data2 = json.load(file)
        global data3
        with open(filename3, "r") as file:
            data3 = json.load(file)

        client.counting = data2["countingChannel"]
        client.count = data2["count"]
        client.filename = filename
        client.filename2 = filename2
        client.filename3 = filename3
        client.botname = "PixelRift"

        client.data = data
        client.data3 = data3

    async def on_ready(self):
        print("Bot Online")

client = MyBot()
client.run(discord_token)