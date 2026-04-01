class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ''
        for i in s:
            if i.isalnum():
                newstr = newstr + i.lower()
        if newstr == newstr[::-1]:
            return True
        else:
            return False
        
        
            
