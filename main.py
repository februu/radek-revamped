import discord
import wavelink
from discord.ext import commands

from config import DISCORD_TOKEN, GUILD_ID, LAVALINK_URI, LAVALINK_PASSWORD, ENABLED_COGS

intents = discord.Intents.all()
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="febru - piję lean"), status=discord.Status.idle)
    print("[INFO] Connected to Discord.")
    for cog in ENABLED_COGS:
        bot.load_extension(f"cogs.{cog}")
        print(f"[INFO] Loaded {cog} Cog.")
    await bot.sync_commands(guild_ids=[GUILD_ID])
    print("[INFO] Synced commands.")
    await wavelink.Pool.connect(nodes=[wavelink.Node(client=bot, uri=LAVALINK_URI, password=LAVALINK_PASSWORD)])
    print(f"[INFO] Connected to Lavalink ({LAVALINK_URI}).")
    
if __name__ == "__main__":
     bot.run(DISCORD_TOKEN)