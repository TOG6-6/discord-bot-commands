deletedcontent = []
deleteduser = []
@client.event
async def on_message_delete(message):
    deletedcontent.append(message.content)
    deleteduser.append(message.author)
        
@client.command()
async def snipe(ctx):
    k = deletedcontent[-1]
    v = deleteduser[-1]
    try:
        await ctx.send("**`" + k + "`**")
        await ctx.send("- " + str(v))
    except KeyError:
        await ctx.send("Eh, Nothing To Snipe Here")
