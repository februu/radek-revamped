import discord
import wavelink
from discord.ext import commands

class MusicCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.repeat_settings = {}

    # Listen for track ending event
    @commands.Cog.listener()
    async def on_wavelink_track_end(self, payload: wavelink.TrackEndEventPayload):
        player = payload.player
        if player:
            if self.repeat_settings[player.guild.id]:
                print(f"\033[32m[INFO - MUSIC]\033[0m Playing {payload.track.title} \033[34m[looping]\033[0m.")
                await player.play(payload.track)
            else:
                if not player.queue.is_empty:
                    next_song = await player.queue.get_wait()
                    print(f"\033[32m[INFO - MUSIC]\033[0m Playing {next_song.title}.")
                    await player.play(next_song)
                else:
                    print(f"\033[32m[INFO - MUSIC]\033[0m Queue is empty. Disconnecting.")
                    await player.disconnect()


    # Command to play a song or add it to queue
    @discord.slash_command(name="play", description="Plays some good tunez")
    @discord.option("query", description="Enter your query")
    @discord.guild_only()
    async def play(self, ctx: discord.ApplicationContext, query : str):
        vc = ctx.voice_client

        if not await self.check_if_user_eligible(ctx):
            return

        await ctx.defer()
        print(f"\033[32m[INFO - MUSIC]\033[0m Invoked /play with query: {query}.")

        # Search for song on YouTube
        song = await wavelink.Pool.fetch_tracks(f"ytsearch:{query}")

        if not song: 
            return await ctx.followup.send("No song found. You stupid?")
        
        if not vc:
            max_retries = 3
            retries = 0
            while retries < max_retries:
                try:
                    vc = await ctx.author.voice.channel.connect(cls=wavelink.Player, reconnect=True)
                    print(f"\033[32m[INFO - MUSIC]\033[0m Connected to {ctx.author.voice.channel.name}.")
                    # Reset track looping settings
                    self.repeat_settings[ctx.guild_id] = False
                    break
                except wavelink.exceptions.ChannelTimeoutException:
                    vc = None
                    retries += 1
            if not vc:
                print(f"\033[31m[ERROR - MUSIC]\033[0m Failed to connect to {ctx.author.voice.channel.name}.")
                return await ctx.followup.send("Error has occured. Try using /shutdown command to restart the bot.")

        # Play or add to queue
        if vc.queue.is_empty and not vc.playing:
            await vc.play(song[0])
            print(f"\033[32m[INFO - MUSIC]\033[0m Playing {song[0].title}.")
            embed = create_embed(f"<a:now_playing:1228665822378065921> **NOW PLAYING** <a:now_playing:1228665822378065921>", f"*{song[0].title}*", song[0].artwork)
            await ctx.followup.send("", embed=embed)
        else:
            vc.queue.put(song[0])
            print(f"\033[32m[INFO - MUSIC]\033[0m Added {song[0].title} to queue.")
            embed = create_embed(f"<a:now_playing:1228665822378065921> **ADDED TO QUEUE** <a:now_playing:1228665822378065921>", f"*{song[0].title}*", song[0].artwork)
            await ctx.followup.send("", embed=embed)
       

    # Command to pause the player
    @discord.slash_command(name="pause", description="Pauses/resumes the music")
    @discord.guild_only()
    async def pause(self, ctx: discord.ApplicationContext):
        vc = ctx.voice_client

        if not await self.check_if_user_eligible(ctx):
            return
        if not vc:
            return await ctx.respond("I'm not even connected bozo 🤡", ephemeral=True)

        await vc.pause(not vc.paused)
        if vc.paused:
            print(f"\033[32m[INFO - MUSIC]\033[0m Paused.")
            await ctx.respond("Paused")
        else:
            print(f"\033[32m[INFO - MUSIC]\033[0m Resumed.")
            await ctx.respond("Resumed")


    # Command to display the queue
    @discord.slash_command(name="queue", description="Displays the queue")
    @discord.guild_only()
    async def queue(self, ctx: discord.ApplicationContext):
        vc = ctx.voice_client

        if not await self.check_if_user_eligible(ctx):
            return
        if not vc:
            return await ctx.respond("I'm not even connected bozo 🤡", ephemeral=True)

        content = ""
        for index, track in enumerate(vc.queue):
            content += f"{index}. {track.title}\n"
        embed = create_embed(f"<a:now_playing:1228665822378065921> **QUEUE** <a:now_playing:1228665822378065921>", content)
        await ctx.respond("", embed=embed)


    # Command to clear the queue
    @discord.slash_command(name="clearqueue", description="Clears the queue")
    @discord.guild_only()
    async def clear_queue(self, ctx: discord.ApplicationContext):
        vc = ctx.voice_client

        if not await self.check_if_user_eligible(ctx):
            return
        if not vc:
            return await ctx.respond("I'm not even connected bozo 🤡", ephemeral=True)

        if not vc.queue.is_empty:
            vc.queue.clear()
            print(f"\033[32m[INFO - MUSIC]\033[0m Queue cleared.")
        await ctx.respond("Queue cleared.")


    # Command to skip currently playing song
    @discord.slash_command(name="skip", description="Skips to next song in queue")
    @discord.guild_only()
    async def skip(self, ctx: discord.ApplicationContext):
        vc = ctx.voice_client

        if not await self.check_if_user_eligible(ctx):
            return
        if not vc:
            return await ctx.respond("I'm not even connected bozo 🤡", ephemeral=True)

        await vc.seek(vc.current.length) 
        self.repeat_settings[ctx.guild_id] = False
        print(f"\033[32m[INFO - MUSIC]\033[0m Skipping current track.")
        await ctx.respond("Skipping...")


    # Command to loop currently playing song
    @discord.slash_command(name="loop", description="Loops currently played track")
    @discord.guild_only()
    async def loop(self, ctx: discord.ApplicationContext):
        vc = ctx.voice_client

        if not await self.check_if_user_eligible(ctx):
            return
        if not vc:
            return await ctx.respond("I'm not even connected bozo 🤡", ephemeral=True)

        if self.repeat_settings[ctx.guild_id]:
            await ctx.respond("Looping disabled")
            print(f"\033[32m[INFO - MUSIC]\033[0m Looping disabled.")
            self.repeat_settings[ctx.guild_id] = False
        else:
            await ctx.respond("Looping enabled")
            print(f"\033[32m[INFO - MUSIC]\033[0m Looping enabled.")
            self.repeat_settings[ctx.guild_id] = True



    # Command to disconnect the bot
    @discord.slash_command(name="disconnect", description="Disconnects the bot from voice channel.")
    @discord.guild_only()
    async def disconnect(self, ctx: discord.ApplicationContext):
        vc = ctx.voice_client

        if not await self.check_if_user_eligible(ctx):
            return
        if not vc:
            return await ctx.respond("I'm not even connected bozo 🤡", ephemeral=True)

        await vc.disconnect()
        print(f"\033[32m[INFO - MUSIC]\033[0m Disconnected.")
        await ctx.respond("Disconnected.")



    async def check_if_user_eligible(self, ctx):
        if not ctx.author.voice.channel:
            await ctx.respond("You must be in voice channel to use this :bruh:", ephemeral=True)
            return False
        if ctx.voice_client:
            if ctx.author.voice.channel.id != ctx.voice_client.channel.id: 
                await ctx.respond("You must be in the same voice channel as me duh.", ephemeral=True)
                return False
        return True



def setup(bot): 
    bot.add_cog(MusicCog(bot)) 


def create_embed(title, content, img=""):
    embed=discord.Embed(title=title, description=content, color=0x0799b8, image=img)
    embed.set_author(name="✨ Radek ✨", url="http://febru.me", icon_url="https://cdn.discordapp.com/avatars/768542083228368907/63758443b0b61297da199dc1741bcc8a")
    return embed