# 148. Sort List

# Given the `head` of a linked list, return *the list after sorting it in **ascending order***.
#
# Follow up: Can you sort the linked list in $O(n \log n)$ time and $O(1)$ memory (i.e. constant space)?
#
# ### Constraints:
# - The number of nodes in the list is in the range `[0, 5 * 10^4]`.
# - $-10^5 \le Node.val \le 10^5$
#
# ### Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]
#
# ### Example 2:
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]
#
# ### Example 3:
# Input: head = []
# Output: []

from test.test_suite import run_tests
from typing import *
from libs.linked_list import ListNode

# https://g.co/gemini/share/06d650c10bf5
#
from typing import *
from libs.linked_list import ListNode

from typing import Optional


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Get list length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        dummy = ListNode(0, head)
        step = 1

        # Merge blocks of increasing size
        while step < length:
            curr = dummy.next
            tail = dummy

            while curr:
                left = curr
                right = self._split(left, step)
                curr = self._split(right, step) if right else None
                merged = self._merge(left, right)
                tail.next = merged
                while tail.next:
                    tail = tail.next

            step *= 2

        return dummy.next

    def _split(self, head: Optional[ListNode], step: int) -> Optional[ListNode]:
        if not head:
            return None
        for _ in range(step - 1):
            if not head.next:
                return None
            head = head.next
        next_head = head.next
        head.next = None
        return next_head

    def _merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left or right
        return dummy.next


test_cases = [
    {
        "method": "sortList",
        "head": [4, 2, 1, 3],
        "expected": [1, 2, 3, 4],
        "case_id": 1,
        "description": "Unsorted list"
    },
    {
        "method": "sortList",
        "head": [-1, 5, 3, 4, 0],
        "expected": [-1, 0, 3, 4, 5],
        "case_id": 2,
        "description": "List with negative values and zero"
    },
    {
        "method": "sortList",
        "head": [],
        "expected": [],
        "case_id": 3,
        "description": "Edge case: Empty list"
    },
    {
        "method": "sortList",
        "head": [1],
        "expected": [1],
        "case_id": 4,
        "description": "Edge case: Single element list"
    },
    {
        "method": "sortList",
        "head": [1, 2, 3, 4, 5],
        "expected": [1, 2, 3, 4, 5],
        "case_id": 5,
        "description": "Edge case: Already sorted list"
    },
    {
        "method": "sortList",
        "head": [5, 4, 3, 2, 1],
        "expected": [1, 2, 3, 4, 5],
        "case_id": 6,
        "description": "Edge case: Reverse sorted list"
    },
    {
        "method": "sortList",
        "head": [3, 1, 4, 1, 5, 9, 2, 6],
        "expected": [1, 1, 2, 3, 4, 5, 6, 9],
        "case_id": 7,
        "description": "List with duplicate values"
    },
    {
        "method": "sortList",
        "head": [2, 1],
        "expected": [1, 2],
        "case_id": 8,
        "description": "Two element unsorted list"
    }
]

run_tests()
