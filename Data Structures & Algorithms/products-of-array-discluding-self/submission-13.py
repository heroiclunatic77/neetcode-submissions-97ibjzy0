class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(n-1):
            prefix[i+1] = prefix[i] * nums[i]

        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        final = []
        for i in range(n):
            final.append(prefix[i] * suffix[i])

        return final  


