class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total=sum(nums)
        if total%k!=0:
            return False
        target=total//k
        part=[0]*k
        nums.sort(reverse=True)
       
        def dfs(i):
            if i ==len(nums):
                return True
            num=nums[i]
            seen=set()
            for j in range (k):
                if part[j] in seen:
                    continue
                if part[j]+num<=target:
                    seen.add(part[j])
                    part[j]+=num
                    if dfs(i+1):
                        return True
                    part[j]-=num
            return False
        return dfs(0)