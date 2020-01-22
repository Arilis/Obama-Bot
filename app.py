import requests, os, discord, urllib, time
from discord.ext import commands
os.system('cls')


client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Online.')
    game = discord.Game('.talk | By ArilisDev')
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_guild_join(guild):
    print('Joined: ' + str(guild.name) + '\nID: ' + str(guild.id) + '\nRegion: ' + str(guild.region) + '\nOwner ID: ' + str(guild.owner_id))

@client.command()
async def talk(ctx, *args):
    try:
        await ctx.send('Processing request, it might take a second! If the video cannot be played, retype the command and it should work! *mass commands by users at once will cause it to corrupt sadley*')
        _new_args = '{}'.format(' '.join(args))
        if _new_args == 'arilis is gay':
            r = requests.post(url='http://talkobamato.me/synthesize.py', data={
                "input_text": "no you're gay"
            })
        else:
            r = requests.post(url='http://talkobamato.me/synthesize.py', data={
                "input_text": _new_args
            })

        if r.status_code == 200:
            _url = r.url.replace('http://talkobamato.me/synthesize.py?speech_key=', '')
            _url2 = 'http://talkobamato.me/synth/output/' + _url + '/obama.mp4'
            time.sleep(1)

            r2 = requests.get(_url2)
            with open('./logs/' + _url + '.mp4', 'wb') as f:
                f.write(r2.content)
            print("Request './logs/" + _url + ".mp4'"" was a success")
        else:
            await ctx.send('Sorry! The requests failed!')
            print('Request Failed.\n')
        file = discord.File("./logs/" + _url + ".mp4", filename="" + _url + ".mp4")
    
        time.sleep(1)
        await ctx.send(file=file)
    except Exception:
        print('Failed to upload/request file.')
    
try:
    client.run('bot token')
except Exception:
        print('Failed to start bot.')
