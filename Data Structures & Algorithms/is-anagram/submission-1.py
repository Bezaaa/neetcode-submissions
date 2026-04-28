class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map_s = {}
        if len(s)!=len(t): return False
        for i in s:
            hash_map_s[i] = hash_map_s.get(i , 0)+1
        for i in t:
            if i not in hash_map_s:
                return False
            else:
                hash_map_s[i]-=1
                if hash_map_s[i] == 0:
                    del hash_map_s[i]
        return True
        