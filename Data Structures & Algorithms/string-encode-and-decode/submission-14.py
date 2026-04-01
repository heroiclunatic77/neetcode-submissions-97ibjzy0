class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""
        for s in strs:
            en += str(len(s)) + "#" + s
        return en

    def decode(self, s: str) -> List[str]:
        de = []
        i = 0
        while i<len(s):
            j = i
            while s[j] != "#":
                j+=1
            l = int(s[i:j])
            word = s[j+1: j+1+l]
            de.append(word)
            i = j+1+l
        return de
