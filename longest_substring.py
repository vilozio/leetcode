class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        left_pt = longest = 0
        for right_pt, char in enumerate(s):
            if (match_idx := chars.get(char)) is not None:
                left_pt = max(match_idx, left_pt)
            longest = max(longest, right_pt - left_pt + 1)
            chars[char] = right_pt + 1
        return longest


def call_func(string):
    s = Solution()
    return s.lengthOfLongestSubstring(string)


def test():
    assert call_func('') == 0
    assert call_func('a') == 1
    assert call_func('bbbbb') == 1
    assert call_func('pwwkew') == 3
    assert call_func('abcabcbb') == 3
    assert call_func('abcdefc') == 6
    assert call_func('abcdcfea') == 5
    assert call_func('cbadcfe') == 6
    assert call_func('abadabc') == 4
    assert call_func('cccctggggghhhyyyyvvvv') == 3
