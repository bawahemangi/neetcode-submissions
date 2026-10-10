class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        res = 0
        l = 0
        for i in range(l, len(nums)):
            if nums[i]<nums[l]:
                l=i
            else:
                diff=nums[i]-nums[l]
                res=max(res,diff)

        return res
