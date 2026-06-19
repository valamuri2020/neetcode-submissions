class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        bestArea = -1

        while l < r:
            rightHeight, leftHeight = heights[r], heights[l]
            curArea = (r-l) * min(rightHeight, leftHeight)
            bestArea = max(bestArea, curArea)

            if leftHeight <= rightHeight:
                l += 1
            else:
                r -= 1
        
        
        return bestArea