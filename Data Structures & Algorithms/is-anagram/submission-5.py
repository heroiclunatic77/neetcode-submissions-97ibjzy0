class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = {}
        count2 = {}
        for i in s:
            count1[i] = count1.get(i,0)+1

        for a in t:
            count2[a] = count2.get(a,0)+1

        if count1 == count2:
            return True
        else:
            return False

            