class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """  
        k ranges between 1 and max number of the piles 
        what we can do is find the mid element check if we can eat all if yes descrease the search range between 1 to the mid 
        element and check the mid again until we can't find and then return the minimum we can
        if we cant after finding the mid element the search range will be between the max and mid contiinue doing that until 
        we find the element
        
        """
        low = 1
        high = max(piles)
        min_hour = float('inf')
        while low <= high:
            mid = (low + high)//2
            total_sum = sum((num + mid - 1) // mid for num in piles)
         
            if total_sum <=h:
                min_hour = min(mid , min_hour )
                high = mid - 1
            else:
                low = mid + 1
        return min_hour