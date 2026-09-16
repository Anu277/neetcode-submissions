class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import math
        stack=[]
        result=0
        for i in tokens:
            if i=="+":
                stack.append(stack.pop()+stack.pop())
            elif i=="-" :
                a,b=stack.pop(),stack.pop()
                stack.append(b-a)
            elif i=="*" :
                stack.append(stack.pop()*stack.pop())
            elif i=="/":
                a,b=stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(i))
        j=stack[0]
        print(j)
        return math.ceil(j)