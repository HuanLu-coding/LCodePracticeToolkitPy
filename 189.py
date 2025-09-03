# 189. Rotate Array
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
#
# ### Constraints:
# - `1 <= nums.length <= 10^5`
# - `-2^31 <= nums[i] <= 2^31 - 1`
# - `0 <= k <= 10^5`
#
# ### Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
# ### Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#
# Follow up:
# - Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# - Could you do it in-place with O(1) extra space?
from test.test_suite import run_tests
from typing import *


# ---
### 解决方案 2：环状替换法
#### 方法思路
# 将元素直接移动到目标位置，形成环。例如：
# `nums = [1,2,3,4,5,6], k = 2`：
# - 1 → 3 → 5 → 1（环1）
# - 2 → 4 → 6 → 2（环2）
# 需处理所有独立的环。
# 好的，没问题。我们用最简单的方式来理解“环状替换法”。
#
# 想象一下数组里的元素是一群小朋友站成一排，现在要让他们整体向右挪动 `k` 个位置，空出来的位置要从队尾绕回来补上。而且我们没有多余的空间，小朋友们必须直接挪到“自己旋转后的那个位置”上去。
#
# **核心难题：**
#
# 如果小朋友 A 直接走到他旋转后的位置上（比如 B 的位置），那 B 原本站在那里的信息（B 是谁）就丢失了！我们必须先记住 B 是谁，A 才能过去。
#
# **解法的关键概念和绝招 (The Trick)：**
#
# 我们玩一个“占位传值”的游戏：
#
# 1.  **找一个起始位置 (Start):** 随便找一个还没“挪好位置”的小朋友作为起点（比如第一个小朋友）。
# 2.  **记住当前的小朋友：** 把当前位置上的小朋友 **“是谁”** 记下来（暂存起来）。
# 3.  **找下一个位置：** 计算当前位置向右挪动 `k` 步后，应该去的位置（记住，如果超过总人数就从头开始数，就像绕圈一样）。
# 4.  **让“下一个人”来占位：** 去“下一个位置”，把那个位置上的小朋友挪到 **当前这个位置** 来。
# 5.  **新的当前位置：** 现在你的“当前位置”变成了刚才小朋友挪过来的那个位置。
# 6.  **重复：** 回到第 2 步，记住新的当前位置上的小朋友，计算他的下一个位置，让再下一个人来占位... 这样形成一个“链条”式的连续挪动。
# 7.  **回到原点：** 这个链条会一圈一圈地传下去，最终你会回到最初的那个起始位置。
# 8.  **放回最初记住的小朋友：** 把最开始你记住的那个小朋友，放到这个链条最终绕回来的位置上。
#
# **一个环完成！** 这就像完成了一次接力，链条上的所有小朋友都向右“轮转”了一步。
#
# **为什么要一个 `for start in range(n)` 和一个计数器 `count`？**
#
# * 有时候，不是所有小朋友都在同一个“传值链条”里。比如总共 6 个人，右移 2 步，1 会传给 3，3 传给 5，5 再传给 1（这是一个链条）。2 会传给 4，4 传给 6，6 再传给 2（这是另一个链条）。这两个链条是分开的。
# * 我们需要确保 **所有** 小朋友都参与了挪动。
# * 外面的 `for start in range(n)` 就是尝试从每个位置 `0, 1, 2, ...` 开始启动一个“占位传值”链条。
# * `count` 计数器就是数着已经有多少小朋友被“挪到位”了。
# * 如果从某个 `start` 开始启动链条时，发现这个位置的小朋友已经被之前的链条处理过了（即这个位置已经被挪动过值了），那么这个链条会很快绕一圈回到 `start`。
# * 只要 `count` 小于总人数 `n`，就说明还有小朋友没挪好，我们继续尝试下一个 `start` 位置，直到 `count` 达到 `n`，所有小朋友都各就各位了。
#
# **文盲也能理解的比喻：**
#
# 就像一队小朋友玩“击鼓传花”，但规则变了：不是传花，而是传 **“这个人是谁”** 这个信息。
#
# * 第一个小朋友记住自己的名字。
# * “鼓”响后，他跑去后面 `k` 个位置，但他不是直接站下，而是把“后面第 k 个位置小朋友的名字”带回来，然后自己站到那个位置上。
# * 现在他手里是“后面第 k 个小朋友的名字”，他去那个小朋友原来的位置，重复上面的动作：记住那位置小朋友的名字，去他后面第 k 个位置，把再后面第 k 个位置的小朋友的名字带回来，自己站过去。
# * 这样一直传下去，名字就像花一样在链条里传递，而小朋友们则按照这个链条依次向前一个空位（或者说被占位的人）的位置站过去。
# * 最后，第一个小朋友最初记住的那个名字，会放到这个链条最终绕回来的那个位置上。
# * 因为可能有不止一个这样的传名字链条（取决于总人数和 `k`），我们要一个一个链条地搞定，直到所有小朋友都换过一次位置为止（用计数器判断）。
#
# **过目不忘的记忆点：**
#
# 1.  **记住要被“顶替”的人！** (先存 `prev = nums[start]`)
# 2.  **链条式占位！** ( `nums[next_pos], prev = prev, nums[next_pos]` 这行是核心，把下一个人挪过来，同时记住被挤走的是谁)
# 3.  **转圈回到原点才算一环！** (`if current == start: break`)
# 4.  **数人头确保都挪了！** (`count < n`)
#
# 希望这个解释能让你一目了然！

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        count = 0

        for start in range(n):
            if count >= n:
                break
            current = start
            prev = nums[start]
            while True:
                next_pos = (current + k) % n
                nums[next_pos], prev = prev, nums[next_pos]
                current = next_pos
                count += 1
                if current == start:
                    break

        return nums


# #### 执行示例
# - **调用栈**：
#   `rotate([1,2,3,4,5,6], 2)`
#   1. `start=0`：1→3→5→1（环1，`count=3`）。
#   2. `start=1`：2→4→6→2（环2，`count=6`）。
#   最终结果：`[5,6,1,2,3,4]`。
#
# - **边界测试**：
#   - `nums = [1], k=5`：直接跳过（单元素无需移动）。
#   - `nums = [1,2,3,4], k=2`：两轮环（1→3→1 和 2→4→2）。
#
# #### 复杂度分析
# - 时间：`O(n)`（每个元素移动一次）。
# - 空间：`O(1)`。
#
# #### 优缺点
# - **优点**：理论最优，无需额外空间。
# - **缺点**：逻辑复杂，易出错。
#
#
# **最优选择**：三次反转法。
# - **理由**：满足所有题目要求，代码简洁，适合面试。
# - **关键点**：解释反转的数学原理（轮转即“尾部变头部”）。
# def rotate(self, nums: List[int], k: int) -> None:
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     n = len(nums)
#     k = k % n  # 处理 k > n 的情况
#
#     def reverse(start, end):
#         while start < end:
#             nums[start], nums[end] = nums[end], nums[start]
#             start += 1
#             end -= 1
#
#     reverse(0, n - 1)  # 全体反转
#     reverse(0, k - 1)  # 前 k 个反转
#     reverse(k, n - 1)  # 剩余反转


test_cases = [
    {
        "method": "rotate",
        "nums": [1, 2, 3, 4, 5, 6, 7],
        "k": 3,
        "expected": [5, 6, 7, 1, 2, 3, 4],
        "case_id": 1,
        "description": "Standard case with positive values"
    },
    {
        "method": "rotate",
        "nums": [-1, -100, 3, 99],
        "k": 2,
        "expected": [3, 99, -1, -100],
        "case_id": 2,
        "description": "Standard case with negative values"
    },
    {
        "method": "rotate",
        "nums": [1, 2, 3, 4, 5, 6],
        "k": 0,

        "expected": [1, 2, 3, 4, 5, 6],
        "case_id": 3,
        "description": "Edge case: k = 0 (no rotation)"
    },
    {
        "method": "rotate",
        "nums": [1, 2, 3, 4, 5, 6],
        "k": 6,

        "expected": [1, 2, 3, 4, 5, 6],
        "case_id": 4,
        "description": "Edge case: k = array length (full rotation)"
    },
    {
        "method": "rotate",
        "nums": [1, 2, 3, 4, 5, 6],
        "k": 8,

        "expected": [5, 6, 1, 2, 3, 4],
        "case_id": 5,
        "description": "Edge case: k > array length"
    },
    {
        "method": "rotate",
        "nums": [1],
        "k": 1,

        "expected": [1],
        "case_id": 6,
        "description": "Edge case: Single element array"
    },
    {
        "method": "rotate",
        "nums": [1, 2],
        "k": 3,

        "expected": [2, 1],
        "case_id": 7,
        "description": "Edge case: k > array length with small array"
    }
]

run_tests()
