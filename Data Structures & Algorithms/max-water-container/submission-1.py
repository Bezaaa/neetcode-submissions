class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """   
        
        to get the max area we have to calculate each area on the i, j point 
        hei
        [1,7,2,5,4,7,3,6]

        area1 = 1 * 
        """
        i = 0
        j = len(heights) - 1
        max_area = 0
        while i <=j :
            current_area = (j - i )* min(heights[i], heights[j])
            max_area = max(current_area , max_area)
            if heights[i] < heights[j]:
                i +=1
            else:
                j-=1
        return max_area