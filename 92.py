# 92. Reverse Linked List II

# Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return *the reversed list*.
#
# ### Constraints:
# - The number of nodes in the list is `n`.
# - `1 <= n <= 500`
# - `-500 <= Node.val <= 500`
# - `1 <= left <= right <= n`
#
# **Follow up**: Could you do it in one pass?
#
# ### Example 1:
# ```
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Explanation: The nodes from position 2 to 4 (values 2,3,4) are reversed.
# ```
#
# ### Example 2:
# ```
# Input: head = [5], left = 1, right = 1
# Output: [5]
# Explanation: Only one node, no reversal needed.
# ```
#
# ### Example 3:
# ```
# Input: head = [3,5], left = 1, right = 2
# Output: [5,3]
# Explanation: The entire list (positions 1 to 2) is reversed.
# ```

from test.test_suite import run_tests
from typing import *
from libs.linked_list import ListNode


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        dummyHead.next = head
        curr = head
        prev = dummyHead
        cnt = 1

        while cnt < left:
            curr = curr.next
            prev = prev.next
            cnt += 1

        # 反转从left到right的节点
        for _ in range(right - left):
            # 每次迭代，我们取当前节点（`curr`）的下一个节点（`temp`），将其插入到`prev`之后，作为新的反转子链表头部。
            # 在这个过程中，`prev`始终指向反转子链表之前的节点（第`left-1`个节点），它的`next`指针不断更新，指向反转后子链表的头部。
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp  # `prev`指向新的子链表头部，即`temp`
            # 1. `prev`固定在第`left-1`个节点，作为反转子链表的锚点。
            # 2. 反转通过更新`prev.next`和`temp.next`完成，`prev`只需保持指向不变。
            # 3. 移动`curr`（通过`curr.next = temp.next`）足够处理反转部分的节点。

        return dummyHead.next


# ### 对比其他反转方法
#
# 在反转整个链表（LeetCode #206）中，通常使用`prev = curr`来移动`prev`，因为需要反转所有节点，最终`prev`指向新头部。但在#92中：
# - 只反转部分链表，`prev`必须固定在第`left-1`个节点，作为连接点。
# - 反转子链表的头部通过`prev.next`动态更新，无需移动`prev`。
#
# ### 为什么不需要移动`prev`？
#
# 简单来说，`prev`在反转过程中不需要移动，因为它的作用是**固定指向第`left-1`个节点**，作为反转子链表的“锚点”。它的`next`指针会被更新，指向反转后子链表的头部，而不需要改变`prev`本身的位置。以下是详细解释：
#
# #### 1. **反转过程的核心逻辑**
# 反转链表的关键是将节点的`next`指针重新指向前一个节点，同时调整链表的连接。考虑一个简单的链表反转（例如反转`2->3->4`变成`4->3->2`）：
# - 每次迭代，我们取当前节点（`curr`）的下一个节点（`temp`），将其插入到`prev`之后，作为新的反转子链表头部。
# - 具体步骤：
#   - 保存`temp = curr.next`（下一个要反转的节点）。
#   - 更新`curr.next = temp.next`（让`curr`跳过`temp`，指向后续节点）。
#   - 将`temp`插入到`prev`和`prev.next`之间：
#     - `temp.next = prev.next`（`temp`指向当前子链表头部）。
#     - `prev.next = temp`（`prev`指向新的子链表头部，即`temp`）。
#
# 在这个过程中，`prev`始终指向反转子链表之前的节点（第`left-1`个节点），它的`next`指针不断更新，指向反转后子链表的头部。
#
# #### 2. **为什么`prev`保持不动？**
# - **角色定位**：`prev`的作用是标记反转子链表的起点前一个节点（第`left-1`个节点）。它用于：
#   - 在反转开始前，连接到反转子链表的头部（`prev.next`）。
#   - 在反转结束后，确保反转后的子链表正确连接到链表的前半部分。
# - **动态更新`prev.next`**：在每次迭代中，`prev.next`被更新为新反转的节点（`temp`），这实际上是在构建反转后的子链表头部，而不需要改变`prev`的指向。
# - **移动`curr`就足够**：`curr`在每次迭代中向前移动（通过`curr.next = temp.next`），负责处理下一个要反转的节点。`prev`只需要保持固定，作为插入新节点时的参考点。
#
# 如果我们移动`prev`（例如`prev = prev.next`），`prev`会跟随反转后的子链表头部移动，最终可能指向反转子链表的中间或末尾，导致无法正确连接到链表的前半部分。
#
# #### 3. **逐步模拟反转过程**
# 以测试用例`head = [1,2,3,4,5], left = 2, right = 4`为例，模拟反转过程，说明`prev`为何不动：
#
# **初始状态**：
# - 链表：`dummyHead -> 1 -> 2 -> 3 -> 4 -> 5`。
# - 定位后：`prev = 1`, `curr = 2`（第`left=2`个节点）。
# - 子链表`2->3->4`需要反转为`4->3->2`，最终链表为`1->4->3->2->5`。
#
# **循环执行**（`for i in range(right - left) = range(2)`）：
# - **第一次迭代**（反转节点`3`）：
#   - 初始：`prev = 1`, `curr = 2`, 链表：`1 -> 2 -> 3 -> 4 -> 5`.
#   - `temp = curr.next = 3`.
#   - `curr.next = temp.next`, 即`2.next = 4`（`curr`跳过`3`）。
#     - 链表：`1 -> 2 -> 4 -> 5, 3 (孤立)`.
#   - `temp.next = prev.next`, 即`3.next = 2`（`temp`指向当前子链表头部）。
#     - 链表：`1 -> 2 -> 4 -> 5, 3 -> 2`.
#   - `prev.next = temp`, 即`1.next = 3`（`prev`指向新头部`3`）。
#     - 链表：`1 -> 3 -> 2 -> 4 -> 5`.
#   - **状态**：`prev = 1`（不动），`curr = 2`, 反转后子链表为`3->2`.
#
# - **第二次迭代**（反转节点`4`）：
#   - 初始：`prev = 1`, `curr = 2`, 链表：`1 -> 3 -> 2 -> 4 -> 5`.
#   - `temp = curr.next = 4`.
#   - `curr.next = temp.next`, 即`2.next = 5`。
#     - 链表：`1 -> 3 -> 2 -> 5, 4 (孤立)`.
#   - `temp.next = prev.next`, 即`4.next = 3`.
#     - 链表：`1 -> 3 -> 2 -> 5, 4 -> 3`.
#   - `prev.next = temp`, 即`1.next = 4`.
#     - 链表：`1 -> 4 -> 3 -> 2 -> 5`.
#   - **状态**：`prev = 1`（仍不动），`curr = 2`, 反转后子链表为`4->3->2`.
#
# **循环结束**：
# - 链表：`1 -> 4 -> 3 -> 2 -> 5`，正确反转了`2->3->4`为`4->3->2`。
# - `prev`始终指向节点`1`（第`left-1`个节点），其`next`指针从`2`更新为`3`，再更新为`4`，正确构建了反转子链表。
#
# **关键观察**：
# - `prev`保持固定在节点`1`，通过更新`prev.next`来插入新反转的节点（`3`, 然后`4`）。
# - `curr`负责遍历反转部分的剩余节点，`curr.next`跳过当前处理的节点。
# - 不需要移动`prev`，因为它的角色是作为反转子链表的“锚点”，确保反转后的头部正确连接到`prev.next`。
#
#
# 正确逻辑依赖于`prev`固定在第`left-1`个节点，动态更新`prev.next`来构建反转子链表。
#
# #### 5. **为什么`for`循环次数是`right - left`？**
# - 需要反转的节点数是`right - left + 1`（从第`left`到第`right`）。
# - 每次迭代处理一个节点（将`curr.next`插入到`prev.next`），但第一次反转后，`curr`已经指向正确的位置，只需处理`right - left`次插入操作。
# - 例如，`left=2, right=4`，需要反转`2->3->4`（3个节点），但只需2次插入（`3`和`4`），因为`curr`初始已在`2`。
#
# ---
#
# ### 图形化解释
#
# 初始链表：`dummyHead -> 1 -> 2 -> 3 -> 4 -> 5`, `left=2, right=4`。
#
# **第一次迭代**：
# - 之前：`1 -> 2 -> 3 -> 4 -> 5`, `prev=1, curr=2`.
# - 之后：`1 -> 3 -> 2 -> 4 -> 5`, `prev=1, curr=2`.
# - `3`被插入到`1`和`2`之间，`prev`不动。
#
# **第二次迭代**：
# - 之前：`1 -> 3 -> 2 -> 4 -> 5`, `prev=1, curr=2`.
# - 之后：`1 -> 4 -> 3 -> 2 -> 5`, `prev=1, curr=2`.
# - `4`被插入到`1`和`3`之间，`prev`仍不动。
#
# 最终：`1 -> 4 -> 3 -> 2 -> 5`，`prev`始终在`1`，确保`prev.next`指向反转子链表头部。
#
# ---
#

#
# ---
#
# ### 结论
#
# 在代码片段中，不移动`prev`是因为：
# 1. `prev`固定在第`left-1`个节点，作为反转子链表的锚点。
# 2. 反转通过更新`prev.next`和`temp.next`完成，`prev`只需保持指向不变。
# 3. 移动`curr`（通过`curr.next = temp.next`）足够处理反转部分的节点。


test_cases = [
    {
        "method": "reverseBetween",
        "head": [1, 2, 3, 4, 5],
        "left": 2,
        "right": 4,
        "expected": [1, 4, 3, 2, 5],
        "case_id": 1,
        "description": "Reverse middle portion of a five-node list"
    },
    {
        "method": "reverseBetween",
        "head": [5],
        "left": 1,
        "right": 1,
        "expected": [5],
        "case_id": 2,
        "description": "Edge case: Single node list, no reversal needed"
    },
    {
        "method": "reverseBetween",
        "head": [3, 5],
        "left": 1,
        "right": 2,
        "expected": [5, 3],
        "case_id": 3,
        "description": "Edge case: Reverse entire two-node list"
    },
    {
        "method": "reverseBetween",
        "head": [1, 2, 3],
        "left": 1,
        "right": 1,
        "expected": [1, 2, 3],
        "case_id": 4,
        "description": "Edge case: Reverse only the first node (no change)"
    },
    {
        "method": "reverseBetween",
        "head": [-500, 0, 500],
        "left": 1,
        "right": 3,
        "expected": [500, 0, -500],
        "case_id": 5,
        "description": "Reverse entire list with extreme values"
    },
    {
        "method": "reverseBetween",
        "head": [1, 2, 3, 4, 5],
        "left": 1,
        "right": 5,
        "expected": [5, 4, 3, 2, 1],
        "case_id": 6,
        "description": "Reverse entire five-node list"
    }
]

run_tests()
