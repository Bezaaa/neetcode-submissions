class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        final_res = []

        # first window
        for j in range(k):
            res.append(nums[j])
        max_num = max(res)
        final_res.append(max_num)

        # sliding
        for j in range(k, len(nums)):
            res.append(nums[j])
            popped = res.pop(0)

            if popped == max_num:
                max_num = max(res)   # recompute from window
            else:
                max_num = max(max_num, nums[j])

            final_res.append(max_num)

        return final_res



          

        

        