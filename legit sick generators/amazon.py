#none of these programs will really generate anything, I AM AGAINST ANYTHING ILLEGAL And the only purpose of this is to make your bot more interesting
@client.command()
async def amazon(ctx):
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    generate1 = random.choice(gentype)
    generate2 = random.choice(gentype)
    generate3 = random.choice(gentype)
    generate4 = random.choice(gentype)
    space1 = "-"
    generate5 = random.choice(gentype)
    generate6 = random.choice(gentype)
    generate7 = random.choice(gentype)
    generate8 = random.choice(gentype)
    generate9 = random.choice(gentype)
    generate10 = random.choice(gentype)
    space2 = "-"
    generate11 = random.choice(gentype)
    generate12 = random.choice(gentype)
    generate13 = random.choice(gentype)
    generate14 = random.choice(gentype)
    code = generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+space2+generate9+generate10+generate11+generate12
    global giftcards
    global num
    global counter
    global invalid
    global valid
    success_keyword = """ <b>Enter claim code</b> """
    r = requests.post("https://www.amazon.com/gc/redeem?ref_=gcui_b_e_r_c_d_b_w", data={"giftcard": code})
    if success_keyword in r.text:
        await ctx.send("Code Generated is: " + code)
        await ctx.send("Checking...")
        await ctx.send("|| Your Amazon Code Is Actually Valid Bro! Code Is: " + code + " ||")
    else:
        await ctx.send("Code Generated is: " + code)
        await ctx.send("Checking...")
        await ctx.send("|| Sad, Invalid Amazon Code: " + code + " ||")

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def amazoncheck(ctx, *, code):
    global giftcards
    global num
    global counter
    global invalid
    global valid
    success_keyword = """ <b>Enter claim code</b> """
    r = requests.post("https://www.amazon.com/gc/redeem?ref_=gcui_b_e_r_c_d_b_w", data={"giftcard": code})
    if success_keyword in r.text:
        await ctx.send("|| Your Amazon Code Is Actually Valid Bro! Code Is: " + code + " ||")
    else:
        await ctx.send("|| Sad, Invalid Amazon Code: " + code + " ||")
