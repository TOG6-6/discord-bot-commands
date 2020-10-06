@client.command()
async def ship(ctx, usah1: discord.User, usah2: discord.User):
    if usah1 == usah2:
        await ctx.send("**`You Cannot Ship The Same Person!`**")
    else:
        kask = random.choice(['number', 'gay'])
        if kask == 'number':
            repcobank = random.randint(0,100)
            await ctx.send("**`" + str(usah1) + " <3 - " + str(repcobank) + "% <3 - " + str(usah2) + "`**")
        else:
            nathas = random.choice([usah1, usah2])
            if nathas == usah1:
                await ctx.send("**`IDK about " + str(usah2) + ", But " + str(usah1) + " GAYYYYYYYYYYYYYYYY!`**")
            else:
                await ctx.send("**`IDK about " + str(usah1) + ", but " + str(usah2) + " GAYYYYYYYYYYYYYYYY!`**")