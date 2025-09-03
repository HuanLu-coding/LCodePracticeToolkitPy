# 75.py
# LeetCode #75 Sort Colors 解决方案
# 问题评估
# 问题分析
#
# 输入：一个整数数组 nums，元素为 0（红色）、1（白色）、2（蓝色）。
# 输出：原地排序数组，使得 0 在最左，1 在中间，2 在最右。
# 约束：
# 数组长度 n 范围：1 <= n <= 300。
# 数组元素仅为 0、1、2。
# 要求原地操作，不使用额外空间（O(1) 空间复杂度）。
# 不允许使用内置排序函数。
#
#
#
# 边缘情况
#
# 最小数组：n = 1，如 [2]，无需排序。
# 全相同元素：如 [1,1,1]，排序后不变。
# 极端分布：如 [2,2,0,0,1,1]，需要正确分组。
# 单一颜色：如 [0,0,0] 或 [2,2,2]。
# 无 1 的情况：如 [0,0,2,2]。
#
# 思考与优化
#
# 直觉：问题类似于分区排序，目标是将数组分为三部分：0、1、2。由于元素种类固定，计数排序或桶排序可能是直观选择，但需要考虑原地要求。
# 分析：原地要求限制了额外空间，排除计数排序（需要 O(n) 空间）。Dutch National Flag 算法（荷兰国旗问题）适合此类三分类问题，通过指针分区实现 O(1) 空间。
# 优化方向：
# 最小化遍历次数，目标 O(n) 时间。
# 确保原地操作，避免临时数组。
# 处理边缘情况，如单元素或单一颜色。
#
#
#
# 解决方案提出
#
# 计数排序（非原地）：统计 0、1、2 数量，重写数组。适合理解问题，但不符合原地要求。
# Dutch National Flag 算法（原地）：使用三指针（low、mid、high）分区，0 放左边，2 放右边，1 留在中间。满足原地和 O(1) 空间要求。
# 两遍扫描（原地）：第一遍将 0 移到左边，第二遍将 2 移到右边。简单但效率稍低。
#
#
# 解决方案 1：计数排序（非原地）
# 实现
# def sortColors(nums):
#     count = [0] * 3  # 统计 0,1,2 的数量
#     for num in nums:
#         count[num] += 1
#
#     index = 0
#     for i in range(3):
#         for _ in range(count[i]):
#             nums[index] = i
#             index += 1
#
# 执行示例
# 测试用例：nums = [2,0,2,1,1,0]
#
# 初始化 count = [0,0,0]。
# 遍历 nums，统计：count = [2,2,2]（2 个 0，2 个 1，2 个 2）。
# 重写数组：
# 写 2 个 0：[0,0,2,1,1,0]。
# 写 2 个 1：[0,0,1,1,1,0]。
# 写 2 个 2：[0,0,1,1,2,2]。结果：[0,0,1,1,2,2]。
#
#
#
# 边缘情况验证
#
# 单元素 [2]：count = [0,0,1]，重写为 [2]，正确。
# 全相同 [1,1,1]：count = [0,3,0]，重写为 [1,1,1]，正确。
# 无 1 [0,0,2,2]：count = [2,0,2]，重写为 [0,0,2,2]，正确。
#
# Big O 分析
#
# 时间复杂度：O(n)，两遍遍历（统计 + 重写）。
# 空间复杂度：O(1)，仅用固定大小数组 count（大小为 3）。
#
# 优缺点
#
# 优点：
# 简单易懂，逻辑清晰。
# 适合元素种类固定的场景。
#
#
# 缺点：
# 非原地操作，修改整个数组。
# 不符合问题严格要求（原地排序）。
# 对大规模数据效率稍低（两遍遍历）。
#
#
#
#
# 解决方案 2：Dutch National Flag 算法（原地）
# 实现
# def sortColors(nums):
#     low, mid, high = 0, 0, len(nums) - 1
#
#     while mid <= high:
#         if nums[mid] == 0:
#             nums[low], nums[mid] = nums[mid], nums[low]
#             low += 1
#             mid += 1
#         elif nums[mid] == 1:
#             mid += 1
#         else:  # nums[mid] == 2
#             nums[mid], nums[high] = nums[high], nums[mid]
#             high -= 1
#
# 执行示例
# 测试用例：nums = [2,0,2,1,1,0]
#
# 初始化：low = 0, mid = 0, high = 5。
# 遍历：
# mid = 0, nums[0] = 2：交换 nums[0] 和 nums[5]，得 [0,0,2,1,1,2]，high = 4。
# mid = 0, nums[0] = 0：交换 nums[0] 和 nums[0]，得 [0,0,2,1,1,2]，low = 1, mid = 1。
# mid = 1, nums[1] = 0：交换 nums[1] 和 nums[1]，得 [0,0,2,1,1,2]，low = 2, mid = 2。
# mid = 2, nums[2] = 2：交换 nums[2] 和 nums[4]，得 [0,0,1,1,2,2]，high = 3。
# mid = 2, nums[2] = 1：mid = 3。
# mid = 3, nums[3] = 1：mid = 4。
# mid > high，退出。结果：[0,0,1,1,2,2]。
#
#
#
# 边缘情况验证
#
# 单元素 [2]：low = 0, mid = 0, high = 0，nums[0] = 2，交换自身，正确。
# 全相同 [1,1,1]：mid 每次加 1，low 不动，high 不动，数组不变，正确。
# 无 1 [0,0,2,2]：0 移到左，2 移到右，得到 [0,0,2,2]，正确。
#
# Big O 分析
#
# 时间复杂度：O(n)，单遍遍历，每个元素最多被交换一次。
# 空间复杂度：O(1)，仅用三个指针。
#
# 优缺点
#
# 优点：
# 原地操作，完全符合问题要求。
# 单遍遍历，效率高。
# 优雅处理所有边缘情况。
#
#
# 缺点：
# 代码稍复杂，需理解三指针逻辑。
# 对初学者可能不易直观理解。
#
#
#
#
# 解决方案 3：两遍扫描（原地）
# 实现
# def sortColors(nums):
#     # 第一遍：将 0 移到左边
#     left = 0
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             nums[left], nums[i] = nums[i], nums[left]
#             left += 1
#
#     # 第二遍：将 2 移到右边
#     right = len(nums) - 1
#     for i in range(len(nums) - 1, left - 1, -1):
#         if nums[i] == 2:
#             nums[right], nums[i] = nums[i], nums[right]
#             right -= 1
#
# 执行示例
# 测试用例：nums = [2,0,2,1,1,0]
#
# 第一遍（移 0）：
# i = 0, nums[0] = 2：无操作。
# i = 1, nums[1] = 0：交换 nums[0] 和 nums[1]，得 [0,2,2,1,1,0]，left = 1。
# i = 5, nums[5] = 0：交换 nums[1] 和 nums[5]，得 [0,0,2,1,1,2]，left = 2。
#
#
# 第二遍（移 2）：
# i = 5, nums[5] = 2：交换 nums[5] 和 nums[5]，得 [0,0,2,1,1,2]，right = 4。
# i = 4, nums[4] = 1：无操作。
# i = 3, nums[3] = 1：无操作。
# i = 2, nums[2] = 2：交换 nums[2] 和 nums[4]，得 [0,0,1,1,2,2]，right = 3。结果：[0,0,1,1,2,2]。
#
#
#
# 边缘情况验证
#
# 单元素 [2]：第一遍无 0，第二遍 2 就位，正确。
# 全相同 [1,1,1]：无 0 或 2，数组不变，正确。
# 无 1 [0,0,2,2]：第一遍移 0，第二遍移 2，正确。
#
# Big O 分析
#
# 时间复杂度：O(n)，两遍遍历。
# 空间复杂度：O(1)，仅用两个指针。
#
# 优缺点
#
# 优点：
# 逻辑简单，易于理解。
# 原地操作，符合要求。
#
#
# 缺点：
# 两遍遍历，效率低于 Dutch National Flag。
# 代码稍长，重复逻辑。
#
#
#
#
# 解决方案比较
#
#
#
# 解决方案
# 时间复杂度
# 空间复杂度
# 代码可读性
# 边缘情况处理
# 适合面试
#
#
#
# 计数排序
# O(n)
# O(1)
# 高
# 优秀
# 不适合
#
#
# Dutch National Flag
# O(n)
# O(1)
# 中
# 优秀
# 非常适合
#
#
# 两遍扫描
# O(n)
# O(1)
# 高
# 优秀
# 适合
#
#
# 评估
#
# 计数排序：
# 不适合面试：非原地，违反问题核心要求。
# 可读性高，但效率一般，适用教学而非实战。
#
#
# Dutch National Flag：
# 最佳选择：单遍遍历，原地操作，效率最高。
# 面试理想：展示算法思维和优化能力，尽管代码稍复杂。
# 边缘情况：优雅处理所有情况。
#
#
# 两遍扫描：
# 适合面试：简单易解释，但效率稍逊。
# 可读性高，适合快速实现，但非最优。
#
#
#
# 最终推荐
# Dutch National Flag 算法 是最优解：
#
# 时间效率：单遍 O(n)，无可挑剔。
# 空间效率：O(1)，完全原地。
# 面试表现：展示高级算法思维，平衡复杂度和清晰度。
# 边缘情况：稳健处理所有可能输入。
from test.test_suite import run_tests

from typing import *


# 该问题描述为：给定一个仅包含 0（红）、1（白）、2（蓝）的数组，要求原地排序，使得 0 在最左，1 在中间，2 在最右，且不能使用库函数排序。
# 该问题作为经典的三路分区题目，适合练习指针操作和算法优化。
# 该算法在设计排序算法时具有重要作用，特别是快速排序（quicksort）的变体中。当数据中存在大量重复元素时，传统的二路分区可能效率低下，而三路分区（即 Dutch National Flag 算法的核心思想）可以将元素分为三类：小于关键值、等于关键值和大于关键值。这种方法显著提高了排序效率，尤其适用于处理重复元素较多的数组。
# 具体来说，该算法的实现方式是通过三个指针（通常称为 low、mid、high）来维护三个分区，时间复杂度为 O(n)，空间复杂度为 O(1)，非常适合大规模数据的处理。
#
# 时间复杂度	O(n)，单遍遍历
# 空间复杂度  O(1)，原地操作
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        return nums


test_cases = [
    {
        "method": "sortColors",
        "nums": [2, 0, 2, 1, 1, 0],
        "expected": [0, 0, 1, 1, 2, 2],
        "case_id": 1,
        "description": "Standard case with multiple colors"
    },
    {
        "method": "sortColors",
        "nums": [2, 0, 1],
        "expected": [0, 1, 2],
        "case_id": 2,
        "description": "Short array with one of each color"
    },
    {
        "method": "sortColors",
        "nums": [0],
        "expected": [0],
        "case_id": 3,
        "description": "Single element (red)"
    },
    {
        "method": "sortColors",
        "nums": [1, 1, 1],
        "expected": [1, 1, 1],
        "case_id": 4,
        "description": "All elements same color (white)"
    },
    {
        "method": "sortColors",
        "nums": [2, 2, 0, 0],
        "expected": [0, 0, 2, 2],
        "case_id": 5,
        "description": "Only red and blue colors present"
    },
    {
        "method": "sortColors",
        "nums": [1, 0],
        "expected": [0, 1],
        "case_id": 6,
        "description": "Two elements out of order"
    },
    {
        "method": "sortColors",
        "nums": [0, 1, 2],
        "expected": [0, 1, 2],
        "case_id": 7,
        "description": "Already sorted array"
    }
]

run_tests()
