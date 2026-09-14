class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        max_freq=max(freq.values())
        max_count=0
        for count in freq.values():
            if max_freq==count:
                max_count+=1
        res=(max_freq-1)*(n+1)+max_count
        return max(len(tasks),res)
