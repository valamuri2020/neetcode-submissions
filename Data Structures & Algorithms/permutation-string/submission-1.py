from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_freq = Counter(s1)
        s2_freq = {}

        for i in range(len(s1)):
            s2_freq[s2[i]] = s2_freq.get(s2[i], 0) + 1
        
        if s1_freq == s2_freq:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            s2_freq[s2[r]] = s2_freq.get(s2[r], 0) + 1
            
            s2_freq[s2[l]] -= 1
            
            if s2_freq[s2[l]] == 0:
                del s2_freq[s2[l]]
            
            l += 1
            
            if s1_freq == s2_freq:
                return True
            
        return False