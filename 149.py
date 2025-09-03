from collections import defaultdict
from math import gcd


class Solution:
    def maxPoints(self, points):
        n = len(points)
        if n <= 2:
            return n

        max_points = 1

        for i in range(n):
            slopes = defaultdict(int)
            same_point = 0
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 == x2 and y1 == y2:
                    same_point += 1
                    continue

                if x1 == x2:
                    slope = float('inf')
                else:
                    dx = x2 - x1
                    dy = y2 - y1
                    g = gcd(dx, dy)
                    # 标准化斜率：确保分母为正
                    if dx // g < 0:
                        slope = (-dy // g, -dx // g)
                    else:
                        slope = (dy // g, dx // g)

                slopes[slope] += 1

            if slopes:
                max_points = max(max_points, max(slopes.values()) + same_point + 1)
            else:
                max_points = max(max_points, same_point + 1)

        return max_points
# 感谢确认修复后的解决方案已通过 LeetCode，但其性能（击败 44.07%）仍有优化空间。以下我们将分析当前解决方案的性能瓶颈，尝试改进或提出更优的解决方案，以提升运行效率，同时保持代码可读性和面试适用性。
#
# ---
#
# ## 当前解决方案分析
#
# ### 修复后的解决方案
# ```python
# from collections import defaultdict
# from math import gcd
#
# class Solution:
#     def maxPoints(self, points):
#         n = len(points)
#         if n <= 2:
#             return n
#
#         max_points = 1
#
#         for i in range(n):
#             slopes = defaultdict(int)
#             same_point = 0
#             for j in range(n):
#                 if i == j:
#                     continue
#                 x1, y1 = points[i]
#                 x2, y2 = points[j]
#
#                 if x1 == x2 and y1 == y2:
#                     same_point += 1
#                     continue
#
#                 if x1 == x2:
#                     slope = float('inf')
#                 else:
#                     dx = x2 - x1
#                     dy = y2 - y1
#                     g = gcd(dx, dy)
#                     slope = (dy // g, dx // g)
#
#                 slopes[slope] += 1
#
#             if slopes:
#                 max_points = max(max_points, max(slopes.values()) + same_point + 1)
#
#         return max_points
# ```
#
# ### 性能瓶颈
# 1. **时间复杂度**：O(n²)，因为需要遍历每对点计算斜率。对于 n ≤ 300，这个复杂度是可接受的，但仍可能因常量因子（如 GCD 计算、哈希表操作）影响性能。
# 2. **GCD 计算**：`math.gcd` 的复杂度为 O(log(min(a, b)))，对每对非垂直线的点都调用，累计开销较大。
# 3. **哈希表操作**：`defaultdict` 的插入和查询操作频繁，尤其在点密集的情况下，哈希冲突可能增加开销。
# 4. **重复计算**：当前方案对每对点 `(i, j)` 和 `(j, i)` 都计算斜率，存在冗余。
#
# ### 优化目标
# - 减少 GCD 计算次数。
# - 避免重复计算斜率。
# - 优化哈希表操作或减少不必要的循环。
# - 保持 O(n²) 时间复杂度和 O(n) 空间复杂度。
#
# ---
#
# ## 优化方案
#
# ### 改进方案 1：减少重复计算
# 当前方案对每对点 `(i, j)` 和 `(j, i)` 都计算斜率，导致冗余。我们可以通过限制 `j > i` 来避免重复计算，同时确保正确统计所有共线点。这种方法在之前的失败方案中尝试过，但因斜率表示错误导致问题。现在使用正确的斜率表示，应该能提升性能。
#
# 以下是改进后的代码：
#
# ```python
# from collections import defaultdict
# from math import gcd
#
# class Solution:
#     def maxPoints(self, points):
#         n = len(points)
#         if n <= 2:
#             return n
#
#         max_points = 1
#
#         for i in range(n):
#             slopes = defaultdict(int)
#             same_point = 0
#             for j in range(i + 1, n):
#                 x1, y1 = points[i]
#                 x2, y2 = points[j]
#
#                 if x1 == x2 and y1 == y2:
#                     same_point += 1
#                     continue
#
#                 if x1 == x2:
#                     slope = float('inf')
#                 else:
#                     dx = x2 - x1
#                     dy = y2 - y1
#                     g = gcd(dx, dy)
#                     slope = (dy // g, dx // g)
#
#                 slopes[slope] += 1
#
#             if slopes:
#                 max_points = max(max_points, max(slopes.values()) + same_point + 1)
#             else:
#                 max_points = max(max_points, same_point + 1)  # 只有重复点的情况
#
#         return max_points
# ```
#
# #### 改进点
# - **循环范围**：将内层循环从 `range(n)` 改为 `range(i + 1, n)`，减少约一半的斜率计算。
# - **结果更新**：显式处理 `slopes` 为空的情况（例如所有点都是重复点），确保正确性。
# - **重复点处理**：保持与原方案一致，确保重复点正确计入。
#
# #### 执行过程（测试用例）
# **输入**：`points = [[1,1],[2,2],[3,3]]`
# - 选择点 `[1,1]`：
#   - 与 `[2,2]` 的斜率：`(1,1)`，`slopes[(1,1)] = 1`。
#   - 与 `[3,3]` 的斜率：`(1,1)`，`slopes[(1,1)] = 2`。
#   - `same_point = 0`，`max(slopes.values()) = 2`，总点数 `2 + 0 + 1 = 3`。
# - 选择点 `[2,2]`：
#   - 与 `[3,3]` 的斜率：`(1,1)`，`slopes[(1,1)] = 1`。
#   - `same_point = 0`，`max(slopes.values()) = 1`，总点数 `1 + 0 + 1 = 2`。
# - 全局最大值：3。
#
# #### 边缘测试用例验证
# - **空数组**：`n = 0`，返回 0。
# - **所有点相同**：`points = [[0,0],[0,0]]`，`same_point = 1`，`slopes` 为空，返回 `1 + 1 = 2`。
# - **垂直线**：`points = [[0,0],[0,1],[0,2]]`，斜率 `float('inf')` 计数 2，返回 `2 + 0 + 1 = 3`。
# - **两个点**：`n = 2`，返回 2。
#
# #### Big O 分析
# - **时间复杂度**：仍为 O(n²)，但内层循环从 n 减少到 n-i，平均约 n/2，实际运行时间显著降低。
# - **空间复杂度**：O(n)，哈希表存储斜率计数。
#
# #### 优缺点
# - **优点**：
#   - 减少约一半的斜率计算，提升运行效率。
#   - 保留原方案的正确性和可读性。
#   - 适合面试，逻辑清晰且易于解释。
# - **缺点**：
#   - 仍需为每对点计算 GCD，未进一步优化 GCD 开销。
# ## 最终评估
# - **原因**：
#   - 通过限制 `j > i`，减少约一半的斜率计算和 GCD 调用，显著提升运行效率。
#   - 保持 O(n²) 时间复杂度和 O(n) 空间复杂度，适合 LeetCode 约束（n ≤ 300）。
#   - 代码简洁，逻辑清晰，易于在面试中实现和解释。
#   - 正确处理所有边缘情况（如空数组、重复点、垂直线）。
# - **预计性能**：减少一半计算后，预计可击败 60-80% 的提交，具体取决于测试用例分布。
# - **面试适用性**：优于原方案，展示了对性能优化的思考，同时保持代码简洁。
#
