class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=0
        pali=''

        for i in range(len(s)):
            # odd length
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>res:
                    pali=s[l:r+1]
                    res=r-l+1
                l-=1
                r+=1
            
            # even length
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>res:
                    pali=s[l:r+1]
                    res=r-l+1
                l-=1
                r+=1

        return pali