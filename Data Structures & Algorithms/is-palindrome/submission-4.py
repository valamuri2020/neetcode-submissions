class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = len(s)-1
        l, r = 0, n
        

        while l <= r:
            while not s[l].isalnum() and l < n:
                l+=1
            while not s[r].isalnum() and r >= 0:
                r-=1
            
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        

        return True