# 160. Intersection of Two Linked Lists

# Given the heads of two singly linked-lists `headA` and `headB`, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return `null`.
#
# For example, the following two linked lists begin to intersect at node `c1`:
#
# ```
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# ```
#
# The test cases are generated such that there are no cycles in the linked structure.
#
# **Note:** that the linked lists must retain their original structure after the function returns.
#
# **Follow up:**
# - Could you write a solution that runs in `O(n)` time and uses only `O(1)` space?
#
# ### Constraints:
# - The number of nodes of each linked list is in the range `[0, 3 * 10^4]`.
# - `-10^9 <= Node.val <= 10^9`
# - The lists may or may not intersect.
#
# ### Example 1:
# ```
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Intersected at '8'
# Explanation: The intersected node's value is 8 (note that this must be the same node, not just the same value).
#              The first linked list has 2 nodes before the intersection, and the second has 3 nodes before it.
# ```
#
# ### Example 2:
# ```
# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# Output: Intersected at '2'
# Explanation: The intersected node's value is 2.
#              The first linked list has 3 nodes before the intersection, and the second has 1 node before it.
# ```
#
# ### Example 3:
# ```
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: null
# Explanation: The two linked lists do not intersect, so return null.
# ```

from test.test_suite import run_tests
from typing import *
from libs.linked_list import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        currA = headA
        currB = headB

        # while currA != currB:
        #     currA = currA.next if currA.next else headB
        #     currB = currB.next if currB.next else headA
        # 如果用以上的代码代码，在某些情况下无法在合理时间内终止（或需要极多步骤），尤其是在无交点或链表长度差异较大的情况下。以下是详细分析：
        #
        # 1. 无交点的情况
        # 假设：
        #
        # 链表A有a个节点，长度为a。
        # 链表B有b个节点，长度为b。
        # 没有交点（c = 0）。
        #
        # 正确代码行为：
        #
        # currA遍历链表A（a步），到达None，切换到headB，遍历链表B（b步），到达None。
        # currB遍历链表B（b步），到达None，切换到headA，遍历链表A（a步），到达None。
        # 总步骤：a + b，currA和currB同时到达None，currA == currB == None，循环终止。
        #
        # 你的代码行为：
        #
        # currA遍历链表A，直到最后一个节点（a-1步，currA.next == None），切换到headB。
        # currA遍历链表B，直到最后一个节点（b-1步，currA.next == None），再次切换到headB。
        # currB类似：遍历链表B到最后一个节点（b-1步），切换到headA，遍历链表A到最后一个节点（a-1步），再次切换到headA。
        # 问题：当currA和currB切换后，它们继续在链表B和链表A之间循环切换，每次遍历到最后一个节点就切换。由于没有交点，currA和currB永远不会指向同一节点。
        # 结果：你的代码可能陷入无限循环，因为切换条件currA.next == None使得指针反复在两个链表之间跳转，而没有明确的终止条件（不像正确代码那样到达None后终止）。

        # 2. 有交点的情况
        # 假设：
        #
        # 链表A：a个独有节点 + c个公共节点。
        # 链表B：b个独有节点 + c个公共节点。
        # 交点是公共部分的第一个节点。
        # 正确代码行为：
        #
        # currA遍历a + c + b步，currB遍历b + c + a步，两个指针在交点相遇，循环终止。
        # 总步骤：a + b + c。
        # 你的代码行为：
        #
        # currA遍历链表A到最后一个节点（a + c - 1步，currA.next == None），切换到headB，继续遍历。
        # currB遍历链表B到最后一个节点（b + c - 1步，currB.next == None），切换到headA。
        # 问题：由于切换发生在最后一个节点（而不是None），指针可能需要额外遍历多次才能对齐到交点。你的代码仍然可能找到交点，但需要更多步骤（例如，currA和currB可能在切换后未正确对齐，需要多次遍历公共部分）。
        # 结果：即使能找到交点，你的代码可能需要额外的循环（例如O(a + b + c + k)，其中k是额外遍历的步数），这在a、b或c较大时会导致性能问题。

        while currA != currB:  # Python里： None == None: True
            currA = currA.next if currA else headB
            currB = currB.next if currB else headA

        return currA


# 要证明双指针法中以下代码不会进入死循环：
#
# ```python
# while currA != currB:
#     currA = currA.next if currA else headB
#     currB = currB.next if currB else headA
# ```
#
# 我们需要分析算法的逻辑，确保循环总会在有限步骤内终止（即`currA`和`currB`最终相等）。以下是用清晰的中文逐步证明，结合数学和逻辑分析。
#
# ---
#
# ### 问题背景
# LeetCode #160要求找到两个单向链表`headA`和`headB`的交点（如果存在）。双指针法让两个指针`currA`和`currB`分别从`headA`和`headB`开始遍历，当一个指针到达链表末尾（`None`）时，切换到另一个链表的头部继续遍历，直到`currA == currB`（指向同一节点或都为`None`）。
#
# 循环终止的条件是`currA == currB`，因此要证明不会死循环，我们需要证明：
# 1. 循环总会在有限步骤内使`currA == currB`。
# 2. 不会出现`currA`和`currB`永远不相等的情况。
#
# ---
#
# ### 证明
#
# 我们分两种情况分析：**链表有交点**和**链表无交点**，并在每种情况下证明循环会终止。以下假设在循环开始前已检查`headA`和`headB`不全为空（因为如果任一为空，函数会直接返回`None`，不会进入循环）。
#
# #### 情况1：链表有交点
#
# 假设：
# - 链表A（从`headA`开始）的结构为：`a`个独有节点 + `c`个公共节点（交点后的部分）。
# - 链表B（从`headB`开始）的结构为：`b`个独有节点 + `c`个公共节点。
# - 交点是公共部分的第一个节点，`c ≥ 1`（因为有交点）。
# - 链表总长度：链表A长度为`a + c`，链表B长度为`b + c`。
#
# **双指针遍历过程**：
# - `currA`从`headA`开始，遍历链表A（`a + c`个节点），到达末尾（`None`）后切换到`headB`，继续遍历链表B（`b + c`个节点）。
# - `currB`从`headB`开始，遍历链表B（`b + c`个节点），到达末尾后切换到`headA`，继续遍历链表A（`a + c`个节点）。
# - 每一步，`currA`和`currB`都向前移动一个节点（如果当前指针非空，移动到`next`；如果为空，切换到另一个链表头部）。
#
# **路径长度分析**：
# - `currA`的总遍历路径：`headA -> 交点 -> 末尾 -> headB -> 交点`。
#   - 第一阶段：遍历链表A（`a + c`步）。
#   - 第二阶段：切换到`headB`，遍历链表B直到交点（`b`步，因为交点是链表B的第`b+1`个节点）。
#   - 总步骤：`a + c + b`。
# - `currB`的总遍历路径：`headB -> 交点 -> 末尾 -> headA -> 交点`。
#   - 第一阶段：遍历链表B（`b + c`步）。
#   - 第二阶段：切换到`headA`，遍历链表A直到交点（`a`步）。
#   - 总步骤：`b + c + a`。
# - 关键点：`a + c + b == b + c + a`，即`currA`和`currB`在遍历`a + b + c`步后都到达交点。
#
# **终止证明**：
# - 在第`a + b + c`步，`currA`和`currB`同时到达交点（同一个节点对象），此时`currA == currB`。
# - 因为`a`、`b`、`c`都是有限的非负整数（题目约束：节点数在`[0, 3*10^4]`），`a + b + c`是有限值。
# - 循环在有限步骤（`a + b + c`）内终止，`currA == currB`，返回交点。
#
# **结论**：当链表有交点时，循环会在有限步骤内终止，不会死循环。
#
# #### 情况2：链表无交点
#
# 假设：
# - 链表A（从`headA`开始）有`a`个节点，长度为`a`。
# - 链表B（从`headB`开始）有`b`个节点，长度为`b`。
# - 没有交点，意味着链表A和链表B没有任何共享节点，`c = 0`。
#
# **双指针遍历过程**：
# - `currA`遍历链表A（`a`步），到达`None`后切换到`headB`，遍历链表B（`b`步）。
# - `currB`遍历链表B（`b`步），到达`None`后切换到`headA`，遍历链表A（`a`步）。
# - 每一步，`currA`和`currB`都向前移动。
#
# **路径长度分析**：
# - `currA`的路径：`headA -> None -> headB -> None`。
#   - 总步骤：`a + b`（链表A长度`a` + 链表B长度`b`）。
# - `currB`的路径：`headB -> None -> headA -> None`。
#   - 总步骤：`b + a`（链表B长度`b` + 链表A长度`a`）。
# - 关键点：`a + b == b + a`，即`currA`和`currB`在遍历`a + b`步后都到达`None`。
#
# **终止证明**：
# - 在第`a + b`步，`currA`和`currB`同时到达`None`（因为`currA`遍历完链表A和B，`currB`遍历完链表B和A）。
# - 此时，`currA == currB == None`，满足循环退出条件`currA == currB`。
# - 因为`a`和`b`都是有限的非负整数（节点数在`[0, 3*10^4]`），`a + b`是有限值。
# - 循环在有限步骤（`a + b`）内终止，返回`None`。
#
# **结论**：当链表无交点时，循环会在有限步骤内终止，不会死循环。
#
# #### 边界情况
# - **空链表**：如果`headA`或`headB`为空，函数在进入循环前返回`None`（如代码中的`if not headA or not headB: return None`）。如果一个链表为空（例如`a = 0`），另一个不空（`b > 0`），则：
#   - `currA`从空链表开始，立即切换到`headB`；`currB`遍历链表B后切换到空链表。
#   - 类似于无交点情况，`currA`和`currB`会在有限步骤（`b`步）都到达`None`，循环终止。
# - **两个链表长度相等且无交点**：如果`a == b`，`currA`和`currB`会在遍历完各自链表（`a`步）后同时到达`None`，循环终止。
# - **题目约束**：题目保证链表无环（“测试用例保证链表结构无环”），因此不会出现指针陷入无限循环的情况。
#
# ---
#
# ### 为什么不会死循环？
# - **有交点**：`currA`和`currB`会在遍历`a + b + c`步后相遇于交点，步骤数有限。
# - **无交点**：`currA`和`currB`会在遍历`a + b`步后相遇于`None`，步骤数有限。
# - **无环保证**：题目明确链表无环，指针不会在链表内循环。
# - **有限节点**：链表节点数有限（`[0, 3*10^4]`），总遍历路径（`a + b`或`a + b + c`）始终有限。
#
# 循环的每次迭代都让`currA`和`currB`向前移动一步，且总路径长度有限，因此`currA`和`currB`必然在有限步骤内相等（ либо在交点，либо在`None`），循环必然终止。
#
# ---
#
# ### 数学视角（可选）
# 从数学角度看，双指针法将两个指针的遍历路径“对齐”：
# - 有交点时，`currA`走`a + c + b`，`currB`走`b + c + a`，路径长度相等，交点是公共节点。
# - 无交点时，`currA`走`a + b`，`currB`走`b + a`，路径长度相等，终点是`None`。
# - 循环的每次迭代相当于在有限状态空间（链表A + 链表B的节点集合）中移动一步，且状态数有限（最多`a + b + c`或`a + b`），因此不可能无限循环。
#
# ---
#
# ### 结论
# 无论链表是否有交点，双指针法的循环总会在有限步骤内终止（最多`a + b + c`或`a + b`步），因为：
# 1. 指针总会相遇（在交点或`None`）。
# 2. 链表节点数有限，无环。
# 3. 每次迭代都严格向前移动。
#


test_cases = [
    {
        "method": "getIntersectionNode",
        "headA": [4, 1, 8, 4, 5],
        "headB": [5, 6, 1, 8, 4, 5],
        "skipA": 2,
        "skipB": 3,
        "expected": 8,
        "case_id": 1,
        "description": "Lists intersect at node with value 8"
    },
    {
        "method": "getIntersectionNode",
        "headA": [1, 9, 1, 2, 4],
        "headB": [3, 2, 4],
        "skipA": 3,
        "skipB": 1,
        "expected": 2,
        "case_id": 2,
        "description": "Lists intersect at node with value 2"
    },
    {
        "method": "getIntersectionNode",
        "headA": [2, 6, 4],
        "headB": [1, 5],
        "skipA": 3,
        "skipB": 2,
        "expected": None,
        "case_id": 3,
        "description": "No intersection between lists"
    },
    {
        "method": "getIntersectionNode",
        "headA": [],
        "headB": [],
        "skipA": 0,
        "skipB": 0,
        "expected": None,
        "case_id": 4,
        "description": "Both lists are empty"
    },
    {
        "method": "getIntersectionNode",
        "headA": [1],
        "headB": [1],
        "skipA": 1,
        "skipB": 1,
        "expected": None,
        "case_id": 5,
        "description": "Single node lists with no intersection"
    },
    {
        "method": "getIntersectionNode",
        "headA": [1, 2, 3],
        "headB": [4, 5, 6, 7, 8, 9],
        "skipA": 3,
        "skipB": 6,
        "expected": None,
        "case_id": 6,
        "description": "Lists of different lengths with no intersection"
    }
]

run_tests()
