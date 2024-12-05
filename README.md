![radek logo](https://cdn.discordapp.com/avatars/768542083228368907/63758443b0b61297da199dc1741bcc8a)

# Radek Revamped

Multipurpose discord bot built with PyCord and WaveLink. _Still in development._

### Available commands

- `play <query>` - Searches <query> on youtube and adds it to queue.
- `pause` - Pauses/resumes the bot.
- `loop` - Enables one-track repeat mode.
- `skip` - Skips currently played track.
- `queue` - Displays the queue.
- `clearqueue` - Empties the queue.
- `disconnect` - Disconnects the bot from voice channel.

### Setup

If you want to run this bot for yourself, you need to create a config.py file in the main directory and paste the definitions below:

```
'''
config.py
LAVALINK_URI should be set in the host:port format:
e.g. https://example.com:443
Remember to add http:// or  https:// before the host url depending on the lavalink server ssl status.
'''
DISCORD_TOKEN = ''
GUILD_ID = ''
LAVALINK_URI = '' 
LAVALINK_PASSWORD = ''
```

You can obtain Discord Bot Token from [Discord Developer Portal](https://discord.com/developers/applications) and get some free LavaLink servers from [here](https://lavalink.darrennathanael.com/SSL/lavalink-with-ssl/). Then install the libraries from requirements.txt. I suggest using Oracle Cloud Instance to host your bot for free 😊
