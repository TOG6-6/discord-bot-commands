#import time for this one
import time
@client.command()
async def hack(ctx, *, usah):
    await ctx.send("HACKING....")
    time.sleep(5)
    randsa = random.choice(USERNAMES)
    culusa = random.choice(USERNAMES)
    ralusa = random.choice(countries)
    await ctx.send(randsa + "@gmail.com - Mail")
    await ctx.send(culusa +" - Password")
    await ctx.send(ralusa)
    await ctx.send("SELLING INFORMATION TO DONALD TRUMP!...")
    time.sleep(3)
    await ctx.send("Sold To Donald Trump")
    await ctx.send("Earned Money From Your Information, damn this guy has some use atleast!")