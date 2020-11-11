#let me explain, just a tiny inch of logic in here, understand it, and then copy paste my guy!

#remember this can cause ratelimits, so will be a tiny inch slow if you're server is a fast growing one!

#first we use the on_member_join event to get the user info
@client.event
async def on_member_join(member):
    gaynelson = client.get_guild(763626880775225384) #the bot gets my guild with the id, change this to your guild id
    chanelson = gaynelson.get_channel(765802545858740264) #from there it searches for the voice channel with channel id, change the id agn
    users = (gaynelson.member_count) #this counts the number of users
    arb = int(users)
    nask = "Members: " + str(arb) #this is basically saying Members: number of members, doing this so we can change voice channel name
    await chanelson.edit(name=nask) #changing the voice channels name
    guild = client.get_guild(763626880775225384) #same getting the guild
    channel = guild.get_channel(765805688529747989) #getting second voice channel
    newname = "Latest Joiner: " + str(member) #prints the latest joiner
    await channel.edit(name=newname) #changes the voice channels name to the latest joiner!
    
#now we will write the code to update the number of members incase someone leaves the server!
@client.event
async def on_member_remove(member):
    gaynelson = client.get_guild(763626880775225384)
    chanelson = gaynelson.get_channel(765802545858740264)
    users = (gaynelson.member_count)
    arb = int(users)
    nask = "Members: " + str(arb)
    await chanelson.edit(name=nask)
