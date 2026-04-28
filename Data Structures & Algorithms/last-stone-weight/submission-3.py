class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap = []
       
        for i in stones:
            heapq.heappush(min_heap , -i)
        while len(min_heap) > 1:
            stone1 = -heapq.heappop(min_heap)
            stone2 = -heapq.heappop(min_heap)
            if stone1 != stone2:
                heapq.heappush(min_heap , -(stone1 - stone2))
        
        return  -min_heap[0] if min_heap else  0


        