@client.command()
async def minesweep(ctx):
    k = [":bomb:", ":slight_smile:"]
    await ctx.send(f"""||{random.choice(k)}||||{random.choice(k)}||||{random.choice(k)}||||{random.choice(k)}||||{random.choice(k)}||
||{random.choice(k)}||||{random.choice(k)}||||{random.choice(k)}||||{random.choice(k)}||||{random.choice(k)}||
||{random.choice(k)}||||{random.choice(k)}||||{random.choice(k)}||||{random.choice(k)}||||{random.choice(k)}||
||{random.choice(k)}||||{random.choice(k)}||||{random.choice(k)}||||{random.choice(k)}||||{random.choice(k)}||
||{random.choice(k)}||||{random.choice(k)}||||{random.choice(k)}||||{random.choice(k)}||||{random.choice(k)}||
""")
