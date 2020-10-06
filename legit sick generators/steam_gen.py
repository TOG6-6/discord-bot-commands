#none of these programs will really generate anything, I AM AGAINST ANYTHING ILLEGAL And the only purpose of this is to make your bot more interesting
import steam as wa #pip install steam
@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def steam(ctx):
    await ctx.send("***SENDING 1 Steam Code!***")
    await ctx.send("`MAKE SURE DMs ARE OPEN!`")
    await ctx.send("10 second cooldown has begun for user: " + ctx.author.mention)
    def bla():
        codelen = 5
        bros = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        return ''.join(random.choice(bros) for i in range(codelen))

    def blb():
        codelen = 5
        bros = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        return ''.join(random.choice(bros) for i in range(codelen))

    def blc():
        codelen = 5
        bros = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        return ''.join(random.choice(bros) for i in range(codelen))
    
    for i in range(1):
        repping = (bla() + "-" + blb() + "-" + blc())
        await ctx.author.send("The Code Generated is: " + repping)
        await ctx.author.send("Checking...")

    p = 'username'
    b = 'password'
    user = wa.WebAuth(p, b)
    
    try:
        user.login()
    except wa.CaptchaRequired:
        await ctx.send("STRANGE ERROR!")
    except wa.EmailCodeRequired:
        code = input("Please enter emailed 2FA code:\n")
        user.login(email_code=code)

    sessionID = user.session.cookies.get_dict()["sessionid"]

    r = user.session.post('https://store.steampowered.com/account/ajaxregisterkey/', data={'product_key' : repping, 'sessionid' : sessionID})
    blob = json.loads(r.text)

    if blob["success"] == 1:
        for item in blob["purchase_receipt_info"]["line_items"]:
            await ctx.author.send("[ Redeemed ]", item["line_item_description"])
    else:
# Error codes from https://steamstore-a.akamaihd.net/public/javascript/registerkey.js?v=qQS85n3B1_Bi&l=english
        errorCode = blob["purchase_result_details"]
        sErrorMessage = ""
        if errorCode == 14:
            await ctx.author.send("**The product code you\'ve entered is not valid. Please double check to see if you\'ve mistyped your key. I, L, and 1 can look alike, as can V and Y, and 0 and O.**")

        elif errorCode == 15:
            await ctx.author.send("**The product code you\'ve entered has already been activated by a different Steam account. This code cannot be used again. Please contact the retailer or online seller where the code was purchased for assistance.**")

        elif errorCode == 53:
            await ctx.author.send("**Please TRY This Code Manually!**")

        elif errorCode == 13:
            await ctx.author.send("**Sorry, but this product is not available for purchase in this country. Your product key has not been redeemed.**")

        elif errorCode == 9:
            await ctx.author.send("**This Steam account already owns the product(s) contained in this offer. To access them, visit your library in the Steam client.**")

        elif errorCode == 24:
            await ctx.author.send("**The product code you\'ve entered requires ownership of another product before activation.\n\nIf you are trying to activate an expansion pack or downloadable content, please first activate the original game, then activate this additional content.**")

        elif errorCode == 36:
            await ctx.author.send("**The product code you have entered requires that you first play this game on the PlayStation®3 system before it can be registered.\n\nPlease:\n\n- Start this game on your PlayStation®3 system\n\n- Link your Steam account to your PlayStation®3 Network account\n\n- Connect to Steam while playing this game on the PlayStation®3 system\n\n- Register this product code through Steam.**")

        elif errorCode == 50: 
            await ctx.author.send("**The code you have entered is from a Steam Gift Card or Steam Wallet Code. Browse here: https://store.steampowered.com/account/redeemwalletcode to redeem it.**")

        else:
            await ctx.author.send("**An unexpected error has occurred.  Your product code has not been redeemed.  Please wait 30 minutes and try redeeming the code again.  If the problem persists, please contact <a href='https://help.steampowered.com/en/wizard/HelpWithCDKey'>Steam Support</a> for further assistance.**")

@client.command()
@commands.has_role("Server Sponsors")
@commands.cooldown(1, 10, commands.BucketType.user)
async def steamcheck(ctx, code):
    await ctx.send("***Checking...***")
    time.sleep(3)
    await ctx.send("***Check Your DMs!***")
    p = 'username'
    b = 'password'
    user = wa.WebAuth(p, b)
    
    try:
        user.login()
    except wa.CaptchaRequired:
        await ctx.send("STRANGE ERROR!")
    except wa.EmailCodeRequired:
        code = input("Please enter emailed 2FA code:\n")
        user.login(email_code=code)

    sessionID = user.session.cookies.get_dict()["sessionid"]

    r = user.session.post('https://store.steampowered.com/account/ajaxregisterkey/', data={'product_key' : code, 'sessionid' : sessionID})
    blob = json.loads(r.text)

    if blob["success"] == 1:
        for item in blob["purchase_receipt_info"]["line_items"]:
            await ctx.author.send("[ Redeemed ]", item["line_item_description"])
    else:
# Error codes from https://steamstore-a.akamaihd.net/public/javascript/registerkey.js?v=qQS85n3B1_Bi&l=english
        errorCode = blob["purchase_result_details"]
        sErrorMessage = ""
        if errorCode == 14:
            await ctx.author.send("**The product code you\'ve entered is not valid. Please double check to see if you\'ve mistyped your key. I, L, and 1 can look alike, as can V and Y, and 0 and O.**")

        elif errorCode == 15:
            await ctx.author.send("**The product code you\'ve entered has already been activated by a different Steam account. This code cannot be used again. Please contact the retailer or online seller where the code was purchased for assistance.**")

        elif errorCode == 53:
            await ctx.author.send("The product code you\'ve entered is not valid. Please double check to see if you\'ve mistyped your key. I, L, and 1 can look alike, as can V and Y, and 0 and O.")

        elif errorCode == 13:
            await ctx.author.send("**Sorry, but this product is not available for purchase in this country. Your product key has not been redeemed.**")

        elif errorCode == 9:
            await ctx.author.send("**This Steam account already owns the product(s) contained in this offer. To access them, visit your library in the Steam client.**")

        elif errorCode == 24:
            await ctx.author.send("**The product code you\'ve entered requires ownership of another product before activation.\n\nIf you are trying to activate an expansion pack or downloadable content, please first activate the original game, then activate this additional content.**")

        elif errorCode == 36:
            await ctx.author.send("**The product code you have entered requires that you first play this game on the PlayStation®3 system before it can be registered.\n\nPlease:\n\n- Start this game on your PlayStation®3 system\n\n- Link your Steam account to your PlayStation®3 Network account\n\n- Connect to Steam while playing this game on the PlayStation®3 system\n\n- Register this product code through Steam.**")

        elif errorCode == 50: 
            await ctx.author.send("**The code you have entered is from a Steam Gift Card or Steam Wallet Code. Browse here: https://store.steampowered.com/account/redeemwalletcode to redeem it.**")

        else:
            await ctx.author.send("**An unexpected error has occurred.  Your product code has not been redeemed.  Please wait 30 minutes and try redeeming the code again.  If the problem persists, please contact <a href='https://help.steampowered.com/en/wizard/HelpWithCDKey'>Steam Support</a> for further assistance.**")