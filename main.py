import discord
import wavelink
from discord.ext import commands

from config import DISCORD_TOKEN, GUILD_ID, LAVALINK_URI, LAVALINK_PASSWORD

intents = discord.Intents.all()
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="febru - piję lean"), status=discord.Status.idle)
    print("[INFO] Connected to Discord.")
    bot.load_extension('cogs.Music')
    bot.load_extension('cogs.Admin')
    print("[INFO] Loaded Music Cog.")
    await bot.sync_commands(guild_ids=[GUILD_ID])
    await wavelink.Pool.connect(nodes=[wavelink.Node(client=bot, uri=LAVALINK_URI, password=LAVALINK_PASSWORD)])
    
if __name__ == "__main__":
     bot.run(DISCORD_TOKEN)