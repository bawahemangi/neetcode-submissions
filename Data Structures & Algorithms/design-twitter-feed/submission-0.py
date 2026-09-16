class Twitter:

    def __init__(self):
        self.time=0
        self.following=defaultdict(set)
        self.tweets=defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweets[userId].append((self.time,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        users=self.following[userId]|{userId}
        for user in users:
            if user in self.tweets and self.tweets[user]:
                index=len(self.tweets[user])-1
                time,tweetId=self.tweets[user][index]
                heapq.heappush(heap,(-time,tweetId,user,index))
        res=[]
        while heap and len(res)<10:
            negTime,tweetId,user,index=heapq.heappop(heap)
            res.append(tweetId)
            index-=1
            if index>=0:
                time,tweetId=self.tweets[user][index]
                heapq.heappush(heap,(-time,tweetId,user,index))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
