import discord
from discord.ext import commands
import asyncio
import time
import importlib
import Utilities
import os
from Utilities import utils
components = [utils]

class managebot:
    def __init__(self, client):
        self.client = client

    @commands.check(utils.is_bloxad_admin)
    @commands.command()
    async def shutdown (self, ctx):
        await ctx.send("BloxAd is shutting down...")
        await self.client.logout()
        await self.client.close()
        self.client.aiosession.close()

    @commands.check(utils.is_bloxad_admin)
    @commands.command()
    async def loadcog(self, ctx, cog):
        await ctx.send(f"Reloading {cog}...")
        self.client.unload_extension(f"cogs.{cog}")
        self.client.load_extension(f"cogs.{cog}")
        await ctx.send(f"{cog} reload complete :white_check_mark:")

    @commands.check(utils.is_bloxad_admin)
    @commands.command()
    async def reload(self, ctx):
        if await self.client.is_owner(ctx.author):
            async with ctx.typing():
                done = 0
                msg = await ctx.send(f"BloxAd is reloading...```Command run start```({done} done)")
                utils = importlib.reload(Utilities)
                done = done + 1
                await msg.edit(content = f"BloxAd is reloading...```Utilities reloaded```({done} done)")
                temp = []
                for cog in self.client.cogs:
                    temp.append(cog)
                    done = done + 1
                    await msg.edit(content = "BloxAd is reloading...```Appended to temp {}{}```({} done)".format(cog, str(temp), done))
                for cog in temp:
                    self.client.unload_extension(f"cogs.{cog}")
                    done = done + 1
                    await msg.edit(content = f"BloxAd is reloading...```Unloaded {cog}```({done} done)")
                    self.client.load_extension(f"cogs.{cog}")
                    done = done + 1
                    await msg.edit(content = f"BloxAd is reloading...```Loaded {cog}```({done} done)")
                for c in components:
                    importlib.reload(c)
                    done = done + 1
                    await msg.edit(content = f"BloxAd is reloading...```Reloaded util {c}```({done} done)")
            await msg.edit(content = f"BloxAd is reloading...```Reload complete {time.time()}```({done} done)")
            await ctx.send( "Reload complete ✅")

def setup(client):
    client.add_cog(managebot(client))
