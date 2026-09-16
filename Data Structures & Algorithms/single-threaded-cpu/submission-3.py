class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)
        tasks.sort(key= lambda t:t [0])
        i,t=0, tasks[0][0]
        minheap,res=[],[]
        while minheap or i<len(tasks):
            while i<len(tasks) and t>=tasks[i][0]:
                heapq.heappush(minheap,[tasks[i][1],tasks[i][2]])
                i+=1
            if not minheap:
                t=tasks[i][0]
            else:
                procTime,index=heapq.heappop(minheap)
                res.append(index)
                t+=procTime
        return res
