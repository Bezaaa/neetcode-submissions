class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        for i in s:
            hash_s[i] = hash_s.get(i , 0) + 1
        for j in t:
            hash_t[j] = hash_t.get(j,0) + 1
        return hash_s == hash_t

        