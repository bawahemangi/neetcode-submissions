class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res,path=[],[]
        def dfs(i):
            if not digits:
                return []

            if i==len(digits):
                res.append(''.join(path))
                return
            for ch in mp[digits[i]]:
                path.append(ch)
                dfs(i+1)
                path.pop()
        dfs(0)
        return res
