class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        def cal(a,b,t):
            if t=='*':
                return a*b
            
            elif t=='+':
                return a+b
            
            elif t=='/':
                return int(a/b)
            
            elif t == '-':
                return a-b
            
            else:
                pass
        
        
        for i in tokens:
            if (c =='*')|(c=='/')|(c=='+')|(c=='-'):
                y = int(stack.pop())
                x = int(stack.pop())
                stack.append(cal(x,y,i))
            else:
                stack.append(i)
        
        return stack[0]
            
    
          
        
            
                
                