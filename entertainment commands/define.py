@client.command()
async def define(ctx, *, query):
    try:
        url = f"http://api.urbandictionary.com/v0/define?term={query}"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        definition = data['list'][0]['definition']
        await ctx.send("**Definition is: `" + definition + "`**")
    except:
        await ctx.send("**Couldn't Find A Definition For: `" + query + "`!**")