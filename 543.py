# 543.py
from test.test_suite import run_tests

from typing import Optional
from libs.tree import TreeNode, tree_to_list


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def depth(node):
            if not node:
                return 0

            left_depth = depth(node.left)  # 计算左子树最大深度
            right_depth = depth(node.right)  # 计算右子树最大深度

            self.diameter = max(self.diameter, left_depth + right_depth)  # 计算直径

            return 1 + max(left_depth, right_depth)

        depth(root)
        return self.diameter
    # 对于 root = [1, 2, 3, 4, 5]，二叉树结构如下：


#     1
#    / \
#   2   3
#  / \
# 4   5

# 计算 depth()：
# 	•	depth(4) = 1
# 	•	depth(5) = 1
# 	•	depth(3) = 1
# 	•	depth(2) = 1 + max(1, 1) = 2
# 	•	depth(1) = 1 + max(2, 1) = 3

test_cases = [
    {
        "method": "diameterOfBinaryTree",
        "root": [1, 2, 3, 4, 5],
        "expected": 3,
        "case_id": 1,
        "description": "Balanced binary tree with two subtrees"
    },
    {
        "method": "diameterOfBinaryTree",
        "root": [1, 2],
        "expected": 1,
        "case_id": 2,
        "description": "Simple binary tree with just two nodes"
    }, {
        "method": "diameterOfBinaryTree",
        "root": [1],
        "expected": 0,
        "case_id": 3,
        "description": "Single node tree (edge case)"
    }, {
        "method": "diameterOfBinaryTree",
        "root": [1, 2, None, 3, None, 4, None, 5],
        "expected": 4,
        "case_id": 4,
        "description": "Highly unbalanced tree (linked list shape)"
    }, {
        "method": "diameterOfBinaryTree",
        "root": [1, 2, 3, 4, 5, None, None, 6, 7],
        "expected": 4,
        "case_id": 5,
        "description": "Deep tree with multiple levels"
    }, {
        "method": "diameterOfBinaryTree",
        "root": [1, None, 2, None, 3, None, 4],
        "expected": 3,
        "case_id": 6,
        "description": "Right-heavy skewed tree"
    }
]
run_tests()
