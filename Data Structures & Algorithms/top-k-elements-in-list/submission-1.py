class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in nums:
            hash_map[i] = hash_map.get(i , 0) + 1
        res = []
        sorted_hash_map = sorted(hash_map.items(), key = lambda item:item[1],reverse=True)
        for key,val in sorted_hash_map:
            if k > 0:
                res.append(key)
            k-=1
        return res
            
            
            
        