class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph={}
        for (a,b),val in zip(equations,values):
            graph.setdefault(a,[]).append((b,val))
            graph.setdefault(b,[]).append((a,1/val))

        def dfs(src,dest,visited):
            if src not in graph or dest not in graph:
                return -1.0
            elif src==dest:
                return 1.0

            visited.add(src)
            for neigh, weight in graph[src]:
                if neigh not in visited:
                    res=dfs(neigh,dest,visited)
                    if res!=-1.0:
                        return weight*res

            return -1.0

        ans=[]

        for a,b in queries:
            ans.append(dfs(a,b,set()))
        return ans

