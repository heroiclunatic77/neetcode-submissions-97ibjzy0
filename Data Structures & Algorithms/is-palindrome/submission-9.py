class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ''
        for a in s:
            if a.isalnum():
                newstr += a.lower()
        if newstr == newstr[::-1]:
            return True
        else:
            return False
        