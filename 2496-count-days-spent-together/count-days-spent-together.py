
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        prefix = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

        def convert(date):
            month = int(date[:2])
            day = int(date[3:])
            return prefix[month - 1] + day

        start = max(convert(arriveAlice), convert(arriveBob))
        end = min(convert(leaveAlice), convert(leaveBob))

        return max(0, end - start + 1)
