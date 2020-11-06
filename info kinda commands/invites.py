@client.command()
async def invites(ctx, member:discord.Member=None):
      if member == None:
          member = ctx.message.author
      totalInvites = 0
      for i in await ctx.guild.invites():
          if i.inviter == member:
              totalInvites += i.uses
      await ctx.send("**" + member.mention + " has invited `" + str(totalInvites) + "` to `" + str(ctx.guild.name) + "`!**")
