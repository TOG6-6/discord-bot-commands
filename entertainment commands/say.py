@client.command()
async def say(ctx, *, somethingshit):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(Fore.LIGHTBLUE_EX + (ctx.author.name +"#"+ ctx.author.discriminator) + " said '" + somethingshit + "' in " + str(ctx.guild.name))
    if '@everyone' in somethingshit:
        await ctx.send("**`GO TO HELL " + ctx.author.name + " AHAHAHA`**")
        await ctx.send("**@" + ctx.author.name + " is a loser lmaoooooo!**")
    elif '@here' in somethingshit:
        await ctx.send("**`GO TO HELL " + ctx.author.name + " AHAHAHA`**")
        await ctx.send("**@" + ctx.author.name + " is a loser lmaoooooo!**")
    else:
        await ctx.send("**`" + somethingshit + "`**")
        await ctx.send("**   **")
        await ctx.send("-" + (ctx.author.name +"#"+ ctx.author.discriminator))