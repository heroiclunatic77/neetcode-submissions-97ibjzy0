class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix  = [1]*len(nums)
        suffix  = [1]*len(nums)

        for i in range(len(nums)-1):
            prefix[i+1] = prefix[i]*nums[i]
        
        for i in range(len(nums)-1, 0,-1):
            suffix[i-1] = suffix[i]*nums[i]
        
        op = []
        for i in range(len(nums)):
            op.append(prefix[i]*suffix[i])
        return op
