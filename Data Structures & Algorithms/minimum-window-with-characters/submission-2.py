from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # s = "abccccdeafxxxxedf"  t="fed"
        if len(s) < len(t): return ""

        t_freq = Counter(t)
        minString = None
        minStringLength = float('inf')

        window_freq = {}
        l = 0
        for r in range(len(s)):
            window_freq[s[r]] = window_freq.get(s[r], 0) + 1
            
            while self.satisfies(window_freq, t_freq):
                if (r-l+1) < minStringLength:
                    minString = [l, r]
                    minStringLength = r-l+1
                
                window_freq[s[l]] -= 1
                l+=1
        
        if minString:
            l, r = minString[0], minString[1]
            return s[l:r+1]
        
        return ""
    
    def satisfies(self, window_freq, needed_freq) -> bool:
        for char, freq in needed_freq.items():
            if window_freq.get(char, 0) < freq:
                return False
        
        return True



        
        
