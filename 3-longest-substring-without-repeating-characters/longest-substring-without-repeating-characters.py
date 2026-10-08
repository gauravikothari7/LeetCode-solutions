class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        box=[]
        max_length=0
        for char in s:
            while char in box:
                box.pop(0)
            box.append(char)
            max_length=max(max_length, len(box))
        return max_length 
