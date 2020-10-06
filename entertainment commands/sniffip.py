@client.command()
async def sniffip(ctx, moron):
    ilsa = random.choice(IP)
    await ctx.send("Grabbing" + moron +"'s ip...")
    time.sleep(3)
    await ctx.send("Bruteforcing to confirm...")
    time.sleep(2)
    await ctx.send("The IP is: " + ilsa)