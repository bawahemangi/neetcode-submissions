class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r=max(nums),sum(nums)

        while l<r:
            m=(l+r)//2

            currsum=0
            subarray=1

            for n in nums:
                if currsum+n>m:
                    subarray+=1
                    currsum=n
                else:
                    currsum+=n

            if subarray<=k:
                r=m
            else:
                l=m+1
        return l


                

