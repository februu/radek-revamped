import discord
import wavelink
from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="rplay")
    @discord.option("query", description="Enter your query")
    @discord.guild_only()
    async def play(self, ctx: discord.ApplicationContext, query : str):
        vc = ctx.voice_client 

        if not vc: 
            if not ctx.author.voice.channel:
                return await ctx.respond("You must be in voice channel to use this :bruh:", ephemeral=True)
                
        song = await wavelink.Pool.fetch_tracks(f"ytsearch:{query}")

        if not song: #
            return await ctx.respond("No song found. You stupid?", ephemeral=True)

        vc = await ctx.author.voice.channel.connect(cls=wavelink.Player) 

        if ctx.author.voice.channel.id != vc.channel.id: 
            return await ctx.respond("You must be in the same voice channel as me duh.", ephemeral=True)

        await vc.play(song[0])

        embed = self.create_embed(f"<a:now_playing:1228665822378065921> **NOW PLAYING** <a:now_playing:1228665822378065921>", f"*{vc.current.title}*", vc.current.artwork)
        await ctx.respond("", embed=embed)
            

    def create_embed(self, title, content, img=""):
        embed=discord.Embed(title=title, description=content, color=0x0799b8, image=img)
        embed.set_author(name="✨ Radek ✨", url="http://febru.me", icon_url="https://cdn.discordapp.com/avatars/768542083228368907/63758443b0b61297da199dc1741bcc8a")
        return embed
    
def setup(bot): 
    bot.add_cog(Music(bot)) 
