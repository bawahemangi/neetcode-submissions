class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ans=set()
        for i in range(len(nums)):
            if nums[i] in ans:
                return True
            ans.add(nums[i])

            if len(ans)>k:
                ans.remove(nums[i-k])
        return False

        
