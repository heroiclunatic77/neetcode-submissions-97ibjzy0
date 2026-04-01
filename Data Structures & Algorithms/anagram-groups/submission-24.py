class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        for st in strs:
            key = "".join(sorted(st))
            if key in ana:
                ana[key].append(st)
            else:
                ana[key] = [st]
        return list(ana.values())
         