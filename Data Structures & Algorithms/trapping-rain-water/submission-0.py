class Solution:
    def trap(self, height: List[int]) -> int:
        # Bruute force solution
        total = 0
        for i in range(1 , len(height)-1):
            left_max = max(height[:i])
            right_max = max(height[i+1:])
            min_h = min(left_max , right_max)
            diff = min_h - height[i]
           
            if diff > 0:
                total+=diff
        return total
        



        