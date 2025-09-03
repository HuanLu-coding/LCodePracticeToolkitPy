# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# ### Constraints:
# - The number of nodes in each linked list is in the range `[1, 100]`.
# - `0 <= Node.val <= 9`
# - It is guaranteed that the list represents a number that does not have leading zeros.
#
# ### Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# ### Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# ### Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


from typing import *

from libs.linked_list import ListNode
from test.test_suite import run_tests


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 空间复杂度: O(1) 原地修改 (你的方案)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = l1
        curr1 = h1
        curr2 = l2
        carry = 0

        # Keep track of the last node in the result list
        last_node = curr1

        while curr1 and curr2:
            adding = curr1.val + curr2.val + carry
            if adding > 9:
                carry, val = divmod(adding, 10)
                curr1.val = val
            else:
                curr1.val = adding
                carry = 0

            last_node = curr1  # Track the last node
            curr1 = curr1.next
            curr2 = curr2.next

        # Handle the case when both lists end
        if not curr1 and not curr2:
            if carry > 0:
                last_node.next = ListNode(carry)
            return h1

        # Handle remaining nodes in either list
        if not curr1:  # l2 remains
            last_node.next = curr2
            curr1 = curr2

        # Process remaining nodes with carry
        while curr1:
            adding = curr1.val + carry
            if adding > 9:
                carry, val = divmod(adding, 10)
                curr1.val = val
            else:
                curr1.val = adding
                carry = 0

            last_node = curr1  # Keep tracking the last node
            curr1 = curr1.next

        # Add final carry node if needed
        if carry > 0:
            last_node.next = ListNode(carry)

        return h1


# 空间复杂度: O(max(n, m)) 创建新链表
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         curr = dummy
#         carry = 0
#
#         while l1 or l2 or carry:
#             x = l1.val if l1 else 0
#             y = l2.val if l2 else 0
#             total = x + y + carry
#             carry, val = divmod(total, 10)
#
#             curr.next = ListNode(val)
#             curr = curr.next
#
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#
#         return dummy.next


test_cases = [
    {
        "method": "addTwoNumbers",
        "l1": ListNode.from_list([2, 4, 3]),
        "l2": ListNode.from_list([5, 6, 4]),
        "expected": [7, 0, 8],
        "case_id": 1,
        "description": "Standard example: 342 + 465 = 807"
    },
    {
        "method": "addTwoNumbers",
        "l1": ListNode.from_list([0]),
        "l2": ListNode.from_list([0]),
        "expected": [0],
        "case_id": 2,
        "description": "Edge case: both numbers are zero"
    },
    {
        "method": "addTwoNumbers",
        "l1": ListNode.from_list([9, 9, 9, 9, 9, 9, 9]),
        "l2": ListNode.from_list([9, 9, 9, 9]),
        "expected": [8, 9, 9, 9, 0, 0, 0, 1],
        "case_id": 3,
        "description": "Different length lists with carry to new digit"
    },
    {
        "method": "addTwoNumbers",
        "l1": ListNode.from_list([1]),
        "l2": ListNode.from_list([9, 9, 9]),
        "expected": [0, 0, 0, 1],
        "case_id": 4,
        "description": "Edge case: single digit + multi-digit with carries"
    },
    {
        "method": "addTwoNumbers",
        "l1": ListNode.from_list([9]),
        "l2": ListNode.from_list([1, 9, 9, 9, 9, 9, 9, 9, 9, 9]),
        "expected": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        "case_id": 5,
        "description": "Edge case: large difference in list lengths with carries"
    },
    {
        "method": "addTwoNumbers",
        "l1": ListNode.from_list([5]),
        "l2": ListNode.from_list([5]),
        "expected": [0, 1],
        "case_id": 6,
        "description": "Edge case: simple addition with carry"
    },
    {
        "method": "addTwoNumbers",
        "l1": ListNode.from_list([1, 8]),
        "l2": ListNode.from_list([0]),
        "expected": [1, 8],
        "case_id": 7,
        "description": "One list is much shorter than the other"
    }
]

run_tests()
