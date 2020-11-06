@client.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, user: discord.Member):
      if user.id == ownerdude:
          await ctx.send("**`He My Master!`**")
      else:
          guild = client.get_guild(763626880775225384)
          role = guild.get_role(763698814829330432)
          if role not in user.roles:
              await ctx.send(f"**`{user}` is not muted!**")
          else:
              await user.remove_roles(role)
              await ctx.send(f"**Unmuted `{user}` as `{ctx.author}` Requested!**")
