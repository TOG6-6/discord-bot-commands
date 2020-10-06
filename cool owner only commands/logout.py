@client.command()
async def logout(ctx):
    if ctx.author.id == ownerdude:
        gentype = '0123456789'
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        space1 = "-"
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        space2 = "-"
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        code = generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(Fore.RED + "[" + current_time + "] Logout Code " + Fore.RESET + code + Fore.RED + " requested in " + str(ctx.guild.name), "by " + (ctx.author.name +"#"+ ctx.author.discriminator))
        user = client.get_user(ownerdude)
        await user.send("**`" + code + "`**")
        await ctx.send("Input the password to logout")
        
        def check(m):
            return m.author == ctx.author

        try:
            msg = await client.wait_for('message', check=check, timeout=30)

            if msg.content == code:
                await ctx.send(f"**`Logging out!`**")
                sys.exit()
            else:
                await ctx.send("**`Invalid Password!`**")
        except asyncio.TimeoutError as e:
            await ctx.send("Looks like you waited too long.")
    else:
        gentype = '0123456789'
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        space1 = "-"
        generate4 = random.choice(gentype)
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        space2 = "-"
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        code = generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(Fore.RED + "[" + current_time + "] Logout Code " + Fore.RESET + code + Fore.RED + " requested in " + str(ctx.guild.name), "by " + (ctx.author.name +"#"+ ctx.author.discriminator))
        user = client.get_user(ownerdude)
        await user.send("**`" + code + "`**")
        await ctx.send("Input the password to logout")
        
        def check(m):
            return m.author == ctx.author

        try:
            msg = await client.wait_for('message', check=check, timeout=30)

            if msg.content == code:
                await ctx.send(f"**`You aren't TOG, So ABORTING!`**")
                await ctx.send("**`JKJK`**")
                await ctx.send("Logged Out!")
                sys.exit()
            else:
                await ctx.send("**`Invalid Password!`**")
        except asyncio.TimeoutError as e:
            await ctx.send("Looks like you waited too long.")