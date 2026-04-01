class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = ''
        for char in s:
            if char.isalnum():
                str+= char.lower()
        left = 0
        right = len(str)-1
        while left<right:
            if str[left] != str[right]:
                return False
            else:
                left+=1
                right -=1
        return True
        
