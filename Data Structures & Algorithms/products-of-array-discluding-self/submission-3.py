class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = []
        arr_product = 1

        for i, n in enumerate(nums):
            if n == 0:
                zeroes.append(i)
            else:
                arr_product *= n
        
        if len(zeroes) > 1:
            return [0]*len(nums)
        
        res = []
        for i, n in enumerate(nums):
            if i in zeroes:
                res.append(arr_product)
            else:
                if zeroes:
                    res.append(0)
                else:
                    res.append(int(arr_product / n))
        
        return res
