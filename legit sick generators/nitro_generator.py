#none of these programs will really generate anything, I AM AGAINST ANYTHING ILLEGAL And the only purpose of this is to make your bot more interesting
@client.command()
@commands.cooldown(1, 600, commands.BucketType.user)
async def nitro(ctx, nitronum: int):
    if (nitronum >= 0 and nitronum <= 100):
        try:
            await ctx.send("***SENDING " + str(nitronum) + " NITRO CODES***")
            await ctx.send("`MAKE SURE DMs ARE OPEN!`")
            await ctx.send("**600 second cooldown has begun for user: `" + ctx.author.mention + "`**")
            for i in range(nitronum):
                await ctx.author.send("https://discord.gift/%s" % (('').join(random.choices(string.ascii_letters + string.digits, k=16))))
        except:
            await ctx.send("**@" + ctx.author.mention + " `Your DMs Are Closed!`**")
    else:
        await ctx.send("**Chill out dude, only number from `0 - 100!`**")
        nitro.reset_cooldown(ctx)