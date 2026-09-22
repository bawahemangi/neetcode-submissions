class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res,cur=[],[]
        count={n:0 for n in nums}
        for n in nums:
            count[n]+=1
        def dfs():
            if len(cur)==len(nums):
                res.append(cur[:])
                return
            for n in count:
                if count[n]>00:
                    cur.append(n)
                    count[n]-=1
                    dfs()
                    cur.pop()
                    count[n]+=1
        dfs()
        return res

