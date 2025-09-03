# 83. Remove Duplicates from Sorted List
import math

# Given the `head` of a sorted linked list, *delete all duplicates such that each element appears only once*. Return *the head of the modified linked list*.
#
# ### Constraints:
# - The number of nodes in the list is in the range `[0, 300]`.
# - `-100 <= Node.val <= 100`
# - The list is guaranteed to be **sorted** in ascending order.
#
# ### Example 1:
# ```
# Input: head = [1,1,2]
# Output: [1,2]
# Explanation: The node with value 1 appears twice, so one of them is removed.
# ```
#
# ### Example 2:
# ```
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
# Explanation: The nodes with values 1 and 3 appear multiple times, so duplicates are removed.
# ```
#
# ### Example 3:
# ```
# Input: head = []
# Output: []
# Explanation: The list is empty, so no changes are needed.
# ```

from test.test_suite import run_tests
from typing import *
from libs.linked_list import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        curr = head

        while curr and curr.next:  # 确保curr和curr.next存在
            if curr.val == curr.next.val:  # 比较相邻节点
                curr.next = curr.next.next  # 跳过重复节点
            else:
                curr = curr.next  # 无重复，移动到下一节点

        return head


test_cases = [
    {
        "method": "deleteDuplicates",
        "head": [1, 1, 2],
        "expected": [1, 2],
        "case_id": 1,
        "description": "List with duplicates at the start"
    },
    {
        "method": "deleteDuplicates",
        "head": [1, 1, 2, 3, 3],
        "expected": [1, 2, 3],
        "case_id": 2,
        "description": "List with multiple duplicates"
    },
    {
        "method": "deleteDuplicates",
        "head": [],
        "expected": [],
        "case_id": 3,
        "description": "Edge case: Empty list"
    },
    {
        "method": "deleteDuplicates",
        "head": [1],
        "expected": [1],
        "case_id": 4,
        "description": "Edge case: Single node list (no duplicates)"
    },
    {
        "method": "deleteDuplicates",
        "head": [1, 1, 1, 1],
        "expected": [1],
        "case_id": 5,
        "description": "Edge case: List with all identical values"
    },
    {
        "method": "deleteDuplicates",
        "head": [-100, -100, 0, 100, 100],
        "expected": [-100, 0, 100],
        "case_id": 6,
        "description": "Edge case: List with extreme values and duplicates"
    }
]

run_tests()
