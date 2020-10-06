@client.command()
async def dmall(ctx, *, message):
    if ctx.message.author.id == ownerdude:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(Fore.LIGHTRED_EX + "[" + current_time + "] DMing everyone in " + str(ctx.guild.name), "by " + (ctx.author.name +"#"+ ctx.author.discriminator))
        for user in list(ctx.guild.members):
            try:
                await asyncio.sleep(0.5)
                await user.send(message)
            except:
                pass
        print("[" + current_time + "] DMed everyone in " + str(ctx.guild.name), "by " + (ctx.author.name +"#"+ ctx.author.discriminator))