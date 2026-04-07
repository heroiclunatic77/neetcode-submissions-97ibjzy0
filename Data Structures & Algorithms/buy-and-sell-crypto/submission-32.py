class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l+1
        profit = 0
        while r<=len(prices)-1:
            if prices[l]>prices[r]:
                l =r
                r=r+1
            else:
                p = prices[r]-prices[l]
                profit = max(profit,p)
                r=r+1
        return profit
