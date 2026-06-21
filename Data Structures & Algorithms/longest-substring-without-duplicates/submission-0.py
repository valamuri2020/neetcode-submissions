class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        longest = -1
        cur_letters = defaultdict(int)
        l = 0

        for r in range(len(s)):
            while cur_letters[s[r]] > 0:
                cur_letters[s[l]] -= 1
                l += 1
            
            longest = max(r-l+1, longest)
            cur_letters[s[r]] += 1
        
        return longest


