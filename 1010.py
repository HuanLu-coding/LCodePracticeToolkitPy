# 1010. Pairs of Songs With Total Durations Divisible by 60

# You are given a list of songs where the ith song has a duration of time[i] seconds.
#
# Return the number of pairs of songs for which their total duration in seconds is divisible by 60.
# Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
#
# ### Constraints:
# - 1 <= time.length <= 6 * 10^4
# - 1 <= time[i] <= 500
#
# ### Example 1:
# Input: time = [30, 20, 150, 100, 40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
#
# ### Example 2:
# Input: time = [60, 60, 60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible by 60.

from test.test_suite import run_tests
from typing import *


# 分析：两数之和能被 60 整除，等价于 time[i] % 60 + time[j] % 60 == 60 或 == 0（当两者均为 60 的倍数时）。可以用哈希表记录余数频率，快速查找配对。
# 数据结构：哈希表适合存储每个余数（0 到 59）的出现次数。
# 算法：遍历数组，对于每个 time[i]，计算其补数 (60 - time[i] % 60) % 60，并查找哈希表中补数的频率。
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder_count = Counter() # 记录每个歌曲持续时间对60取余（% 60）后的值（即余数，范围0到59）出现的次数。
        pairs = 0
        for t in time:
            remainder = t % 60
            complement = (60 - remainder) % 60 # 当前余数的“补数”，计算方式是 (60 - remainder) % 60，使得 remainder + complement 能被60整除。
            pairs += remainder_count[complement] # 累加当前歌曲能与之前歌曲形成的配对数。
            remainder_count[remainder] += 1 # 更新余数计数，为后续歌曲配对做准备。
        return pairs


test_cases = [
    {
        "method": "numPairsDivisibleBy60",
        "time": [30, 20, 150, 100, 40],
        "expected": 3,
        "case_id": 1,
        "description": "Three pairs with total durations divisible by 60"
    },
    {
        "method": "numPairsDivisibleBy60",
        "time": [60, 60, 60],
        "expected": 3,
        "case_id": 2,
        "description": "All pairs sum to 120, which is divisible by 60"
    },
    {
        "method": "numPairsDivisibleBy60",
        "time": [1, 2, 3, 4, 5],
        "expected": 0,
        "case_id": 3,
        "description": "No pairs sum to a multiple of 60"
    },
    {
        "method": "numPairsDivisibleBy60",
        "time": [60],
        "expected": 0,
        "case_id": 4,
        "description": "Single element, no pairs possible"
    },
    {
        "method": "numPairsDivisibleBy60",
        "time": [30, 30, 30, 30],
        "expected": 6,
        "case_id": 5,
        "description": "All pairs of 30s sum to 60; 4 elements yield 6 pairs"
    },
    {
        "method": "numPairsDivisibleBy60",
        "time": [20, 40, 20, 40, 60],
        "expected": 4,
        "case_id": 6,
        "description": "Multiple pairs: (20,40) x2, (20,40) x2, (60,60) x0"
    }
]

run_tests()
