<p align="center">
  <img width="512" height="512" src="https://raw.githubusercontent.com/februu/februu.github.io/refs/heads/main/media/radek-logo.png">
</p>

# Radek Revamped

Multipurpose discord bot built with PyCord and WaveLink. _Still in development._

## Available commands

**Music Cog**

- `play <query>` - Searches <query> on youtube and adds it to queue.
- `pause` - Pauses/resumes the bot.
- `loop` - Enables one-track repeat mode.
- `skip` - Skips currently played track.
- `queue` - Displays the queue.
- `clearqueue` - Empties the queue.
- `disconnect` - Disconnects the bot from voice channel.

**Admin Cog**

- `shutdown` - Shuts down the bot. (You can use it with bash script to restart the bot whenever you want).

**AI Cog**

- `gpt <query>` - Sends <query> to gpt 4o-mini.

## Installation

```shell
git clone https://github.com/februu/radek-revamped
cd radek-revamped
pip install -r requirements.txt
```

If you want to run this bot for yourself, you need to create a `config.py` file in the main directory and paste the definitions below:

```python
'''
config.py
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

You can obtain Discord Bot Token from [Discord Developer Portal](https://discord.com/developers/applications) and get some free LavaLink servers from [here](https://lavalink.darrennathanael.com/SSL/lavalink-with-ssl/). Then install the libraries from requirements.txt. I suggest using Oracle Cloud Instance to host your bot for free 😊

⚠️ In case of errors use the command below to download newest version of PyCord and get rid of conflicts with discord.py: ⚠️

```shell
pip uninstall discord.py
pip uninstall py-cord
pip install git+https://github.com/pycord-development/pycord
pip install py-cord
```
