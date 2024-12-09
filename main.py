import discord
import wavelink
from discord.ext import commands

from config import DISCORD_TOKEN, GUILD_ID, LAVALINK_URI, LAVALINK_PASSWORD, ENABLED_COGS, DISCORD_ACTIVITY_NAME

intents = discord.Intents.all()
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=DISCORD_ACTIVITY_NAME), status=discord.Status.idle)
    print("\033[32m[INFO]\033[0m Connected to Discord.")
    for cog in ENABLED_COGS:
        bot.load_extension(f"cogs.{cog}")
        print(f"\033[32m[INFO]\033[0m Loaded {cog} Cog.")
    await bot.sync_commands(guild_ids=[GUILD_ID])
    print("\033[32m[INFO]\033[0m Synced commands.")
    await wavelink.Pool.connect(nodes=[wavelink.Node(client=bot, uri=LAVALINK_URI, password=LAVALINK_PASSWORD)])
    print(f"\033[32m[INFO]\033[0m Connected to Lavalink ({LAVALINK_URI}).")
    
if __name__ == "__main__":
     bot.run(DISCORD_TOKEN)