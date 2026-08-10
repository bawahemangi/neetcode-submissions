class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        freq={0:1}
        curSum=0
        for num in nums:
            curSum+=num
            diff=curSum-k
            res+= freq.get(diff,0)
            freq[curSum]=1+freq.get(curSum,0)

        return res