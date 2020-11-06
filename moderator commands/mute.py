@client.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member):
      if member.id == ownerdude:
          await ctx.send("**`He My Master!`**")
      elif member.guild_permissions.kick_members:
          await ctx.send("**`Can't Mute Him, He's A Worthy One!`**")
      else:
          guild = client.get_guild(763626880775225384)
          role = guild.get_role(763698814829330432)
          await member.edit(roles=[role])
          await ctx.send(f"**`{member}` was muted by `{ctx.author.name}`**!")
