class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fin = []
        
        for i, num in enumerate(nums):
            temp = nums[:i] + nums[i+1:]
            result = 1
            for n in temp:
                
                result  = result * n
            fin.append(result)
        return fin



            

