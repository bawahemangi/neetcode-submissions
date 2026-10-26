class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=list(range(len(edges)+1))

        def find(x):
            if x!=  parent[x]:
                parent[x]=find(parent[x])
            return parent[x]

        for u,v in edges:
            rootu=find(u)
            rootv=find(v)

            if rootu==rootv:
                return [u,v]

            parent[rootu]=rootv
                
