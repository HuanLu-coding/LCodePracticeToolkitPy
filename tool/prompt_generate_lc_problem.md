Provide complete information about LeetCode problem #{problem_number}. Please include:

1. The original problem statement with all details (description, constraints, examples);
2. A Python v3.13.2 code template with the class Solution and method signature (empty function body);
3. At least 6 test cases (any numeric values have been carefully verified to ensure accuracy & at least 3 of these test
   cases are edge cases) in the structured format showed below;

## Special Instructions:

- If the problem involves a Tree data structure, add the import statement `from libs.tree import TreeNode` before the
  `class Solution:`
- If the problem involves a Linked List data structure, add the import statement `from libs.linked_list import ListNode`
  before the `class Solution:`

## Example Output Format

For reference, here's how the output should look for the LeetCode problem #110:

```
# 110. Balanced Binary Tree

# Given a binary tree, determine if it is height-balanced.
#
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
#
# ### Constraints:
# - The number of nodes in the tree is in the range `[0, 5000]`.
# - `-100 <= Node.val <= 100`
#
# ### Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#
# ### Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#
# ### Example 3:
# Input: root = []
# Output: true

from test.test_suite import run_tests
from typing import *
from libs.tree import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        pass


test_cases = [
    {
        "method": "isBalanced",
        "root": [3, 9, 20, None, None, 15, 7],
        "expected": True,
        "case_id": 1,
        "description": "Balanced binary tree"
    },
    {
        "method": "isBalanced",
        "root": [1, 2, 2, 3, 3, None, None, 4, 4],
        "expected": False,
        "case_id": 2,
        "description": "Unbalanced binary tree (deep on one side)"
    },
    {
        "method": "isBalanced",
        "root": [],
        "expected": True,
        "case_id": 3,
        "description": "Empty tree (considered balanced)"
    },
    {
        "method": "isBalanced",
        "root": [1],
        "expected": True,
        "case_id": 4,
        "description": "Single node tree (considered balanced)"
    },
    {
        "method": "isBalanced",
        "root": [1, 2, None, 3, None, 4, None, 5],
        "expected": False,
        "case_id": 5,
        "description": "Unbalanced skewed tree (left side)"
    },
    {
        "method": "isBalanced",
        "root": [1, None, 2, None, 3, None, 4, None, 5],
        "expected": False,
        "case_id": 6,
        "description": "Unbalanced skewed tree (right side)"
    },
    {
        "method": "isBalanced",
        "root": [1, 2, 2, 3, None, None, 3, 4, None, None, 4],
        "expected": True,
        "case_id": 7,
        "description": "Balanced tree with deeper but still balanced subtrees"
    }
]

run_tests()

```

Please provide the complete information for LeetCode problem #{problem_number} following above structure and format (
especially follow the `class Solution` and `test_cases` parts, and leave the solution function body empty for me to
implement).