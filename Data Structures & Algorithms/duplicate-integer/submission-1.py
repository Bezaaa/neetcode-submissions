class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = list(set(nums))
        return True if len(unique)!=len(nums) else False
         