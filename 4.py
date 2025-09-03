# ### LeetCode 第 4 题：寻找两个有序数组的中位数
#
# #### 1. 问题分析
# **问题描述**：
# 给定两个大小分别为 `m` 和 `n` 的正序（非递减）数组 `nums1` 和 `nums2`，找出这两个数组的 **中位数**。要求时间复杂度为 `O(log(m+n))`。
#
# **关键点**：
# - 中位数定义：若合并后数组长度为奇数，中位数为中间元素；若为偶数，则为中间两个元素的平均值。
# - **有序数组**：可利用二分法优化搜索。
# - **时间复杂度限制**：直接合并数组的 `O(m+n)` 方法不满足要求。
#
# #### 2. 边界条件与约束
# - 数组可能为空（如 `nums1=[], nums2=[1]`）。
# - 数组元素可能全部相同（如 `nums1=[2,2], nums2=[2,2]`）。
# - 两数组长度差异极大（如 `nums1=[1], nums2=[2,3,4,...,10000]`）。
# - 元素范围：`-10^6 <= nums[i] <= 10^6`。
#
# ---
#
# ### 解决方案
#
# #### 方法一：二分切割法（最优解）
# **核心思想**：
# 将两个数组分别切割，确保左半部分元素数量等于右半部分，且左半部分的最大值不超过右半部分的最小值。通过二分法快速定位切割点。
#
# **步骤**：
# 1. 确保 `nums1` 是较短的数组，简化边界处理。
# 2. 在 `nums1` 中进行二分搜索，确定切割点 `i`，则 `nums2` 的切割点 `j` 满足 `(m+n+1)//2 - i`。
# 3. 检查切割后的左右部分是否满足 `max_left <= min_right`。
# 4. 根据奇偶性返回中位数。
#
# **代码实现**：
# ```python
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         if len(nums1) > len(nums2):
#             nums1, nums2 = nums2, nums1
#         m, n = len(nums1), len(nums2)
#         left, right = 0, m
#         total_left = (m + n + 1) // 2
#
#         while left <= right:
#             i = (left + right) // 2
#             j = total_left - i
#             if i < m and nums2[j-1] > nums1[i]:
#                 left = i + 1
#             elif i > 0 and nums1[i-1] > nums2[j]:
#                 right = i - 1
#             else:
#                 if i == 0: max_left = nums2[j-1]
#                 elif j == 0: max_left = nums1[i-1]
#                 else: max_left = max(nums1[i-1], nums2[j-1])
#
#                 if (m + n) % 2 == 1:
#                     return max_left
#
#                 if i == m: min_right = nums2[j]
#                 elif j == n: min_right = nums1[i]
#                 else: min_right = min(nums1[i], nums2[j])
#                 return (max_left + min_right) / 2
# ```
#
# **执行示例**：
# 输入 `nums1=[1,3], nums2=[2]`：
# 1. 初始 `i=1`, `j=1`，左半部分 `[1,2]`，右半部分 `[3]`，满足 `max_left=2 <= min_right=3`。
# 2. 合并长度奇数，返回 `2`。
#
# **边界测试**：
# - `nums1=[], nums2=[1]`：直接返回 `1`。
# - `nums1=[2], nums2=[]`：返回 `2`。
#
# **复杂度分析**：
# - 时间：`O(log(min(m,n)))`，因二分法作用于较短数组。
# - 空间：`O(1)`，仅用常数变量。
#
# **优缺点**：
# - 优点：高效，满足题目要求。
# - 缺点：逻辑复杂，易出错。
#
# ---
#
# #### 方法二：合并后取中位数（暴力法）
# **思路**：直接合并数组并排序，取中位数。
# **代码**：
# ```python
# def findMedianSortedArrays(nums1, nums2):
#     merged = sorted(nums1 + nums2)
#     length = len(merged)
#     return (merged[length//2] + merged[(length-1)//2]) / 2
# ```
# **复杂度**：时间 `O((m+n)log(m+n))`，空间 `O(m+n)`。
# **适用场景**：面试中可先提此方法，再优化。
#
# ---
#
# ### 方案对比
# | 方案         | 时间复杂度       | 空间复杂度 | 面试适用性 | 代码复杂度 |
# |--------------|------------------|------------|------------|------------|
# | 二分切割法   | `O(log(min(m,n)))` | `O(1)`     | ★★★★★      | 高         |
# | 暴力合并法   | `O((m+n)log(m+n))` | `O(m+n)`   | ★★☆☆☆      | 低         |
#
# **最优选择**：二分切割法，因其高效且能体现算法思维。
#
# ---
#
# ### 关键总结
# - **核心技巧**：通过二分法切割数组，确保左右部分平衡。
# - **面试技巧**：先提暴力法，再逐步优化到二分法。
# - **记忆口诀**：“短数组二分切，左半右半比大小，奇偶分情况返回”。
