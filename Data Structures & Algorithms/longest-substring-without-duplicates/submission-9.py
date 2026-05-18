class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len  = 0
        i = 0
        unique_s = set()
        j = 0
        while j < len(s):
            while s[j] in unique_s :
                
                unique_s.remove(s[i])
                i+=1
            
            unique_s.add(s[j])
            j+=1
            max_len = max(max_len , j -i)
        return max_len


         

         

                


        