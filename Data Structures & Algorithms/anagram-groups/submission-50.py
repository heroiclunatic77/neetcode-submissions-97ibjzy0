class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for str in strs:
            key = "".join(sorted(str))
            if key in anagram:
                anagram[key].append(str)
            else:
                anagram[key] = [str]
        return list(anagram.values())