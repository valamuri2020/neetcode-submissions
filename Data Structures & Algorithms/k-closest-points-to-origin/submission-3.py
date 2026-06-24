class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def euclidian2DToOrigin(x, y):
            return (x ** 2 + y ** 2) ** 0.5
        
        minHeap = []
        
        for point in points:
            distToOrigin = euclidian2DToOrigin(point[0], point[1])
            if len(minHeap) == k:
                heapq.heappushpop(minHeap, (-distToOrigin, point))
            else:
                heapq.heappush(minHeap, (-distToOrigin, point))
        

        res = []
        while minHeap:
            distToOrigin, point = heapq.heappop(minHeap)
            res.append(point)
        
        return res




