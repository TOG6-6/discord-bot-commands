@client.command()
async def math(ctx, num: float, sym: str, numeros: float):
    if sym == '+':
        k = (num + numeros)
        await ctx.send("**`" + str(num) + str(sym) + str(numeros) + " = " + str(k) + "`**")
    elif sym == '-':
        k = num-numeros
        await ctx.send("**`" + str(num) + " " + str(sym) + " " + str(numeros) + " = " + str(k) + "`**")
    elif sym == '*':
        k = num*numeros
        await ctx.send("**`" + str(num) + " " + str(sym) + " " + str(numeros) + " = " + str(k) + "`**")
    elif sym == 'X':
        k = num*numeros
        await ctx.send("**`" + str(num) + " " + str(sym) + " " + str(numeros) + " = " + str(k) + "`**")
    elif sym == '**':
        k = num**numeros
        await ctx.send("**`" + str(num) + " " + str(sym) + " " + str(numeros) + " = " + str(k) + "`**")
    elif sym == '/':
        k = num/numeros
        await ctx.send("**`" + str(num) + " " + str(sym) + " " + str(numeros) + " = " + str(k) + "`**")
    else:
        await ctx.send("**`This Feature Not Available ATM!")