class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_strs = {}
        for s in strs:
            if dict_strs.get(tuple(sorted(s))):
               dict_strs.get(tuple(sorted(s))).append(s)
            else:
                dict_strs[tuple(sorted(s))] = [s]
        return list(dict_strs.values())

        