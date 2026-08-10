class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing=1
        nums.sort()
        for n in nums:
            if n>0 and missing==n:
                missing+=1

        return missing
    