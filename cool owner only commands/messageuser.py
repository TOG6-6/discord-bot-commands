@client.command()
async def pm(ctx, user: discord.Member, *,thing: str):
    if ctx.message.author.id == ownerdude:
        print(Fore.LIGHTGREEN_EX + "You have requested to DM People!")
        print("The Process Has Begun!")
        user = client.get_user(user)    
        await user.send(thing)
        print(Fore.LIGHTGREEN_EX + "Process Done TOG!")
    else:
        await ctx.send("BRO TOG ONLY!")