class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generateParentheses(current ,open, closed,res=[]):
           
            if open:
                generateParentheses(current + '(', open-1, closed)
            if closed > open: 
                generateParentheses(current + ')', open, closed-1)
            if not closed:    
                res += current,
            return res
        return generateParentheses('', n, n)
        