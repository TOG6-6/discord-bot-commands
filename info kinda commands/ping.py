@client.command()
async def ping(ctx):
      if round(client.latency * 1000) <= 50:
          await ctx.send(f'**I Have A `{round(client.latency * 1000)}` Milli Seconds! The Server Is Based Off `{(ctx.message.guild.region)}`! The Ping Is GREAT!**')
      else:
          await ctx.send(f'**I Have A `{round(client.latency * 1000)}` Milli Seconds! The Server Is Based Off `{(ctx.message.guild.region)}`! The Ping Could Be Better Honestly!**')
