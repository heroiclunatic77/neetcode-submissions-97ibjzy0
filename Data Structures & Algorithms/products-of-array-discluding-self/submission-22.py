class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            temp = nums[:i] + nums[i+1:]
            mul = 1
            for n in temp:
                mul = mul*n
            res.append(mul)
        return res

