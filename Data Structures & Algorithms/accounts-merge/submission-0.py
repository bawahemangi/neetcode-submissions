class unionfind:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[1]*n
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,a,b):
        p1=self.find(a)
        p2=self.find(b)
        if p1==p2:
            return False
        if self.parent[p1]>self.parent[p2]:
            self.parent[p2]=p1
            self.rank[p1]+=self.rank[p2]
        else:
            self.parent[p1]=p2
            self.rank[p2]+=self.rank[p1]
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf=unionfind(len(accounts))

        emailAcc={}
        for i,a in enumerate(accounts):
            for e in a[1:] :
                if e in emailAcc:
                    uf.union(i,emailAcc[e])
                else:
                    emailAcc[e]=i
        
        emailgraph=defaultdict(list)
        for e, i in emailAcc.items():
            leader=uf.find(i)
            emailgraph[leader].append(e)

        res=[]
        for i,e in emailgraph.items():
            name=accounts[i][0]
            res.append([name]+sorted(emailgraph[i]))
        return res





