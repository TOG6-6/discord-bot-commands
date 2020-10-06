#your usual discord imports
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        #await member.ban(reason=reason)
        await ctx.send("**`" + str(member) + "` was banned from `" + str(ctx.guild.name) + "` by `" + ctx.author.mention + "` with reason: `" + str(reason) + "` succesfully!**")
    except:
        await ctx.send("**Some error ocurred! Couldn't Ban `" + str(member) + "` from `" + str(ctx.guild.name) + "` " + ctx.author.mention + "`**")