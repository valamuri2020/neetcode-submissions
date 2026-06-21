class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {
            "}": "{",
            "]": "[",
            ")": "(" 
        }
        stack = []

        for c in s:
            if c in "{[(":
                stack.append(c)
            else:
                if stack and stack[-1] == parentheses_map[c]:
                    stack.pop()
                else:
                    stack.append(c)
        
        return len(stack) == 0

            