class FreqStack:

    def __init__(self):
        self.maxcnt=0
        self.stacks={}
        self.freq={}

    def push(self, val: int) -> None:
        valcnt=1+self.freq.get(val,0)
        self.freq[val]=valcnt
        if valcnt> self.maxcnt:
            self.maxcnt=valcnt
            self.stacks[valcnt]=[]
        self.stacks[valcnt].append(val)
    
    def pop(self) -> int:
        res=self.stacks[self.maxcnt].pop()
        self.freq[res]-=1
        if not self.stacks[self.maxcnt]:
            self.maxcnt-=1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()