class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures) 
        res  = [0] * n 
        # for i in range(len(temperatures)):
        #     for j in range(i+1 , len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             res.append(j-i)
        #             break
                
        # while len(res) <= len(temperatures)-1:
        #     res.append(0)

        # return res
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                popped = stack.pop()
                res[popped] = i - popped
            stack.append(i)
   
        return res
                
                

            
    

        

       
    
