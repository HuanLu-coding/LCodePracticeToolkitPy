from test.test_suite import run_tests

# 82. Remove Duplicates from Sorted List II

# Given the `head` of a sorted linked list, *delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list*. Return *the head of the modified linked list*.
#
# ### Constraints:
# - The number of nodes in the list is in the range `[0, 300]`.
# - `-100 <= Node.val <= 100`
# - The list is guaranteed to be **sorted** in ascending order.
#
# ### Example 1:
# ```
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
# Explanation: The nodes with values 3 and 4 appear multiple times, so all nodes with these values are removed.
# ```
#
# ### Example 2:
# ```
# Input: head = [1,1,1,2,3]
# Output: [2,3]
# Explanation: The node with value 1 appears multiple times, so all nodes with value 1 are removed.
# ```
#
# ### Example 3:
# ```
# Input: head = [1,1]
# Output: []
# Explanation: All nodes have value 1, so all nodes are removed.
# ```


from typing import *
from libs.linked_list import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dh = ListNode(0)  # 哑节点值任意
        dh.next = head
        prev, curr = dh, head

        while curr and curr.next:
            if curr.val == curr.next.val:  # 发现重复
                dp_val = curr.val
                # 跳过所有值为dp_val的节点
                while curr and curr.val == dp_val:
                    curr = curr.next
                prev.next = curr  # 连接到第一个非重复节点
            else:
                prev = prev.next  # 无重复，移动prev
                curr = curr.next

        return dh.next


test_cases = [
    {
        "method": "deleteDuplicates",
        "head": [1, 2, 3, 3, 4, 4, 5],
        "expected": [1, 2, 5],
        "case_id": 1,
        "description": "List with multiple duplicates in middle"
    },
    {
        "method": "deleteDuplicates",
        "head": [1, 1, 1, 2, 3],
        "expected": [2, 3],
        "case_id": 2,
        "description": "List with duplicates at the start"
    },
    {
        "method": "deleteDuplicates",
        "head": [1, 1],
        "expected": [],
        "case_id": 3,
        "description": "Edge case: List with all duplicates (minimum length)"
    },
    {
        "method": "deleteDuplicates",
        "head": [],
        "expected": [],
        "case_id": 4,
        "description": "Edge case: Empty list"
    },
    {
        "method": "deleteDuplicates",
        "head": [1],
        "expected": [1],
        "case_id": 5,
        "description": "Edge case: Single node list (no duplicates)"
    },
    {
        "method": "deleteDuplicates",
        "head": [-100, -100, 0, 0, 100],
        "expected": [100],
        "case_id": 6,
        "description": "Edge case: List with extreme values and duplicates"
    }
]

run_tests()
