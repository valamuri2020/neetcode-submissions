class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # a + b = -c
        # sorting
        # fix a, two sum over b,c
        # two sum over sorted array, so use pointers
        # update pointers smartly

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append(
                        [a, nums[l], nums[r]]
                    )
                    l+=1
                    while l < r and nums[l-1] == nums[l]:
                        l+=1
            
        return res
        