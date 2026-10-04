class TrieNode:
    def __init__(self):
        self.children={}
        self.endword=False

class Trie:
    def __init__(self,word):
        self.root=TrieNode()
        for w in word:
            cur=self.root
            for c in w:
                if c not in cur.children:
                    cur.children[c]=TrieNode()
                cur=cur.children[c]
            cur.endword=True
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp={len(s):0}
        trie=Trie(dictionary).root
        def dfs(i):
            if i in dp:
                return dp[i]

            res=1+dfs(i+1)
            cur=trie
            for j in range(i, len(s)):
                if s[j] not in cur.children:
                    break
                cur=cur.children[s[j]]
                if cur.endword:
                    res=min(res,dfs(j+1))
            dp[i]=res
            return res
        return dfs(0)
            

        