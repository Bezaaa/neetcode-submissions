class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
            ops = {
                "+": lambda a, b: int(a) + int(b),
                "-": lambda a, b: int(a) - int(b),
                "*": lambda a, b: int(a) * int(b),
                "/": lambda a, b: int(int(a)/ int(b)) 
            }

            stack = []
            for i in tokens:
                if i in ops:
                   
                    a = stack.pop()
                    b =stack.pop()
                    
                    stack.append(ops[i](b,a))
                    continue
                else:
                    stack.append(i)
           
            return int(stack[-1])

        