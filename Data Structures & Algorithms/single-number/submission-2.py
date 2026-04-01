class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1
        for key, val in count.items():
            if val == 1:
                return key

