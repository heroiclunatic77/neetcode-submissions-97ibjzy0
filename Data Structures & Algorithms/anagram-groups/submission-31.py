class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        key = ''
        for str in strs:
            key = "".join(sorted(str))
            if key in ana:
                ana[key].append(str)
            else:
                ana[key] = [str]
        return list(ana.values())
