# 15.py
from test.test_suite import run_tests
from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        if n < 3:
            return result

        nums.sort()

        for i in range(n):
            # 如果第一个数就大于0，后面不可能有三数之和等于0的情况
            # 退出整个循环
            if nums[i] > 0:
                break

            # 跳过重复的第一个数
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # 在固定 nums[i] 的情况下，找到一个三元组后继续向中间搜索的逻辑是必要的，因为：
                    # 覆盖所有可能组合：同一个 nums[i] 可能对应多个不同的三元组。
                    #
                    # 跳过重复元素
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result


test_cases = [
    {
        "method": "threeSum",
        "nums": [-1, 0, 1, 2, -1, -4],
        "expected": [[-1, -1, 2], [-1, 0, 1]],
        "case_id": 1
    },
    {
        "method": "threeSum",
        "nums": [0, 1, 1],
        "expected": [],
        "case_id": 2
    },
    {
        "method": "threeSum",
        "nums": [0, 0, 0],
        "expected": [[0, 0, 0]],
        "case_id": 3
    },
    {
        "method": "threeSum",
        "nums": [-2, 0, 1, 1, 2],
        "expected": [[-2, 0, 2], [-2, 1, 1]],
        "case_id": 4
    },
    {
        "method": "threeSum",
        "nums": [-4, -2, -2, -2, 0, 1, 2, 2, 2, 2],
        "expected": [[-4, 2, 2], [-2, 0, 2]],
        "case_id": 5
    }
]

run_tests()
