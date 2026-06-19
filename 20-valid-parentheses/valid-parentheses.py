class Solution(object):
    def isValid(self, s):
        stack = []
        brackets = {
            ")":"(", "}":"{" , "]":"["
            }
        for char in s:
            if char in brackets:
                if stack and stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
        