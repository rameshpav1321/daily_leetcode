class Solution:
    def isValid(self, s: str) -> bool:
        my_map={')':'(',']':'[','}':'{'}
        stack=[]
        for char in s:
            if char in my_map.values():
                stack.append(char)
                continue
            if char in my_map.keys():
                if not stack or my_map[char]!=stack[-1]:
                    return False
                else:
                    stack.pop()
                    continue
        return len(stack)==0
