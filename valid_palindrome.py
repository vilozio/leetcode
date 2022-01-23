class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and i < j:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


def call(string):
    s = Solution()
    return s.isPalindrome(string)


def test():
    assert call('abcba') is True
    assert call('abccba') is True
    assert call(',-?!') is True
    assert call('aaaaaa    aa') is True
    assert call('A man, a plan, a canal: Panama') is True
    assert call('race a car') is False
    assert call(' ') is True
    assert call('') is True
