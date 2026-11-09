class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxcur,mincur=1,1
        res=max(nums)
        for n in nums:
            if n==0:
                maxcur,mincur=1,1
                continue
            temp=maxcur*n
            maxcur=max(maxcur*n,n,mincur*n)
            mincur=min(temp,n,mincur*n)
            res=max(res,maxcur)
        return res