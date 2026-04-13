class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_left = []
        stack_star = []

        for i, c in enumerate(s):
            if (c == '('):
                stack_left.append(i)
            elif (c == '*'):
                stack_star.append(i)
            elif (c == ')'):
                if (not stack_left and not stack_star):
                    return False
                if (stack_left):
                    stack_left.pop()
                else:
                    stack_star.pop()
        
        while (stack_left and stack_star):
            if (stack_left.pop() > stack_star.pop()):
                return False
        
        return not stack_left
            