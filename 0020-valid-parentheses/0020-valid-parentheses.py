class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = "({["
        right = ")}]"
        for c in s:
            if c in left:
                stack.append(c)
            else:
                if len(stack) != 0 and left.find(stack[-1]) == right.find(c):
                    stack.pop()
                else:
                    return False
        if len(stack) != 0:
            return False
        return True