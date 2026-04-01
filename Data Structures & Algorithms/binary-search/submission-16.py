class Solution:
    def search(self, nums: List[int], target: int) -> int:
        seen = {}
        for i , num in enumerate(nums):
            if target == num:
                return i
            seen[num] = i
        return -1
        
        
          
            
        
        
