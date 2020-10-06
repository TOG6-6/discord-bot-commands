#create a txt called creditcard.txt in the same folder
#none of these programs will really generate anything, I AM AGAINST ANYTHING ILLEGAL And the only purpose of this is to make your bot more interesting
@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def cc(ctx):
    await ctx.send("**`Sending CC To Your DMs!`**")
    f = open("creditcard.txt")
    number_of_lines = 1
    for i in range(number_of_lines):
        line = f.readline()
        await ctx.author.send("**`CreditCardNo|ExpMonth|ExpYear|CVV`**")
        await ctx.author.send("**`" + line + "`**")
        await ctx.author.send("""
**Information To Use With The Card:**
**`Address : 
Street: Stone St
City: New York
State: New York
Zip Code: 10004
Country: USA`**""")
    a_file = open("creditcard.txt", "r")
    lines = a_file.readlines()
    a_file.close()
    del lines[0]
    new_file = open("creditcard.txt", "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()