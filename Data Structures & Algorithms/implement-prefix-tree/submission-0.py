class TrieNode:
    def __init__(self):
        self.childern={}
        self.endofWord=False

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.childern:
                cur.childern[c]=TrieNode()
            cur=cur.childern[c]
        cur.endofWord=True

    def search(self, word: str) -> bool:
        cur=self.root
        for c in word:
            if c not in cur.childern:
                return False
            cur=cur.childern[c]
        return cur.endofWord

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for c in prefix:
            if c not in cur.childern:
                return False
            cur=cur.childern[c]
        return True
        
        