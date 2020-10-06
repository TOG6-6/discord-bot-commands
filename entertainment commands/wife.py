@client.command()
async def wife(ctx):
    wives = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '20 - But youre gayyyyyyyyyy!')
    await ctx.send(f'Answer: {random.choice(wives)}')