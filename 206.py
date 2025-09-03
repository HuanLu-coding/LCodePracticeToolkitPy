# 206.py
from typing import Optional
from libs.linked_list import ListNode
from test.test_suite import run_tests


# 最优解：
# “存next，指prev，往前挪”
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # 初始为空，以保证掉头后尾巴是None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # 此时curr指向一个None，但是无所谓了。
        return prev


test_cases = [
    {
        "method": "reverseList",
        "head": [1, 2, 3, 4, 5],
        "expected": [5, 4, 3, 2, 1],
        "case_id": 1
    },
    {
        "method": "reverseList",
        "head": [1, 2],
        "expected": [2, 1],
        "case_id": 2
    },
    {
        "method": "reverseList",
        "head": [],
        "expected": [],
        "case_id": 3
    },
    {
        "method": "reverseList",
        "head": [5],
        "expected": [5],
        "case_id": 4
    },
    {
        "method": "reverseList",
        "head": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "expected": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "case_id": 5
    }
]
run_tests()
