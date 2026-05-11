class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         unique = set()
         i = 0
         j = 0
         max_len = 0
         while j < len(s):
            if s[j] not in unique:
                unique.add(s[j])
                
                j+=1
                max_len = max(max_len , j - i)
                
            else:
              
            
               
                unique.remove(s[i])
            
                i +=1
                
            
         
         return max_len

         

                


        