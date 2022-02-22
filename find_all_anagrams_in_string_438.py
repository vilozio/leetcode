from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []                  # [0, 6]
        p_letters = Counter(p)       # {a: 1, b: 1, c: 1}
        in_progress = Counter()      # {c: 0, b: 0, a: 0}
        i = 0                        # 7
        for j in range(len(s)):      # 9
            if s[j] in p_letters:
                in_progress.update(s[j])
            else:
                in_progress.subtract(in_progress)
                i = j + 1
            if len(p) == j - i + 1:
                for letter, count in in_progress.items():
                    if p_letters[letter] != count:
                        break
                else:
                    result.append(i)
                in_progress.subtract(s[i])
                i += 1

        return result
