acceptableImageFormats = [".png",".jpg",".jpeg",".gif",".gifv",".webm",".mp4","imgur.com"]
memeHistory = deque()
memeSubreddits = ["dankmemes", "memes", "2meirl4meirl", "deepfriedmemes", "MemeEconomy", "", "okbuddyretard"]

async def getSub(ctx, sub):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.reddit.com/r{sub}/hot.json?limit=100") as response:
                request = await response.json()

        attempts = 1
        while attempts < 5:
            if 'error' in request:
                print("failed request {}".format(attempts))
                await asyncio.sleep(2)
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"https://www.reddit.com/r/{sub}/hot.json?limit=100") as response:
                        request = await response.json()
                attempts += 1
            else:
                index = 0

                for index, val in enumerate(request['data']['children']):
                    if 'url' in val['data']:
                        url = val['data']['url']
                        urlLower = url.lower()
                        accepted = False
                        for j, v, in enumerate(acceptableImageFormats): #check if it's an acceptable image
                            if v in urlLower:
                                accepted = True
                        if accepted:
                            if url not in memeHistory:
                                memeHistory.append(url)  #add the url to the history, so it won't be posted again
                                if len(memeHistory) > 63: #limit size
                                    memeHistory.popleft() #remove the oldest

                                break #done with this loop, can send image
                await ctx.send(memeHistory[len(memeHistory) - 1]) #send the last image
                return
        await ctx.send("_{}! ({})_".format(str(request['message']), str(request['error'])))

class SubredditFetcher(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @client.command()
    async def meme(ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.reddit.com/r/{0}/hot.json?limit=100".format(random.choice(memeSubreddits))) as response:
                request = await response.json()

        attempts = 1
        while attempts < 5:
            if 'error' in request:
                await asyncio.sleep(2)
                async with aiohttp.ClientSession() as session:
                    async with session.get("https://www.reddit.com/r/{0}/hot.json?limit=100".format(random.choice(memeSubreddits))) as response:
                        request = await response.json()
                attempts += 1
            else:
                index = 0

                for index, val in enumerate(request['data']['children']):
                    if 'url' in val['data']:
                        url = val['data']['url']
                        urlLower = url.lower()
                        accepted = False
                        for j, v, in enumerate(acceptableImageFormats): 
                            if v in urlLower:
                                accepted = True
                        if accepted:
                            if url not in memeHistory:
                                memeHistory.append(url)  
                                if len(memeHistory) > 63: 
                                    memeHistory.popleft() 

                                break 
                await ctx.send(memeHistory[len(memeHistory) - 1])
                return
        await ctx.send("_{}! ({})_".format(str(request['message']), str(request['error'])))
    
    @client.command()
    async def showerthought(ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://www.reddit.com/r/showerthoughts/hot.json?limit=100") as response:
                request = await response.json()

        attempts = 1
        while attempts < 5:
            if 'error' in request:
                await asyncio.sleep(2)
                async with aiohttp.ClientSession() as session:
                    async with session.get("https://www.reddit.com/r/showerthoughts/hot.json?limit=100") as response:
                        request = await response.json()
                attempts += 1
            else:
                index = 0

                for index, val in enumerate(request['data']['children']):
                    if 'title' in val['data']:
                        url = val['data']['title']
                        urlLower = url.lower()
                        accepted = False
                        if url == "What Is A Showerthought?":
                            accepted = False
                        elif url == "Showerthoughts is looking for new moderators!":
                            accepted = False
                        else:
                            accepted = True
                        if accepted:
                            if url not in memeHistory:
                                memeHistory.append(url)
                                if len(memeHistory) > 63:
                                    memeHistory.popleft()

                                break
                await ctx.send(memeHistory[len(memeHistory) - 1])
                return
        await ctx.send("_{}! ({})_".format(str(request['message']), str(request['error'])))

    nsfwSubreddits = ['collegesluts', 'CollegeAmateurs', 'collegensfw', 'CollegeInitiation', 'springbreakers', 'milf', 'MilfsAndHousewives', 'LegalTeens', 'Just18', 'youngporn', 'Barelylegal', 'barelylegalteens', 'YoungMalePorn', 'RealGirls', 'Amateur', 'PetiteGoneWild', 'homemadexxx', 'ChangingRooms', 'NSFW_Snapchat', 'NudeSelfies', 'GirlsWithiPhones', 'nsfwskirts', 'WeddingsGoneWild', 'assinthong', 'Bikini', 'bikinis', 'GirlsWearingVS', 'asshole', 'ass', 'SpreadEm', 'datgap', 'vagina']
    @client.command()
    async def nsfw(ctx):
        if ctx.channel.is_nsfw():
            async with aiohttp.ClientSession() as session:
                async with session.get("https://www.reddit.com/r/{0}/hot.json?limit=100".format(random.choice(nsfwSubreddits))) as response:
                    request = await response.json()

            attempts = 1
            while attempts < 5:
                if 'error' in request:
                    await asyncio.sleep(2)
                    async with aiohttp.ClientSession() as session:
                        async with session.get("https://www.reddit.com/r/{0}/hot.json?limit=100".format(random.choice(nsfwSubreddits))) as response:
                            request = await response.json()
                    attempts += 1
                else:
                    index = 0

                    for index, val in enumerate(request['data']['children']):
                        if 'url' in val['data']:
                            url = val['data']['url']
                            urlLower = url.lower()
                            accepted = False
                            for j, v, in enumerate(acceptableImageFormats): 
                                if v in urlLower:
                                    accepted = True
                            if accepted:
                                if url not in memeHistory:
                                    memeHistory.append(url)  
                                    if len(memeHistory) > 63: 
                                        memeHistory.popleft() 

                                    break 
                    await ctx.send(memeHistory[len(memeHistory) - 1])
                    return
            await ctx.send("_{}! ({})_".format(str(request['message']), str(request['error'])))
        else:
            await ctx.send("NONO HORNY = BAD :joy:")

    
    @client.command(aliases=['dankmeme', 'dank'])
    async def dankmemes(ctx):
        await getSub(ctx, 'dankmemes')
        
    @client.command()
    async def meirl(ctx):
        await getSub(ctx, 'me_irl')

    @client.command()
    async def coderjoke(ctx):
        await getSub(ctx, 'ProgrammerHumor')
