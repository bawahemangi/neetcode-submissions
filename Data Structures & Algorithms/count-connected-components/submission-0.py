class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent= list(range(n))
        count=n
        rank=[1]*n
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(u,v):
            nonlocal count
            roor_u=find(u)
            roor_v=find(v)

            if roor_u==roor_v:
                return 
            if rank[roor_u]<rank[roor_v]:
                roor_u,roor_v=roor_v,roor_u
            parent[roor_v]=roor_u
            rank[roor_u]+=roor_v

            count-=1

            
                
        for u,v in edges:
            union(u,v)

        return count
