class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res,cur=[],[]
        def dfs():
            if len(cur)==len(nums):
                res.append(cur[:])
            for num in nums:
                if num not in cur:
                    cur.append(num)
                    dfs()
                    cur.pop()
        dfs()
        return res