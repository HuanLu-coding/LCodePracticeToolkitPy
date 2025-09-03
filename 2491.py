# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/


# 2491. Divide Players Into Teams of Equal Skill
# You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is the same.
#
# The chemistry of a team is equal to the product of the skills of the players on that team.
#
# Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is the same.
#
# ### Constraints:
# - `2 <= skill.length <= 10^5`
# - `skill.length` is even.
# - `1 <= skill[i] <= 1000`
#
# ### Example 1:
# Input: skill = [3,2,5,1,3,4]
# Output: 22
# Explanation:
# Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
# The sum of the chemistry of all teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.
#
# ### Example 2:
# Input: skill = [3,4]
# Output: 12
# Explanation:
# The two players form a team with a total skill of 7.
# The chemistry of the team is 3 * 4 = 12.
#
# ### Example 3:
# Input: skill = [1,1,2,3]
# Output: -1
# Explanation:
# There is no way to divide the players into teams such that the total skill of each team is the same.
#
# ### LeetCode 第 2491 题：将玩家分成技能相等的队伍
#
# #### 问题描述
# 给定一个长度为偶数 `n` 的正整数数组 `skill`，其中 `skill[i]` 表示第 `i` 名玩家的技能值。要求将这些玩家分成 `n / 2` 个两人小队，且每个小队的总技能值必须相等。
#
# 一个小队的“化学反应”等于该小队两名玩家技能值的乘积。
# 返回所有小队化学反应的总和；如果无法满足每个小队总技能值相等的条件，则返回 `-1`。
#
# #### 示例
# **示例 1：**
# 输入：`skill = [3, 2, 5, 1, 3, 4]`
# 输出：`22`
# 解释：
# 将玩家分成以下小队：`(1, 5)`、`(2, 4)`、`(3, 3)`，每个小队的总技能值为 `6`。
# 化学反应总和为：`1*5 + 2*4 + 3*3 = 5 + 8 + 9 = 22`。
#
# **示例 2：**
# 输入：`skill = [3, 4]`
# 输出：`12`
# 解释：
# 两名玩家组成一个小队，总技能值为 `7`，化学反应为 `3*4 = 12`。
#
# **示例 3：**
# 输入：`skill = [1, 1, 2, 3]`
# 输出：`-1`
# 解释：
# 无法将这些玩家分成总技能值相等的两人小队。
#
# #### 约束条件
# - `2 <= skill.length <= 10^5`
# - `skill.length` 是偶数。
# - `1 <= skill[i] <= 1000`
#
# ---
# ### 关键点说明
# 1. **问题核心**：
#    - 必须确保所有两人小队的总技能值相等，否则直接返回 `-1`。
#    - 若可均分，则计算所有小队化学反应的累加和。
#
# 2. **解题思路**：
#    - **排序 + 双指针**：
#      1. 将数组排序后，用双指针（首尾配对）验证每组的总和是否等于目标值（`skill[0] + skill[-1]`）。
#      2. 若所有配对均满足，则累加乘积；否则返回 `-1`。
#    - **数学优化**：
#      目标总和必须满足 `sum(skill) / (n/2)` 为整数，否则直接返回 `-1`。
#
# 3. **边界处理**：
#    - 输入长度为 `2` 时直接返回两数乘积。
#    - 所有技能值相同时可直接计算（如 `[1,1,1,1]` 返回 `1*1 + 1*1 = 2`

# 以下是对LeetCode问题#2491的详细分析和解决方案：
#
# # LeetCode 2491：将球员分成相同技能的团队
#
# ## 问题评估
#
# ### 问题理解
# - 给定一个偶数长度的技能数组，将球员分成两人一组的团队
# - 每个团队的总技能必须相同
# - "化学反应值"是团队两名球员技能的乘积
# - 返回所有团队化学反应值的总和，如果无法平均分配则返回-1
#
# ### 约束条件
# - 数组长度为偶数（2 ≤ 长度 ≤ 10^5）
# - 技能值范围：1 ≤ skill[i] ≤ 1000
#
# ### 边缘情况
# 1. 最小输入：只有两名球员 [3,4]
# 2. 不可能平均分配的情况 [1,1,2,3]
# 3. 所有球员技能相同 [2,2,2,2]
# 4. 技能值极端差异 [1000,1,1000,1]
#
# ## 解决方案思路
#
# 这个问题的关键在于：如果可以平均分配，则每个队伍的总技能值必须相同。
#
# ### 解决方案1：排序配对法
#
# 思路：
# 1. 计算所有技能的总和，确定每队的目标和（总和除以队伍数量）
# 2. 排序数组
# 3. 使用双指针（从两端向中间）配对球员，检查每对是否满足目标和
# 4. 如果所有对都满足，计算化学反应值总和
#
# ```python
# class Solution:
#     def dividePlayers(self, skill: List[int]) -> int:
#         # 排序技能数组
#         skill.sort()
#         n = len(skill)
#         teams = n // 2
#
#         # 计算目标和
#         total_skill = sum(skill)
#         if total_skill % teams != 0:
#             return -1
#
#         target_sum = total_skill // teams
#
#         # 使用双指针配对
#         chemistry_sum = 0
#         left, right = 0, n - 1
#
#         while left < right:
#             team_sum = skill[left] + skill[right]
#             if team_sum != target_sum:
#                 return -1
#             chemistry_sum += skill[left] * skill[right]
#             left += 1
#             right -= 1
#
#         return chemistry_sum
# ```
#
# **详细执行过程分析**（以示例[3,2,5,1,3,4]为例）：
# 1. 排序: [1,2,3,3,4,5]
# 2. 总技能: 1+2+3+3+4+5 = 18
# 3. 队伍数: 6/2 = 3
# 4. 目标和: 18/3 = 6
# 5. 配对过程:
#    - 左=0(值=1), 右=5(值=5): 和=6, 化学值=5, 累计=5
#    - 左=1(值=2), 右=4(值=4): 和=6, 化学值=8, 累计=13
#    - 左=2(值=3), 右=3(值=3): 和=6, 化学值=9, 累计=22
# 6. 返回: 22
#
# **边缘情况分析**：
# - [3,4]: 目标和=7, 只有一队，结果=12
# - [1,1,2,3]: 总和=7, 无法平均分成2队，返回-1
# - [2,2,2,2]: 目标和=4, 所有队都满足，结果=8
# - [1000,1,1000,1]: 目标和=1001, 两队都满足，结果=2000
#
# **复杂度分析**：
# - 时间复杂度: O(n log n) - 主要是排序操作
# - 空间复杂度: O(1) - 只使用常数额外空间
#
# **优缺点**：
# - 优点: 直观易懂，代码简洁
# - 缺点: 排序带来额外的时间复杂度
#
# ### 解决方案2：哈希表法
#
# 思路：
# 1. 计算目标和（同上）
# 2. 使用哈希表记录每个技能值的出现次数
# 3. 遍历所有技能值，寻找匹配的伙伴使和等于目标和
# 4. 累计化学反应值
#
# ```python
# class Solution:
#     def dividePlayers(self, skill: List[int]) -> int:
#         n = len(skill)
#         teams = n // 2
#
#         # 计算目标和
#         total_skill = sum(skill)
#         if total_skill % teams != 0:
#             return -1
#
#         target_sum = total_skill // teams
#
#         # 使用哈希表记录技能出现频率
#         skill_count = {}
#         for s in skill:
#             skill_count[s] = skill_count.get(s, 0) + 1
#
#         chemistry_sum = 0
#
#         # 遍历检查每个技能值
#         for s in list(skill_count.keys()):
#             if skill_count[s] > 0:
#                 partner = target_sum - s
#
#                 # 检查伙伴是否存在
#                 if partner == s:
#                     # 特殊情况：伙伴与自己相同
#                     if skill_count[s] < 2:
#                         return -1
#                     pairs = skill_count[s] // 2
#                     chemistry_sum += (s * s) * pairs
#                     skill_count[s] -= pairs * 2
#                 else:
#                     if partner not in skill_count or skill_count[partner] <= 0:
#                         return -1
#
#                     # 配对数量（取二者最小值）
#                     pairs = min(skill_count[s], skill_count[partner])
#                     chemistry_sum += (s * partner) * pairs
#
#                     skill_count[s] -= pairs
#                     skill_count[partner] -= pairs
#
#         # 检查是否所有球员都已匹配
#         for count in skill_count.values():
#             if count > 0:
#                 return -1
#
#         return chemistry_sum
# ```
#
# **详细执行过程分析**（以示例[3,2,5,1,3,4]为例）：
# 1. 总技能: 18, 目标和: 6
# 2. 哈希表: {1:1, 2:1, 3:2, 4:1, 5:1}
# 3. 配对过程:
#    - 1需要伙伴5: 各减1，化学值+=5
#    - 2需要伙伴4: 各减1，化学值+=8
#    - 3需要伙伴3: 各减1，化学值+=9
#    - 所有值用完，返回22
#
# **复杂度分析**：
# - 时间复杂度: O(n) - 只需遍历数组一次，哈希表操作均为O(1)
# - 空间复杂度: O(n) - 哈希表最大可能存储n个不同的技能值
#
# **优缺点**：
# - 优点: 时间复杂度优于排序法
# - 缺点: 实现略复杂，需要处理技能值相同的特殊情况
#
# ### 解决方案3：计数法（优化版哈希表）
#
# 这是解决方案2的简化版，利用技能范围有限的特点。
#
# ```python
# class Solution:
#     def dividePlayers(self, skill: List[int]) -> int:
#         n = len(skill)
#         teams = n // 2
#
#         # 计算目标和
#         total_skill = sum(skill)
#         if total_skill % teams != 0:
#             return -1
#
#         target_sum = total_skill // teams
#
#         # 使用数组替代哈希表（因为技能值范围有限）
#         skill_count = [0] * 1001
#         for s in skill:
#             skill_count[s] += 1
#
#         chemistry_sum = 0
#
#         # 遍历所有可能的技能值
#         for s in range(1, 1001):
#             if skill_count[s] > 0:
#                 partner = target_sum - s
#
#                 # 检查伙伴有效性
#                 if partner < 1 or partner > 1000:
#                     return -1
#
#                 if s == partner:
#                     # 伙伴与自己相同的情况
#                     if skill_count[s] % 2 != 0:
#                         return -1
#                     chemistry_sum += (s * s) * (skill_count[s] // 2)
#                     skill_count[s] = 0
#                 else:
#                     if skill_count[partner] != skill_count[s]:
#                         return -1
#                     chemistry_sum += (s * partner) * skill_count[s]
#                     skill_count[partner] = 0
#                     skill_count[s] = 0
#
#         return chemistry_sum
# ```
#
# **复杂度分析**：
# - 时间复杂度: O(n + k) - n是数组长度，k是技能范围（此题中k=1000）
# - 空间复杂度: O(k) - 固定大小的计数数组
#
# **优缺点**：
# - 优点: 在技能范围有限的情况下性能很好
# - 缺点: 如果技能范围很大，会浪费空间
#
# ## 方案比较与最佳选择
#
# |              | 排序配对法       | 哈希表法         | 计数法           |
# |--------------|---------------|---------------|---------------|
# | 时间复杂度      | O(n log n)    | O(n)          | O(n + k)      |
# | 空间复杂度      | O(1)          | O(n)          | O(k)          |
# | 代码简洁性      | 极好           | 中等           | 好             |
# | 边缘情况处理    | 完整           | 完整           | 完整           |
#
# **最佳选择：排序配对法**
#
# 虽然在理论时间复杂度上排序法略逊，但综合考虑以下因素：
# 1. 代码简洁易懂，面试中能快速编写并解释
# 2. 空间复杂度最优
# 3. 对于算法题实际测试案例，n log n 与 n 的实际运行时间差异可能不大
# 4. 无需处理技能值相同的特殊情况
#
# ## 关键思想总结
#
# 这道题的核心思想是：
# 1. **目标和必须一致**：所有球员技能和÷队伍数=每队技能和
# 2. **配对方法**：排序后从两端配对是最直观的方法
# 3. **验证条件**：每对球员和必须等于目标和
# 4. **化学反应值**：就是每对球员技能的乘积之和
#
# 记住这个问题的解决方案关键在于"两端配对法"，这是解决许多两人组合问题的常用技巧。
from test.test_suite import run_tests
from typing import *


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # 排序技能数组
        skill.sort()
        n = len(skill)
        teams = n // 2

        # 计算所有技能的总和
        total_skill = sum(skill)
        if total_skill % teams != 0:
            return -1
        # 确定每队的目标和（总和除以队伍数量）
        target_sum = total_skill // teams

        # 使用双指针（从两端向中间）配对球员，检查每对是否满足目标和
        chemistry_sum = 0
        left, right = 0, n - 1

        while left < right:
            team_sum = skill[left] + skill[right]
            if team_sum != target_sum:
                return -1
            chemistry_sum += skill[left] * skill[right]
            left += 1
            right -= 1

        return chemistry_sum


test_cases = [
    {
        "method": "dividePlayers",
        "skill": [3, 2, 5, 1, 3, 4],
        "expected": 22,
        "case_id": 1,
        "description": "常规示例：可均分且计算化学反应总和"
    },
    {
        "method": "dividePlayers",
        "skill": [3, 4],
        "expected": 12,
        "case_id": 2,
        "description": "最小输入：仅两名玩家"
    },
    {
        "method": "dividePlayers",
        "skill": [1, 1, 2, 3],
        "expected": -1,
        "case_id": 3,
        "description": "无法均分总技能值的情况"
    },
    {
        "method": "dividePlayers",
        "skill": [1, 1, 1, 1],
        "expected": 2,
        "case_id": 4,
        "description": "所有玩家技能值相同"
    },
    {
        "method": "dividePlayers",
        "skill": [10, 10, 20, 20, 30, 30],
        "expected": 1000,
        "case_id": 5,
        "description": "多组重复技能值"
    },
    {
        "method": "dividePlayers",
        "skill": [2, 3, 4, 5],
        "expected": 22,
        "case_id": 6,
        "description": "无法均分的非对称输入"
    }
]

run_tests()
