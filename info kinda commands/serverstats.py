#your usual discord imports
@client.command()
async def serverstat(ctx):
    wlist = []
    for w in await ctx.guild.webhooks():
        wlist.append(f"{w.name} - {w.url}")
    content = "\n".join(wlist)
    lk = len(wlist)
    server_name = str(ctx.guild.name)
    server_owner = str(ctx.guild.owner)
    users = (ctx.guild.member_count)
    arb = int(users)
    countas = 0
    for user in list(ctx.guild.members):
        if user == user.bot:
            countas +=1
    server_region = str(ctx.message.guild.region)
    role_count = len(ctx.message.guild.roles)
    emoji_count = len(ctx.message.guild.emojis)
    channel_count = len([x for x in ctx.message.guild.channels if type(x) == discord.channel.TextChannel])
    voice_count = len(ctx.guild.voice_channels)
    created_on = ctx.message.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S')
    verification_level = ctx.message.guild.verification_level
    idserver = ctx.message.guild.id
    iconurl = ctx.message.guild.icon_url
    await ctx.send("``` ```")
    await ctx.send(f"""***SERVER STATS ARE: ***
**Server Name: `{server_name}`
Server Owner: `{server_owner}`
Server ID: `{str(idserver)}`
Full Count Of Users: `{str(arb)}`
Number Of Members: `{str(arb-countas)}`
Number Of Bots: `{str(countas)}`
Number Of Channels: `{str(channel_count)}`
Number Of Voice Channels: `{str(voice_count)}`
Number Of Roles: `{str(role_count)}`
Number Of Emojis: `{str(emoji_count)}`
Number Of Boosts: `{str(ctx.message.guild.premium_subscription_count)}`
Number Of Webhooks: `{str(lk)}`
Verification Level: `{str(verification_level)}`
Server Region: `{str(server_region)}`
Server Created On: `{str(created_on)}`**""")
    await ctx.send(iconurl)
    await ctx.send("``` ```")
