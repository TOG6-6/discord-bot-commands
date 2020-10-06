#your usual discord imports
@client.command()
async def onduty(ctx):
    online, idle, dnd, offline = [], [], [], []

    for user in ctx.guild.members:
        if ctx.channel.permissions_for(user).manage_messages:
            if not user.bot and user.status is discord.Status.online:
                online.append(f"**{user}**")
            if not user.bot and user.status is discord.Status.idle:
                idle.append(f"**{user}**")
            if not user.bot and user.status is discord.Status.dnd:
                dnd.append(f"**{user}**")
            if not user.bot and user.status is discord.Status.offline:
                offline.append(f"**{user}**")

    on = len(online)
    off = len(offline)
    dn = len(dnd)
    idlee = len(idle)
    await ctx.send(f"**Number of Mods In {str(ctx.guild.name)}**")
    await ctx.send(f"""**```🟢 - {str(on)} Members!
🟡 - {str(idlee)} Members!
🔴 - {str(dn)} Members!
⚫ - {str(off)} Members!
Total Members: {str(on + idlee + dn + off)}```**""")