import discord
from discord.ext import commands, tasks
import httpx
import xml.etree.ElementTree as ET 
from config import YT_CHANNELS, DISCORD_FEED_CHANNEL_ID, DISCORD_FEED_MESSAGE

class YouTubeCog(commands.Cog):

    def __init__(self, bot : commands.Bot):
        self.bot = bot
        self.latest_video = {}
        self.channel = None
        self.check_feeds.start()

    # Automatically send notification every time a video is uploaded to specified channel 
    @tasks.loop(seconds=60.0)
    async def check_feeds(self):
        try:
            async with httpx.AsyncClient() as client:
               for channel_id in YT_CHANNELS:
                    
                    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
                    response = await client.get(url)
                    response.raise_for_status()
                    x = ET.fromstring(response.text)

                    entry = x.find("{http://www.w3.org/2005/Atom}entry")
                    link = entry.find("{http://www.w3.org/2005/Atom}link").attrib["href"]

                    if self.latest_video.get(channel_id) == link:
                        continue
                    
                    self.latest_video[channel_id] = link
                    if self.channel == None:
                        self.channel = await self.bot.fetch_channel(DISCORD_FEED_CHANNEL_ID)
                        continue
                    await self.channel.send(f"{DISCORD_FEED_MESSAGE} {link}")

        except httpx.HTTPStatusError as e:
            return f"HTTP error occurred: {e.response.status_code}"
        except httpx.RequestError as e:
            return f"An error occurred while requesting: {str(e)}"

def setup(bot): 
    bot.add_cog(YouTubeCog(bot)) 