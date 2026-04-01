class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = ""
        for char in s:
            if char.isalnum():
                strs+=char.lower()
        left = 0
        right = len(strs)-1

        while left<right:
            if strs[left]!=strs[right]:
                return False
            else:
                left+=1
                right -=1
        return True
