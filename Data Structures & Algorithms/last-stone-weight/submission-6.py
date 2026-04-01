class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones  = sorted(stones)
        while len(stones)> 1:
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            else:
                new = stones[-1] - stones[-2]
                stones.pop()
                stones.pop()
                stones.append(new)
                stones = sorted(stones)
        if not stones:
            return 0
        else:
            return stones[0]
