class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        for x in s:
            s_map[x]=0
        for x in t:
            t_map[x]=0
        for x in s:
            s_map[x]=s_map[x]+1
        for x in t:
            t_map[x]=t_map[x]+1
        if set(t_map.keys()) == set(s_map.keys()):
            for x in t_map.keys():
                if t_map[x] != s_map[x]:
                    return False
            return True
        return False