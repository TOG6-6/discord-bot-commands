@client.command()
async def iplookup(ctx, ip):
    if statcheck() == "1":
        response = requests.get(f"https://geolocation-db.com/json/{ip}&position=true").json()
        await ctx.send(f"**```{response}```**")
