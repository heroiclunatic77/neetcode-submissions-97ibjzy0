class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_c = {}
        for str in strs:
            key = "".join(sorted(str))
            if key in ana_c:
                ana_c[key].append(str)
            else:
                ana_c[key] = [str]
        return list(ana_c.values())