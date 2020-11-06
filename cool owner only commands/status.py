@client.command()
async def status(ctx, job, *, statoos):
      if ctx.author.id == ownerdude: #here ownerdude = bots owner id
        if job == 'playing':  
              await client.change_presence(activity=discord.Game(name=statoos))
              await ctx.send(f"**Changed Presence To -> `playing | {statoos}` **")
          elif job == "streaming":
              def check(m):
                  return m.author == ctx.author
              await ctx.send(f"**What Is The URL You Want It To Stream? {ctx.author.mention}**")
              link = await client.wait_for('message', check=check, timeout=30)
              await client.change_presence(activity=discord.Streaming(name=statoos, url=link.content))
              await ctx.send(f"**Changed Presence To -> `streaming | {statoos}` **")
          elif job == "listening":
              await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=statoos))
              await ctx.send(f"**Changed Presence To -> `listening | {statoos}` **")
          elif job == "watching":
              await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=statoos))
              await ctx.send(f"**Changed Presence To -> `watching | {statoos}` **")
          else:
              await ctx.send("**Could not find option! Options are: ```\nplaying status\nstreaming status\nlistening status\nwatching status```**")
      else:
          pass
