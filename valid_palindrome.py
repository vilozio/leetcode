class Solution:
    def is_alphanumeric(self, char):
        return ((ord('a') <= ord(char.lower()) <= ord('z'))
                or (ord('0') <= ord(char) <= ord('9')))

    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while not self.is_alphanumeric(s[i]) and i < j:
                i += 1
            while not self.is_alphanumeric(s[j]) and i < j:
                j -= 1
            if i == j:
                return True
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
