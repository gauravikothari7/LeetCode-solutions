
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)
        squares = [0] * (4 * n)
        last = {}
        ans = 0

        def update(node, start, end, left, right):
            if lazy[node]:
                val = lazy[node]
                length = end - start + 1

                squares[node] = (
                    squares[node] + 2 * val * tree[node]
                    + length * val * val
                ) % MOD

                tree[node] = (tree[node] + length * val) % MOD

                if start != end:
                    lazy[node * 2] += val
                    lazy[node * 2 + 1] += val

                lazy[node] = 0

            if start > right or end < left:
                return

            if left <= start and end <= right:
                val = 1
                length = end - start + 1

                squares[node] = (
                    squares[node] + 2 * tree[node] + length
                ) % MOD

                tree[node] = (tree[node] + length) % MOD

                if start != end:
                    lazy[node * 2] += 1
                    lazy[node * 2 + 1] += 1

                return

            mid = (start + end) // 2

            update(node * 2, start, mid, left, right)
            update(node * 2 + 1, mid + 1, end, left, right)

            tree[node] = (
                tree[node * 2] + tree[node * 2 + 1]
            ) % MOD

            squares[node] = (
                squares[node * 2] + squares[node * 2 + 1]
            ) % MOD

        for i, x in enumerate(nums):
            left = last.get(x, -1) + 1

            update(1, 0, n - 1, left, i)

            last[x] = i
            ans = (ans + squares[1]) % MOD

        return ans
