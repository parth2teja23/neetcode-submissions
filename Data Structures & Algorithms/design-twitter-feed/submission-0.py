class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set) # user -> (followers)
        self.tweetMap = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> list[int]:
        feed = self.tweetMap[userId][:]
        for followeeId in self.followMap[userId]:
            feed.extend(self.tweetMap[followeeId])
        heap = []
        for time, tweetId in feed:
            heapq.heappush(heap, (time, tweetId))
            if len(heap) > 10:
                heapq.heappop(heap)  # kicks out the oldest tweet
        result = []
        while heap:
            time, tweetId = heapq.heappop(heap)  # pops smallest first
            result.append(tweetId)

        result.reverse()  # flip to get newest first
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followerId == followeeId:
            self.followMap[followerId].add(followeeId)
            

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
        
        


