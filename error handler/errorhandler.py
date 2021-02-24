#your usual discord imports
@bot.event
async def on_command_error(ctx, error):
    embed = discord.Embed(title="Error", color=0xff0000, description=str(error))
  await ctx.channel.send(embed=embed)







@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("**`Command doesn't exist!`**")
        retur

    if isinstance(error, commands.CommandOnCooldown):
        coolerrr = "**`Mate `" + (ctx.author.mention) + "` You are on cooldown for {:.2f}s. Please Be Patient!`**".format(error.retry_after)
        await ctx.send(coolerrr)
        return

    if isinstance(error, commands.BotMissingPermissions):
            missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
            if len(missing) > 2:
                fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = ' and '.join(missing)
            _message = '**I need the `{}` permission(s) to run this command.**'.format(fmt)
            await ctx.send(_message)
            return

    if isinstance(error, commands.CheckFailure):
            await ctx.send("**You do not have permission to use this command.**" + ctx.author.mention)
            return
    
    if isinstance(error, commands.MissingPermissions):
        missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
        if len(missing) > 2:
            fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
            return
        else:
            fmt = ' and '.join(missing)
        _message = 'You need the **{}** permission(s) to use this command.'.format(fmt)
        await ctx.send(_message)
        return

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("**`You Need To Give The Required Statement After The Command Bruh, `" + (ctx.author.mention) + "**")
        return
    
    if isinstance(error, commands.BadArgument):
        await ctx.send("**`SOME ERRNO`**")
        return

    if isinstance(error, AttributeError):
        return

    raise error
