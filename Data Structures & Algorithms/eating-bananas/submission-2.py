import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k: 1...max(piles), binary search instead of linear search
        def satisfies(k):
            if k == 0:
                return False
                
            total_h = 0
            for p in piles:
                total_h += math.ceil(p / k)
            
            if total_h <= h:
                return True
            
            return False
        
        max_piles = max(piles)
        
        l, r = 0, max_piles
        best_k = -1
        while l <= r:
            k = (l + r) // 2
            if satisfies(k):
                best_k = k
                r = k-1
            else:
                l = k+1
        
        return best_k
