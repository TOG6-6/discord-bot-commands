#none of these programs will really generate anything, I AM AGAINST ANYTHING ILLEGAL And the only purpose of this is to make your bot more interesting
@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def robux(ctx):
    await ctx.send(ctx.author.mention + ", I've sent the code to Your DMs!")
    await ctx.send(ctx.author.mention + ", 10 second cooldown has begun for you!")
    gentype = '0123456789'
    generate1 = random.choice(gentype)
    generate2 = random.choice(gentype)
    generate3 = random.choice(gentype)
    space1 = "-"
    generate4 = random.choice(gentype)
    generate5 = random.choice(gentype)
    generate6 = random.choice(gentype)
    space2 = "-"
    generate7 = random.choice(gentype)
    generate8 = random.choice(gentype)
    generate9 = random.choice(gentype)
    generate10 = random.choice(gentype)
    code = generate1+generate2+generate3+space1+generate4+generate5+space1+generate6+space2+generate7+generate8+generate9+space2+generate10
    await ctx.author.send("**Your Code is: `" + code + "`**")