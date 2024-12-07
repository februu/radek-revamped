import discord
import httpx
from openai import AsyncOpenAI
from discord.ext import commands
from datetime import time

from config import OPEN_AI_API_KEY

class AICog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.client = AsyncOpenAI(api_key=OPEN_AI_API_KEY)
        
    @discord.slash_command(name="gpt", description="Asks a question")
    @discord.option("query", description="Enter your query")
    @discord.guild_only()
    async def gpt(self, ctx: discord.ApplicationContext, query: str):
        await ctx.defer()
        response = await self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": query}
            ],
            max_tokens=400,
            
            )
        response_content = response.choices[0].message.content
        if len(response_content) > 2000:
            response_content = response_content[:2000]  # Truncates the message if needed
        await ctx.respond(response_content)
        
    # async def get_response(self, url):
    #     try:
    #         async with httpx.AsyncClient() as client:
    #             response = await client.get(url)
    #             response.raise_for_status()
    #             return response.text
    #     except httpx.HTTPStatusError as e:
    #         print(f"HTTP error occurred: {e.response.status_code}")
    #         return ""
    #     except httpx.RequestError as e:
    #         print(f"An error occurred while requesting: {str(e)}")
    #         return ""


def setup(bot): 
    bot.add_cog(AICog(bot)) 