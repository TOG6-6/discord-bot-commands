@client.command()
async def tspam(ctx, num: int, *, thing: str):
    if ctx.author.id == ownerdude:
        for i in range(num):
            await ctx.send(thing)
    else:
        await ctx.send("owner ONLY!")