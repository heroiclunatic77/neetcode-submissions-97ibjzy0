class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right  = len(heights)-1
        area = 0
        while left<right:
            breath = right-left
            height = min(heights[left], heights[right])
            a = breath * height
            if a > area:
                area  =  a
            if heights[left]<heights[right]:
                left+=1
            elif heights[left] == heights[right]:
                left+=1
            elif heights[left]>heights[right]:
                right-=1
        return area



        