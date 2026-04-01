class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lis = []
        for i in nums:
            if i not in lis:
                lis.append(i)
            else:
                return True
        return False

