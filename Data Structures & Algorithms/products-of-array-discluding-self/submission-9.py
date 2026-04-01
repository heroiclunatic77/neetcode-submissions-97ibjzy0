class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            temp = nums[:i] + nums[i+1:]
            m = 1
            for n in temp:
                m = m*n
            res.append(m)
        return res
