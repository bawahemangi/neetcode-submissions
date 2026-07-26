class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        l=self.sortArray(nums[:mid])
        r=self.sortArray(nums[mid:])

        return self.merge(l,r)

    def merge(self, l, r):
        result=[]
        i=0
        j=0

        while i<len(l) and j<len(r):
            if l[i]<=r[j]:
                result.append(l[i])
                i+=1
            else:
                result.append(r[j])
                j+=1
        
        while i< len(l):
            result.append(l[i])
            i+=1
        while j< len(r):
            result.append(r[j])
            j+=1

        return result




    
