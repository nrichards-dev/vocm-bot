
# VOCM Radio Discord Bot

Discord bot to stream VOCM Newfoundland's radio station to your server.

Invite the bot with [this link!](https://discord.com/oauth2/authorize?client_id=1343083960623697970&permissions=36711424&integration_type=0&scope=bot)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DISCORD_TOKEN`


## Run Locally

Clone the project

```bash
  git clone https://github.com/nrichards-dev/vocm-bot
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python bot.py
```


## Commands
Default prefix is '>'
- play      (Bot will join and AUTOMATICALLY stream the station.)
- leave     (Leaves the discord channel and stops playing music.)
## Disclaimer

The audio streams played by this bot are sourced from third-party radio stations. The creator of this bot is not responsible for the content, availability, or use of these streams. By using this bot, you acknowledge that you understand and accept these terms.