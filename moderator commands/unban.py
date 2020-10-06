#your usual discord imports
@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    global banned_users
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send("**UnBanned `" + member + "` Successfully!**")