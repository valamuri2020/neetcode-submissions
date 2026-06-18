from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_indices = defaultdict(list)
        for i, c in enumerate(s):
            char_indices[c].append(i)
        
        min_index = float('inf')
        for c, indices in char_indices.items():
            if len(indices) > 1:
                continue
            
            min_index = min(min_index, indices[0])
        
        return -1 if min_index == float('inf') else min_index