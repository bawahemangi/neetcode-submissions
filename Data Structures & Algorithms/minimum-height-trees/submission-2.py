class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return[0]
        graph=defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        degree=[len(graph[i]) for i in range(n)]

        q=deque()

        for i in range(n):
            if degree[i]==1:
                q.append(i)

        rem=n
        

        while rem>2:
            size=len(q)
            rem-=size
            for _ in range(size):
                node=q.popleft()
                for neigh in graph[node]:
                    degree[neigh]-=1
                    if degree[neigh]==1:
                        q.append(neigh)

        return list(q)
                