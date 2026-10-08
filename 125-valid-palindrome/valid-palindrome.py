class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []

        for char in s:
            if char.isalnum():
                stack.append(char.lower())

        for char in s:
            if char.isalnum():
                if char.lower() != stack.pop():
                    return False

        return True