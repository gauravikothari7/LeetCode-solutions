
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0

        # Pass 1: Find the candidate
        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        # Pass 2: Verify the candidate
        frequency = 0
        for num in nums:
            if num == candidate:
                frequency += 1

        if frequency > len(nums) // 2:
            return candidate

        return -1
