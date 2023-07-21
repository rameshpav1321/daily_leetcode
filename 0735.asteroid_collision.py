class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            add_current = True
            while len(stack) > 0 and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                elif abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    continue
                add_current = False
                break
            if add_current:
                stack.append(asteroid)
        return stack
