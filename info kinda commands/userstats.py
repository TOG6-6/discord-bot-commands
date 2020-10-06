#your usual imports and then this code

@client.command()
async def user(ctx, member:discord.Member=None):
    if member is None:
        member = ctx.message.author
        pronoun = "Your"
    else:
        pronoun = str(member)
    name = f"{member.name}#{member.discriminator}"
    status = ctx.author.status.name
    created_on = member.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S')
    userAvatarUrl = member.avatar_url
    join = member.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S')
    statoos = member.activity
    house = member.top_role
    permissions = member.permissions_in(ctx.message.channel)
    #userhighest role
    await ctx.send("``` ```")
    await ctx.send(f"""**`Here's Some Dirt On:` {member.mention}!:
Username is: `{str(member.name)}`
UserTag is: `{str(member.discriminator)}`
User ID is: `{str(member.id)}`
User Presence is: `{str(status)}`
User Is Playing: `{str(statoos)}`
User Highest Role: `{str(house)}`
User Created On: `{str(created_on)}`
User Joined On: `{str(join)}`
User Permissions: `{str(permissions)}`**""")
    await ctx.send(userAvatarUrl)
    await ctx.send("``` ```")