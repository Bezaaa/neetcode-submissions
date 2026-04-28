class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        res = []
        for i in range(len(strs)):
            if sortedString(strs[i]) in hash_map:
                hash_map[sortedString(strs[i])].append(strs[i])
            else:
                hash_map[sortedString(strs[i])] = [strs[i]]
        return list(hash_map.values())
def sortedString(string):
    list_sort = list(string)
    sortedList = sorted(list_sort)
    return "".join(sortedList)