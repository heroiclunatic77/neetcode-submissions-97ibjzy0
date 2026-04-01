class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fin = []
        for i in range(len(nums)):
            temp = nums[:i] + nums[i+1:]  # all elements except index i
            result = 1
            for n in temp:
                result *= n
            fin.append(result)
        return fin


            

