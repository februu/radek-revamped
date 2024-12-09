import discord
from discord.ext import commands

class AdminCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Command to shutdown the bot
    @discord.slash_command(name="shutdown", description="Shutdowns the bot")
    @discord.guild_only()
    async def restart(self, ctx: discord.ApplicationContext):
        print(f"\033[32m[INFO - ADMIN]\033[0m Invoked /shutdown. Shutting down...")
        await ctx.respond("Shutting down..")
        await self.bot.close()


def setup(bot): 
    bot.add_cog(AdminCog(bot)) 