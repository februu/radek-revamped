<p align="center">
  <img width="256" height="256" src="https://raw.githubusercontent.com/februu/februu.github.io/refs/heads/main/media/radek-logo.png">
</p>

# Radek Revamped

Multipurpose Discord Bot built with PyCord, OpenAI and WaveLink. _Still in development._

## Available commands

**Music Cog**

- `play <query>` - Searches `<query>` on youtube and adds it to queue.
- `pause` - Pauses/resumes the bot.
- `loop` - Enables one-track repeat mode.
- `skip` - Skips currently played track.
- `queue` - Displays the queue.
- `clearqueue` - Empties the queue.
- `disconnect` - Disconnects the bot from voice channel.

**Admin Cog**

- `shutdown` - Shuts down the bot. (You can use it with bash script to restart the bot whenever you want).

**AI Cog**

- `gpt <query>` - Sends `<query>` to gpt 4o-mini.

## Installation

```shell
git clone https://github.com/februu/radek-revamped
```

If you want to run this bot for yourself, you need to create a `config.py` file in the main directory and paste the definitions below:

```python
'''
config.py
> ENABLED_COGS - add or remove cogs that you want the bot to load (all enabled by default).
> DISCORD_ACTIVITY_NAME - bot activity displayed on his profile. will be "Listening to {DISCORD_ACTIVITY_NAME}".
> LAVALINK_URI -  should be set in the host:port format e.g. https://example.com:443
(Remember to add http:// or  https:// before the host url depending on the lavalink server ssl status).
> YT_CHANNELS - list of youtube channel ids to follow e.g "UCZa1LlHpCehqvEJQ9O281Wg"
> DISCORD_FEED_CHANNEL_ID - id of channel where the bot should post announcements about new youtube videos
> DISCORD_FEED_MESSAGE - message to display before youtube link
'''

##### Main Section #####
DISCORD_TOKEN = ''
GUILD_ID = ''
ENABLED_COGS = ["Music", "Admin", "AI", "YouTube"]
DISCORD_ACTIVITY_NAME = "good tunez 🎶"

##### Music Section #####
LAVALINK_URI = ''
LAVALINK_PASSWORD = ''

##### Youtube Section #####
YT_CHANNELS = [""]
DISCORD_FEED_CHANNEL_ID = ""
DISCORD_FEED_MESSAGE = "@everyone Nowe gorące gówno na kanale:"

##### AI Cog Section #####
OPEN_AI_API_KEY = ""
```

You can obtain Discord Bot Token from [Discord Developer Portal](https://discord.com/developers/applications) and get some free LavaLink servers from [here](https://lavalink.darrennathanael.com/SSL/lavalink-with-ssl/). I also suggest using Oracle Cloud Instance to host your bot for free 😊

To run the bot use the command provided below. You will need [uv package manager](https://github.com/astral-sh/uv) which is a small but powerful python package manager. On first launch the venv will be created and all dependencies will be downloaded automatically.

```shell
uv run main.py
```
