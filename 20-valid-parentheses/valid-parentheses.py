class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            else:
                if not stack:
                    return False

                top = stack.pop()

                if top != char:
                    return False

        return not stack