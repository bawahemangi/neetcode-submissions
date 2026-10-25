class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph=[[False]*numCourses for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[a][b]=True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if graph[i][k] and graph[k][j]:
                        graph[i][j]=True
        
        ans=[]
        for a,b in queries:
            ans.append(graph[a][b])

        return ans

