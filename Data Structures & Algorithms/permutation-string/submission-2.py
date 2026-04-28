class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_map = {}
        s2_map = defaultdict(int)
        for i in s1:
            s1_map[i] = s1_map.get(i,0)+1
        for i in range(len(s1)):
            s2_map[s2[i]] +=1
        i = 0
        j = len(s1) 
        
        if s1_map == s2_map:
            return True
        while j < len(s2):

            
            s2_map[s2[i]]-=1
            s2_map[s2[j]]+=1
           
            if s2_map[s2[i]]==0:
                del s2_map[s2[i]]
            i+=1
          
           
            j+=1
            if s1_map == s2_map:
                return True
        return False
                
            


        