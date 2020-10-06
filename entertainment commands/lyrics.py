import requests #pip install requests
#your usual discord imports
@client.command()
async def lyric(ctx, artist, title):
    r = requests.get('https://api.lyrics.ovh/v1/{}/{}'.format(artist, title))
    if r.status_code == 200:
        l_response = json.loads(r.content)
        try:
            lyric = l_response["lyrics"]
            await ctx.send(f'**`Here are the lyrics:`**\n```{lyric}```')
        except:
            await ctx.send(f'**`Lyrics not found!`**')