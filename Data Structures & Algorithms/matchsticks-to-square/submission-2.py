class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total=sum(matchsticks)
        if total%4!=0:
            return False
        target=total//4
        part=[0]*4
        matchsticks.sort(reverse=True)

        def dfs(i):
            
            if i==len(matchsticks):
                return True
            stick=matchsticks[i]
            for j in range(4):
                if part[j]+stick<=target:
                    part[j]+=stick
                    if dfs(i+1):
                        return True
                    part[j]-=stick
            return False
        return dfs(0)
        
                    

