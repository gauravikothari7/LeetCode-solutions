class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        chunks = []
        counts = []

        current = divisor
        count = 1

        # Build all doubled chunks
        while current <= dividend:
            chunks.append(current)
            counts.append(count)

            current = current + current
            count = count + count

        quotient = 0

        # Use chunks from biggest to smallest
        for i in range(len(chunks) - 1, -1, -1):
            if chunks[i] <= dividend:
                dividend = dividend - chunks[i]
                quotient = quotient + counts[i]

        if negative:
            quotient = -quotient

        if quotient > 2**31 - 1:
            quotient = 2**31 - 1

        return quotient