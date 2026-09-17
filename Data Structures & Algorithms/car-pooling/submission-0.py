class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes=[0]*1000
        for t in trips:
            passNo,start,end=t
            changes[start]+=passNo
            changes[end]-=passNo
        curr=0
        for i in range(1000):
            curr+=changes[i]
            if curr>capacity:
                return False
        return True
