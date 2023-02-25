class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        dict={'+','-','/','*'}
        for k in tokens:
            if k not in dict:
                stack.append(int(k))
            if k=='+':
                stack.append(stack.pop()+stack.pop())
            elif k=='/': 
                x,y=stack.pop(),stack.pop()
                stack.append(int(y/x))
            elif k=='*':  
                stack.append(stack.pop()*stack.pop())

            elif k=='-':
                x,y=stack.pop(),stack.pop()
                stack.append(y-x)             
        return stack[0]