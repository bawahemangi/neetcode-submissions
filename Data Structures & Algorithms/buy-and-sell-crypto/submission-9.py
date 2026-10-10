class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        res=0
        min_price=nums[0]
        for price in nums:
            min_price=min(price,min_price)
            profit=price-min_price
            res=max(res,profit)

        return res
