class Solution:
    def calculate(self, s: str) -> int:
        res,curr_num,sign,stack=0,0,1,[]
        for char in s:
            if char.isdigit():
                curr_num=curr_num*10+int(char)
            elif char in '+-':
                res+=curr_num*sign
                sign=1 if char=='+' else -1
                curr_num=0
            elif char=='(':
                stack.append(res)
                stack.append(sign)
                res,sign=0,1
            elif char==')':
                res+=curr_num*sign
                res*=stack.pop()
                res+=stack.pop()
                curr_num=0
        return res+curr_num*sign
            