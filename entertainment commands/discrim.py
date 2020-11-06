@client.command()
async def discrim(ctx, numero: str):
      try:
          if len(str(numero)) == 4:
              members = [member.name + "#" + member.discriminator for member in ctx.guild.members if member.discriminator == numero]
              await ctx.send("\n".join(members))
          elif len(str(numero)) == 3:
              await ctx.send(f"**Did You Mean: `0{numero}` or `{numero}0`?**")
          else:
              await ctx.send("**`I'm Not Sure You Understood How To Use This Command!`**")
      except:
          await ctx.send(f"**Nobody has the discriminator -> `{numero}`**")
