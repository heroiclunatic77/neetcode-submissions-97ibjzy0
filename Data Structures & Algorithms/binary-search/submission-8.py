class Solution:
    def search(self, nums: List[int], target: int) -> int:
        seen = {}
        for i, num in enumerate(nums):
            if target == num:
                return i
            if target in seen:
                return seen[target]
            else:
                seen[num] = i
        return -1
