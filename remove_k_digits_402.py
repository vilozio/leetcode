class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and len(stack) > 0 and stack[-1] > digit:
                k -= 1
                stack.pop()
            stack.append(digit)
        if k > 0:
            stack = stack[:-k]
        return "".join(stack).lstrip("0") or "0"


def call(num, k):
    s = Solution()
    return s.removeKdigits(num, k)


def test():
    assert call('12345', 2) == '123'
    assert call('1432219', 3) == '1219'
    assert call('10200', 1) == '200'
    assert call('10', 2) == '0'
