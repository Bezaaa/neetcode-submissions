class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
      
            stack = []  # store indices
            max_area = 0
            heights.append(0)  # Sentinel to flush the stack at the end

            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h:
                    top_index = stack.pop()
                    height = heights[top_index]

                    # Width is either from start (if stack is empty) or between previous and current index
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)

                stack.append(i)

            return max_area
        