class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp={}
        def dfs(i,rem):
            if rem==0:
                return 1
            if i==len(coins) or rem<0:
                return 0
            if (i,rem) in dp:
                return dp[(i,rem)]
            pick=dfs(i,rem-coins[i])
            keep=dfs(i+1,rem)
            dp[(i,rem)]=keep+pick

            return dp[(i,rem)]
        return dfs(0,amount)
