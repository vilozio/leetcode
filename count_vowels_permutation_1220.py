class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 0, 1, 2, 3, 4
        counts = (1, 1, 1, 1, 1)
        if n == 1:
            return sum(counts)
        for _ in range(n - 1):
            counts = (
                counts[e] + counts[i] + counts[u],
                counts[i] + counts[a],
                counts[e] + counts[o],
                counts[i],
                counts[i] + counts[o],
            )
        return sum(counts) % (10**9 + 7)
