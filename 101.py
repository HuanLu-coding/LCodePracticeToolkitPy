# 101.py
from test.test_suite import run_tests

# # 101. Symmetric Tree
#
# Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
#
# ### Constraints:
# - The number of nodes in the tree is in the range `[0, 1000]`.
# - `-100 <= Node.val <= 100`
#
# ### Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#
# ### Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#

from typing import Optional
from libs.tree import TreeNode

# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         def isMirror(t1, t2):
#             if not t1 and not t2:
#                 return True
#             if not t1 or not t2 or t1.val != t2.val:
#                 return False
#             return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)  # 注意顺序
#
#         return isMirror(root.left, root.right)


# 4.  时间复杂度: O(N)，其中 N 是树中的节点数。每个节点最多被访问一次。这是最优的，因为必须检查所有节点才能确定对称性。
# 5.  空间复杂度: O(H)，其中 H 是树的高度。这是递归调用栈所使用的空间。在最坏情况下（树倾斜成链表），空间复杂度为 O(N)。在最佳情况下（完全平衡树），空间复杂度为 O(log N)。
#
# Solution 2: 层序遍历，每层检查是否回文
from collections import deque


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_values = []

            for _ in range(level_size):
                node = queue.popleft()
                # only append node.left and node.right to the queue if node is not None. This prevents None from being added to the queue unnecessarily.
                if node:
                    level_values.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    level_values.append(None)

            if level_values != level_values[::-1]:
                return False

        return True


test_cases = [
    {
        "method": "isSymmetric",
        "root": [1, 2, 2, 3, 4, 4, 3],
        "expected": True,
        "case_id": 1,
        "description": "Symmetric balanced binary tree"
    },
    {
        "method": "isSymmetric",
        "root": [1, 2, 2, None, 3, None, 3],
        "expected": False,
        "case_id": 2,
        "description": "Asymmetric tree with different inner nodes"
    },
    {
        "method": "isSymmetric",
        "root": [1],
        "expected": True,
        "case_id": 4,
        "description": "Single node tree (considered symmetric)"
    },
    {
        "method": "isSymmetric",
        "root": [1, 2, None],
        "expected": False,
        "case_id": 5,
        "description": "Asymmetric tree with only left child"
    },
    {
        "method": "isSymmetric",
        "root": [1, None, 2],
        "expected": False,
        "case_id": 6,
        "description": "Asymmetric tree with only right child"
    },
    {
        "method": "isSymmetric",
        "root": [1, 2, 2, 3, None, None, 3],
        "expected": True,
        "case_id": 7,
        "description": "Symmetric tree with null children"
    }
]

run_tests()
