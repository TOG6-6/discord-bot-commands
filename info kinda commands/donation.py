@client.command()
async def sponsor(ctx):
        await ctx.send("**`Check Your DMS!`" + ctx.author.mention + "**")
        await ctx.author.send("You have No Idea On how much I appreciate that you want to sponsor my server and/or my work!")
        await ctx.author.send("I really Appreciate it!")
        await ctx.author.send("Are You Sure You Want To Donate? [y/n]: ")
            
        def check(m):
            return m.author == ctx.author

        try:
            msg = await client.wait_for('message', check=check, timeout=30)

            if 'y' in msg.content:
                await ctx.author.send("https://paypal.me/togs66")
                await ctx.author.send("Thanks again :) :heart:")
            else:
                await ctx.author.send("You Didnt donate but thanks for considering :) :heart:")
        except:
            return
