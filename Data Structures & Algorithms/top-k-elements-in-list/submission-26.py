class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count  = {}
        for num in nums:
            count[num] = count.get(num,0)+1

        freq = [[] for _ in range(len(nums)+1)]

        for key,value in count.items():
            freq[value].append(key)
        
        op=[]
        for i in range(len(freq)-1, 0,-1):
            for num in freq[i]:
                op.append(num)
                if len(op)==k:
                    return op

