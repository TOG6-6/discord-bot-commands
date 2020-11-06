@client.command()
@commands.has_guild_permissions(manage_channels=True)
async def createvc(ctx, *, mane):
    if statcheck() == "1":
        guild = ctx.guild
        await guild.create_voice_channel(name=mane)
        await ctx.send(f"**Successfully Created Voice Channel - `{mane}`**")
