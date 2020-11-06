@client.command()
async def donorrole(ctx):
    cost = 0
    def check(m):
        return m.author == ctx.author and m.guild is None

    features = []
    await ctx.send(f"**`Hey, Please Check Your DMs!` {ctx.author.mention}**")
    await ctx.author.send("**Hey, thank you for considering to get a custom role, this really helps me run the server :) **")
    await ctx.author.send("**Alright, First Question - `What do you want the name of the role to be?: `**")
    rolename = await client.wait_for('message', check=check, timeout=30)
    cost += 3
    kkk = rolename.content
    await ctx.author.send(f"**Rolename Has Been Set To: `{rolename.content}`**")
    await ctx.author.send("**What Do You Want The Colour Of The Role To Be?: [Ex: #FF0000]: **")
    colorcode = await client.wait_for('message', check=check, timeout=30)
    cost += 2
    await ctx.author.send(f"**Colour Has Been Set To: `{colorcode.content}`**")
    await ctx.author.send(f"**Now Let Us Concentrate On The Permissions For `{kkk}`!: **")
    await ctx.author.send("**[NOTE: Answer The Following Questions With `y` and `n`**")

    await ctx.author.send(f"**Is `{kkk} Seperately Viewable?: **")
    viewz = await client.wait_for('message', check=check, timeout=30)
    if viewz.content.lower() == 'y':
        await ctx.author.send(f"**`{kkk} Is Seperately Viewable!**")
        features.append("Seperate View")
        cost += 5
    elif viewz.content.lower() == 'n':
        pass
    else:
        await ctx.author.send("**Invalid Choice! Skipping...**")

    await ctx.author.send(f"**Is `{kkk}` Pingable By Anyone?: **")
    pinga = await client.wait_for('message', check=check, timeout=30)
    if pinga.content.lower() == 'y':
        await ctx.author.send(f"**`{kkk}` Is Pingable By Everyone!**")
    elif pinga.content.lower() == 'n':
        await ctx.author.send(f"**Noone Can Ping `{kkk}`!**")
        features.append("Unpingable")
        cost += 2
        pass
    else:
        await ctx.author.send("**Invalid Choice! Skipping...**")

    await ctx.author.send(f"**Can `{kkk}` View Audit Logs?: **")
    pinga = await client.wait_for('message', check=check, timeout=30)
    if pinga.content.lower() == 'y':
        await ctx.author.send(f"**`{kkk}` can View Audit Logs!**")
        features.append("Audit Logs")
        cost += 2
    elif pinga.content.lower() == 'n':
        pass
    else:
        await ctx.author.send("**Invalid Choice! Skipping...**")

    await ctx.author.send(f"**Can `{kkk}` View Server Insights?: **")
    si = await client.wait_for('message', check=check, timeout=30)
    if si.content.lower() == 'y':
        await ctx.author.send(f"**`{kkk}` Can View Server Insights!**")
        features.append("Server Insights")
        cost += 1
    elif si.content.lower() == 'n':
        await ctx.author.send(f"**`{kkk}` Cant View Server Insights!**")
    else:
        await ctx.author.send("**Invalid Choice! Skipping...**")

    await ctx.author.send(f"**Can `{kkk}` Manage Server?: **")
    ms = await client.wait_for('message', check=check, timeout=30)
    if ms.content.lower() == 'y':
        await ctx.author.send(f"**`{kkk}` Can Manage Server!**")
        features.append("Server Management")
        cost += 100
    elif ms.content.lower() == 'n':
        await ctx.author.send(f"**`{kkk}` Can't Manage Server!**")
    else:
        await ctx.author.send("**Invalid Choice! Skipping...**")

    await ctx.author.send(f"**Can `{kkk}` Manage Roles?: **")
    mr = await client.wait_for('message', check=check, timeout=30)
    if mr.content.lower() == 'y':
        await ctx.author.send(f"**`{kkk}` Can Manage Roles!**")
        features.append("Manage Roles")
        cost += 125
    elif mr.content.lower() == 'n':
        await ctx.author.send(f"**`{kkk}` Can't Manage Roles!**")
    else:
        await ctx.author.send("**Invalid Choice! Skipping...**")

    await ctx.author.send(f"**Can `{kkk}` Manage Channels?: **")
    mc = await client.wait_for('message', check=check, timeout=30)
    if mc.content.lower() == 'y':
        await ctx.author.send(f"**`{kkk}` Can Manage Channels!**")
        features.append("Manage Channels")
        cost += 50
    elif mc.content.lower() == 'n':
        await ctx.author.send(f"**`{kkk}` Can't Manage Channels!**")
    else:
        await ctx.author.send("**Invalid Choice! Skipping...**")

    await ctx.author.send("**Can Role Members Change Their Own NickName?: **")
    nn = await client.wait_for('message', check=check, timeout=30)
    if nn.content.lower() == 'y':
        await ctx.author.send("**Role Members Can Change Their Own NickName!**")
        features.append("Manage Own NickName")
        cost += 1
    elif nn.content.lower() == 'n':
        await ctx.author.send("**Role Members Can't Change Their Own NickName**")
    else:
        await ctx.author.send("**Invalid Choice! Skipping...**")

    await ctx.author.send("**Can Role Members Manage Others Nicknames?: **")
    mn = await client.wait_for('message', check=check, timeout=30)
    if mn.content.lower() == 'y':
        await ctx.author.send("**Role Members Can Manage Others Nicknames!**")
        features.append("Manage NickNames")
        cost += 5
    elif mn.content.lower() == 'n':
        await ctx.author.send("**Role Members Can't Manage Others NickNames!**")
    else:
        await ctx.author.send("**Invalid Choice! Skipping...**")

    await ctx.author.send("**Can Role Members Manage Emojis?: **")
    me = await client.wait_for('message', check=check, timeout=30)
    if me.content.lower() == 'y':
        await ctx.author.send("**Role Members Can Manage Emojis!**")
        features.append("Manage Emojis")
        cost += 2
    elif me.content.lower() == 'n':
        await ctx.author.send("**Role Members Can't Manage Emojis!**")
    else:
        await ctx.author.send("**Invalid Choice! Skipping...**")

    await ctx.author.send(f"**Can `{kkk}` Manage Messages?: **")
    mm = await client.wait_for('message', check=check, timeout=30)
    if mm.content.lower() == 'y':
        await ctx.author.send(f"**`{kkk}` Can Manage Messages!**")
        features.append("Manage Messages")
        cost += 3
    elif mm.content.lower() == 'n':
        await ctx.author.send(f"**`{kkk}` Members Can't Manage Message!**")
    else:
        await ctx.author.send("**Invalid Choice! Skipping...**")

    await ctx.author.send(f"**Can `{kkk}` Embeds Links?: **")
    el = await client.wait_for('message', check=check, timeout=30)
    if el.content.lower() == 'y':
        await ctx.author.send(f"**`{kkk}` Can Embed Links!**")
        features.append("Embed Links")
        cost += 3
    elif el.content.lower() == 'n':
        await ctx.author.send(f"**`{kkk}` Members Can't Embed Links!**")
    else:
        await ctx.author.send("**Invalid Choice! Skipping...**")

    await ctx.author.send(f"**Can `{kkk}` Attach Files?: **")
    af = await client.wait_for('message', check=check, timeout=30)
    if af.content.lower() == 'y':
        await ctx.author.send(f"**`{kkk}` Can Attach Files!**")
        features.append("Attach Files")
        cost += 3
    elif af.content.lower() == 'n':
        await ctx.author.send(f"**`{kkk}` Members Can't Attach Files!**")
    else:
        await ctx.author.send("**Invalid Choice! Skipping...**")

    await ctx.author.send(f"**Can `{kkk}` Use External Emojis And Add Reactions?: **")
    ee = await client.wait_for('message', check=check, timeout=30)
    if ee.content.lower() == 'y':
        await ctx.author.send(f"**`{kkk}` Can Use External Emojis And Add Reactions!**")
        features.append("External Emojis")
        features.append("Add Reactions")
        cost += 5
    elif ee.content.lower() == 'n':
        await ctx.author.send(f"**`{kkk}` Can't Use External Emojis And Add Reactions!**")
    else:
        await ctx.author.send("**Invalid Choice! Skipping...**")

    await ctx.author.send(f"**Can `{kkk}` Ping `Everyone` and `here`?: **")
    ee = await client.wait_for('message', check=check, timeout=30)
    if ee.content.lower() == 'y':
        await ctx.author.send(f"**`{kkk}` Can Ping everyone And here!**")
        features.append("Ping Everyone")
        features.append("Ping Here")
        cost += 60
    elif ee.content.lower() == 'n':
        await ctx.author.send(f"**`{kkk}` Can't Ping Everyone And Here!**")
    else:
        await ctx.author.send("**Invalid Choice! Skipping...**")

    await ctx.author.send(f"**Author Name: `{ctx.author.id}`**")
    await ctx.author.send(f"**Role Name: ``{kkk}``**")
    await ctx.author.send(f"**Role Colour: `{colorcode.content}`**")
    await ctx.author.send(f"**The Features Are: **")
    await ctx.author.send("**```" + str(features) + "```**")
    await ctx.author.send(f"**Total Cost Is: `{int(cost)}`**")

    await ctx.author.send(f"**`Pay `{int(cost)}` To ` https://paypal.me/togs66 `And Send Me The Image Of The Final Product To Recieve Your Role!`**")
