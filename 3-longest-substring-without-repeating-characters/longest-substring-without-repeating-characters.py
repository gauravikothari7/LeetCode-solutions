class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            char = s[right]

            if char in last and last[char] >= left:
                left = last[char] + 1

            last[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length



