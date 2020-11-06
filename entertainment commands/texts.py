@client.command()
async def underline(ctx, *, message: str):
    if statcheck() == "1":
        await ctx.send(f"__{message}__")

@client.command()
async def cb(ctx, *, message: str):
    if statcheck() == "1":
        await ctx.send(f"```{message}```")

@client.command()
async def bold(ctx, *, message):
    await ctx.send(f"*{message}*")

@client.command()
async def dbold(ctx, *, message):
    await ctx.send(f"**{message}**")

@client.command()
async def tbold(ctx, *, message):
    await ctx.send(f"***{message}***")

@client.command()
async def rtext(ctx, *, message):
      await ctx.send(f"""```diff
  -{message}
      ```""")

@client.command()
async def gtext(ctx, *, message):
    await ctx.send(f"""```css
{message}
    ```""")

@client.command()
async def btext(ctx, *, message):
    await ctx.send(f"""```ini
[{message}
```""")
