import bisect
from functools import cache
from typing import List


# def binsearch(arr, x):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if x < arr[mid]:
#             high = mid - 1
#         elif x > arr[mid]:
#             low = mid + 1
#         else:
#             return mid
#     return mid if x > arr[mid] else -1


@cache
def stair_divmod(mod, index, coins):  # 24, 0, [...]
    result_div = 0
    while index >= 0 and mod >= coins[index]:  # 24 > 1
        div, mod = divmod(mod, coins[index])  # 24, 0
        result_div += div  # 24
        index = bisect.bisect_right(coins, mod) - 1  # -1
    return result_div, mod  # 24, 0


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()
        max_index = bisect.bisect_right(coins, amount) - 1  # 3
        if len(coins) < max_index < 0:
            return -1
        coins = tuple(coins)
        all_divs = []
        while max_index >= 0:  # 0 >= 0
            # index = max_index                           # 4
            # mod = amount                                # 24
            result_div, last_mode = stair_divmod(amount, max_index, coins)
            # while mod > coins[index]:                   # 0 > 1
            #     div, mod = divmod(mod, coins[index])    # 3, 0
            #     result_div += div                       # 6
            #     index = bisect.bisect_right(coins, mod) # 0
            max_index -= 1
            if last_mode == 0:
                all_divs.append(result_div)  # [6, 4, 8, 24]
        if not all_divs:
            return -1
        return min(all_divs)

# [1, 5, 6, 7] 24
