class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_map = {}
        for word in strs:
           sorted_word= "".join(sorted(word))
           if sorted_word not in sorted_map:
                sorted_map[sorted_word] = []
        for i in strs:
            sorted_word = "".join(sorted(i))
            if sorted_word in sorted_map:
                sorted_map[sorted_word].append(i)
        res = []
        for vals in sorted_map.values():
            res.append(vals)
        return res

        