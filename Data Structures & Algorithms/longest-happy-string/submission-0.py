class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res,maxheap='',[]
        for cnt,char in [(-a,'a'),(-b,'b'),(-c, 'c')]:
            if cnt!=0:
                heapq.heappush(maxheap,(cnt,char))
        while maxheap:
            cnt,char=heapq.heappop(maxheap)
            if len(res)>1 and res[-1]==res[-2]==char:
                if not maxheap:
                    break
                cnt2,char2=heapq.heappop(maxheap)
                res+=char2
                cnt2+=1
                if cnt2:
                    heapq.heappush(maxheap,(cnt2,char2))
            else:
                res+=char
                cnt+=1
            if cnt:
                heapq.heappush(maxheap,(cnt,char))
        return res
            
