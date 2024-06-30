class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        prev_sums = set()
        while True:
            n = sum(int(digit) ** 2 for digit in str(n))
            if n == 1:
                return True
            if n in prev_sums:
                return False
            prev_sums.add(n)
        return False
