@client.command()
async def goallserver(ctx, *, messags):
    if ctx.message.author.id == ownerdude:
        try:
            for guild in client.guilds: 
                await guild.system_channel.send(messags)
                await ctx.author.send("Sent the message to " + str(ctx.guild.name))
        except:
            pass
    else:
        await ctx.send("It's only for owner!")