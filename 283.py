# 283.py
from test.test_suite import run_tests


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slow = 0  # 慢指针
        for fast in range(len(nums)):  # 快指针
            if nums[fast] != 0:
                if fast != slow:  # 避免冗余交换
                    nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1

        return nums


test_cases = [
    {
        "method": "moveZeroes",
        "nums": [0, 1, 0, 3, 12],
        "expected": [1, 3, 12, 0, 0],
        "case_id": 1
    },
    {
        "method": "moveZeroes",
        "nums": [0],
        "expected": [0],
        "case_id": 2
    },
    {
        "method": "moveZeroes",
        "nums": [1, 2, 3, 4, 5],
        "expected": [1, 2, 3, 4, 5],
        "case_id": 3
    },
    {
        "method": "moveZeroes",
        "nums": [0, 0, 0, 0, 1],
        "expected": [1, 0, 0, 0, 0],
        "case_id": 4
    },
    {
        "method": "moveZeroes",
        "nums": [1, 0, 1, 0, 1, 0],
        "expected": [1, 1, 1, 0, 0, 0],
        "case_id": 5
    },
    {
        "method": "moveZeroes",
        "nums": [0, 0, 0, 0, 0],
        "expected": [0, 0, 0, 0, 0],
        "case_id": 6
    },
    {
        "method": "moveZeroes",
        "nums": [-1, 0, 5, -3, 0, 10],
        "expected": [-1, 5, -3, 10, 0, 0],
        "case_id": 7
    }
]

run_tests()
