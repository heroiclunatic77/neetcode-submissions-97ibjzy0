class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ag = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in ag:
                ag[key].append(s)
            else:
                ag[key] = [s]
        return list(ag.values())