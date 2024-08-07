import discord
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Command to shutdown the bot
    @discord.slash_command(name="shutdown", description="Shutdowns the bot")
    @discord.guild_only()
    async def restart(self, ctx: discord.ApplicationContext):
        await ctx.respond("Shutting down..")
        await self.bot.close()


def setup(bot): 
    bot.add_cog(Admin(bot)) 