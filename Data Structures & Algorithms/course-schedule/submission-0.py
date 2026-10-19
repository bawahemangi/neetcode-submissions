class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]

        for a,b in prerequisites:
            graph[a].append(b)
        visit=set()
        def dfs(a):
            if graph[a]==[]:
                return True
            if a in visit:
                return False
            visit.add(a)
            for b in graph[a]:
                if not dfs(b):  return False
            visit.remove(a)
            graph[a]=[]
            return True
        for a in range(numCourses):
            if not dfs(a): return False
        return True

