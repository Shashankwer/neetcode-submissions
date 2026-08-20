class Twitter:

    def __init__(self):
        self.tweets = {}
        self.follows = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        if userId not in self.tweets:
            self.tweets[userId] = [(-self.time,tweetId)]
            self.follows[userId] = [userId]
        else:
            heapq.heappush(self.tweets[userId], (-self.time,tweetId))
    
    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        for user in self.follows.get(userId,[]):
            tweets+=self.tweets.get(user,[])
        heapq.heapify(tweets)
        tweets_to_return = []
        for _ in range(10):
            if len(tweets):
                tweets_to_return.append(heapq.heappop(tweets)[1])
            else:
                break
        return tweets_to_return

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = [followerId]
        if followerId in self.follows:
            if followeeId not in self.follows[followerId]:
                self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            if followeeId in self.follows[followerId] and followeeId != followerId:
                self.follows[followerId].remove(followeeId)

