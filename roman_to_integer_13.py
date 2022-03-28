class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        substract_chars = ('I', 'X', 'C')
        num = 0
        i = 0
        while i < len(s):
            digit = nums[s[i]]  # 1
            if s[i] in substract_chars and i < len(s) - 1:   # true
                next_digit = nums[s[i + 1]]                  # 5
                may_digit = next_digit - digit               # 4
                if (may_digit > 0
                    and (may_digit % 4 == 0
                         or may_digit % 9 == 0)):            # false
                    digit = may_digit                        # 4
                    i += 1                                   # 2
            num += digit                # 14
            i += 1
        return num

# XIV
