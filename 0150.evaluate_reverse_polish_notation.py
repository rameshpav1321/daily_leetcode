class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token not in {'+','-','/','*'}:
                stack.append(token)
            else:
                op1=stack.pop()
                op2=stack.pop()
                stack.append(str(int(eval(op2+token+op1))))
        return int(stack[-1])