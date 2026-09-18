class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxheap=[]
        projects=sorted(zip(capital,profits))
        i=0
        for _ in range(k):
            while i<len(projects) and  projects[i][0]<=w:
                heapq.heappush(maxheap,-projects[i][1])
                i+=1
            if not maxheap:
                break
            w+=-heapq.heappop(maxheap)
        return w