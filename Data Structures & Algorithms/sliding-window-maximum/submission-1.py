import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        l, r = 0, 0
        res = []
        
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
            r+=1
        
        res.append(-heap[0][0])

        for r in range(k, len(nums)):
            heapq.heappush(heap, (-nums[r], r))
            l+=1

            while not (l <= heap[0][1] <= r):
                heapq.heappop(heap)
            
            maxWindowVal = -heap[0][0]
            res.append(maxWindowVal)
        
        return res