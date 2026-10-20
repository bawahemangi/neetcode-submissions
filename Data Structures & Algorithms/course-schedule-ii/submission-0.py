class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph={c:[] for c in range(numCourses)}

        for crs,pre in prerequisites:
            graph[crs].append(pre)
        output=[]
        cycle,seen=set(),set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in seen:
                return True
            cycle.add(crs)
            for pre in graph[crs]:
                if not dfs(pre): 
                    return False
            cycle.remove(crs)
            seen.add(crs)
            output.append(crs)
            return True

        for crs in range (numCourses):
            if dfs(crs)==False:
                return []
        return output