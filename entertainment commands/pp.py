#your usual discord imports
import random
@client.command()
async def pp(ctx):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    pps = ['=', '==', '===', '====', '=====', '======', '=======', '========', '=========', '==========', '===========', '============', '=============', '=================']
    ppx = random.choice(pps)
    await ctx.send("8" + ppx + "D")