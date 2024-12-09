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
        print(f"\033[32m[INFO - AI]\033[0m Invoked /gpt. Responding with:\n\n {response_content}\n\n")
        await ctx.respond(response_content)

def setup(bot): 
    bot.add_cog(AICog(bot)) 