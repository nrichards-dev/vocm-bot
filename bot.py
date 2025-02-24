import discord
import yt_dlp
from os import getenv
from dotenv import load_dotenv
from discord.ext import commands
from discord import FFmpegPCMAudio
load_dotenv()
DISCORD_TOKEN = getenv('DISCORD_TOKEN')
VOCM_LIVE_URL = 'https://newcap.leanstream.co/VOCMAM?args=3rdparty_02&aw_0_req.gdpr=false&gdpr=false'

def main():

    ydl_opts = {
        'format': 'bestaudio',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'quiet': True,
    }

    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix='>', intents=intents)

    @client.event
    async def on_ready():
        print('Connection established to discord.')
        print('----------------------------------')

    @client.command(pass_context=True)
    async def join(ctx):
        if ctx.author.voice:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(VOCM_LIVE_URL, download=False)
                url = info['formats'][0]['url']

            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio(url)
            player = voice.play(source)

            
        else:
            await ctx.send('You must be in a voice channel first.')
    
    @client.command(pass_context=True)
    async def leave(ctx):
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()
        else:
            await ctx.send('I am not in a voice channel.')

    client.run(DISCORD_TOKEN)

main()