##your usual discord imports
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        #await member.kick(reason=reason)
        await ctx.send("**`" + str(member) + "` was kicked from `" + str(ctx.guild.name) + "` by `" + (ctx.author.mention) + "` with reason: `" + str(reason) + "` succesfully!**")
    except:
        await ctx.send("** I don't thing you can kick `" + str(member) + "` " + ctx.author.mention + "**")