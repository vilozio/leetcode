from collections import defaultdict
from math import ceil


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        word_len = len(words[0])
        if len(words) * word_len > n:
            return []
        start_ids = {}
        uniq_words = defaultdict(int)
        for word in words:
            uniq_words[word] += 1
        steps = ceil(n / word_len)
        # Time complexity n * m * k
        for i in range(word_len):
            for step in range(steps):
                shift = step * word_len
                if i + shift < n:
                    for word in uniq_words:
                        if s[i + shift:i + shift + word_len] == word:
                            start_ids[i + shift] = word
        starts = []
        # Time complexity n * m
        for i, word in start_ids.items():
            substr = defaultdict(int)
            substr[word] = 1
            for step in range(1, len(words)):
                next_i = i + step * word_len
                if next_i in start_ids:
                    substr[start_ids[next_i]] += 1
            if substr == uniq_words:
                starts.append(i)
        return starts
