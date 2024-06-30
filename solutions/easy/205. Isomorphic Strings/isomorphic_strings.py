class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}  # {r: f, d: g}
        t_to_s = {}  # {f: r, g: d}
        for s_char, t_char in zip(s, t):   # r, g
            if s_to_t.get(s_char):
                if s_to_t.get(s_char) != t_char:
                    return False
            elif not t_to_s.get(t_char):
                s_to_t[s_char] = t_char
                t_to_s[t_char] = s_char
            else:
                return False
        return True
