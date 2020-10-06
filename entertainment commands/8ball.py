@client.command(aliases = ['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.', 'It is decidedly so', 'Without a Doubt', 'YES - Definitely', 'You may rely on it', 'As I see it, YES', 'Most Likely', 'Outlook good', 'Yes.', 'Signs Point To YES!', 'Reply Hazy, try again!', 'Ask Again Later', 'Better Not Tell You Now', 'Cannot Predict Now', 'Concentrate and ask again', 'Dont Count ON it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very Doubtful']
    saxena = random.choice(responses)
    await ctx.send('Answer: ' + saxena)