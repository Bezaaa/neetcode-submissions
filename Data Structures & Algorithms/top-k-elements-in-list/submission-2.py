class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #  max_heap
        # heap.sort()
        

        hash_map = {}
        for i in nums:
            hash_map[i] = hash_map.get(i , 0) + 1
       
        res = []
        listed = [(-freq, num) for num, freq in hash_map.items()]
        heapq.heapify(listed)
        while k > 0:
            res.append(heapq.heappop(listed)[1])

            k-=1
        return res

        