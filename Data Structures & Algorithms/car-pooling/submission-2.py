class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t:t[1])
        curr=0
        minheap=[]
        for t in trips:
            passNo,start,end=t
            while minheap and minheap[0][0]<=start:
                curr-=minheap[0][1]
                heapq.heappop(minheap)
                
            curr+=passNo
            if curr>capacity:
                return False
            heapq.heappush(minheap,(end,passNo))
        return True