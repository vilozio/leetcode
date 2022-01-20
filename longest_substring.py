class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        left_pt = longest = 0
        for right_pt, char in enumerate(s):
            if (match_idx := chars.get(char)) is not None:
                left_pt = match_idx + 1
                chars[char] = right_pt
                for other_char in list(chars.keys()):
                    if chars[other_char] < left_pt:
                        del chars[other_char]
            else:
                chars[char] = right_pt
            longest = max(longest, right_pt - left_pt + 1)
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
