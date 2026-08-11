class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping = {']': '[', '}': '{', ')': '('}

        for ch in s:
            if ch in '[({':
                stack.append(ch)

            else:
                if not stack or mapping[ch]!=stack[-1]:
                    return False
                stack.pop()

        return not stack
