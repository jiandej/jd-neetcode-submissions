class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []

        for i, c in enumerate(s):
            if (c == '('):
                left.append(i)
            elif (c == '*'):
                star.append(i)
            else:
                if (not left and not star):
                    return False
                if (left):
                    left.pop()
                else:
                    star.pop()
        
        # need to check the star can handle left parenthesis 
        while (left and star):
            # left index is bigger than star index, there is no way we can handle the left parenthesis
            if (left[-1] > star[-1]):
                return False
            left.pop()
            star.pop()
        
        # no left exists
        return not left
            