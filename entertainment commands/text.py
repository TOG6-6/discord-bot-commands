#for this you will need text2art library
#pip install text2art
import text
@client.command()
async def text(ctx, *, gene):
    gena = gene
    fontlist = ['random', 'rand' 'small', 'rnd-medium', 'cybermedum']
    fontrandom = random.choice(fontlist)
    arting = text2art(gena, font=f'{fontrandom}')
    await ctx.send(f"""```
{arting}
```""")