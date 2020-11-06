@client.command()
@commands.has_guild_permissions(manage_channels=True)
async def deletevc(ctx, *, mane: discord.VoiceChannel):
    await mane.delete()
    await ctx.send(f"**Successfully Deleted Voice Channel - `{mane}`**")
