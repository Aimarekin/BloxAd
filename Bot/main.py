import discord
from discord.ext import commands
import asyncio
import botconfig

extensions = ["managebot"]

def prefix_callable(bot, message):
    return commands.when_mentioned_or("-")(bot, message)

client = commands.Bot(command_prefix = prefix_callable, case_insensitive = True)

@client.event
async def on_ready():
    print("BloxAd is booting up!")
    log_channel = client.get_channel(505689063232372736)
    await log_channel.send("BloxAd is booting up...")
    await client.change_presence(activity=discord.Activity(type=0, name="booting up..."), status= discord.Status.idle)
    await log_channel.send("Loading cogs...")
    for extension in extensions:
        try:
            client.load_extension(f"cogs.{extension}")
        except Exception as error:
            print(f"[{error}] , error while loading cog {extension}")
            await log_channel.send(f"[{error}] , error while loading cog {extension}")
    await log_channel.send(":white_check_mark: BloxAd is online!")
    await client.change_presence(activity=discord.Activity(type=0, name="Prefix is - | BloxAd | discord.gg/wQ83rrz"))
    print("BloxAd is online!")

client.run(botconfig.token())
