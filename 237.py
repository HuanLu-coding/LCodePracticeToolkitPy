# 237. Delete Node in a Linked List

# There is a singly-linked list `head` and we want to delete a node `node` in it.
#
# You are given the node to be deleted `node`. You will **not** be given access to the first node of `head`.
#
# All the values of the linked list are **unique**, and it is guaranteed that the given node `node` is not the last node in the linked list.
#
# Delete the given node. Note that by deleting the node, we mean that:
# - The value of the given node should not exist in the linked list.
# - The number of nodes in the linked list should decrease by one.
# - All the values before the node should remain in their original order.
# - All the values after the node should remain in their original order.
#
# ### Constraints:
# - The number of nodes in the given list is in the range `[2, 1000]`.
# - `-1000 <= Node.val <= 1000`
# - The value of each node in the list is **unique**.
# - The node to be deleted is **in the list** and is **not a tail node**.
#
# ### Example 1:
# ```
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
# ```
#
# ### Example 2:
# ```
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
# ```

from test.test_suite import run_tests
from typing import *
from libs.linked_list import ListNode


class Solution:
    def deleteNode(self, node: Optional[ListNode]) -> None:
        pass


test_cases = [
    {
        "method": "deleteNode",
        "head": [4, 5, 1, 9],
        "node": 5,
        "expected": [4, 1, 9],
        "case_id": 1,
        "description": "Delete second node in a four-node list"
    },
    {
        "method": "deleteNode",
        "head": [4, 5, 1, 9],
        "node": 1,
        "expected": [4, 5, 9],
        "case_id": 2,
        "description": "Delete third node in a four-node list"
    },
    {
        "method": "deleteNode",
        "head": [1, 2],
        "node": 1,
        "expected": [2],
        "case_id": 3,
        "description": "Delete first node in a two-node list (minimum size)"
    },
    {
        "method": "deleteNode",
        "head": [1, 2, 3],
        "node": 2,
        "expected": [1, 3],
        "case_id": 4,
        "description": "Delete middle node in a three-node list"
    },
    {
        "method": "deleteNode",
        "head": [-1000, 0, 1000],
        "node": 0,
        "expected": [-1000, 1000],
        "case_id": 5,
        "description": "Delete node with value 0 in a list with extreme values"
    },
    {
        "method": "deleteNode",
        "head": [1, 2, 3, 4, 5],
        "node": 4,
        "expected": [1, 2, 3, 5],
        "case_id": 6,
        "description": "Delete second-to-last node in a five-node list"
    }
]

run_tests()
