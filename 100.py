# 100.py
from test.test_suite import run_tests

from typing import Optional
from libs.tree import TreeNode
from libs.tree import tree_to_list


# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if p and not q:
#             return False
#         if not p and q:
#             return False
#         if not p and not q:
#             return True
#         if p and q:
#             if p.val != q.val:
#                 return False
#             return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# 最优解：
class OptimalSolution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 基本情况 1: 如果两个节点都为 None，则它们在此位置相同。
        if not p and not q:
            return True

        # 基本情况 2: 如果一个节点是 None 而另一个不是，或者它们的值不同，
        # 则它们不相同。这个检查隐式地处理了 p 和 q 都存在但值不同的情况。
        if not p or not q or p.val != q.val:
            return False

        # 递归步骤: 如果当前节点匹配，则递归地检查
        # 左子树 AND 右子树。两者必须都相同，
        # 整体树才算相同。
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# 4.  时间复杂度: O(N)，其中 N 是任一树中节点的最小数量。我们最多访问每个节点一次。这是最优的。
# 5.  空间复杂度: O(H)，其中 H 是树的最大高度，由递归调用栈引起。在最坏情况下（倾斜树），这是 O(N)。在最佳情况下（平衡树），这是 O(log N)。使用栈的迭代解决方案将具有相同的空间复杂度特性，但避免了潜在的递归深度限制。然而，为了清晰起见，通常首选递归解决方案。


test_cases = [
    {
        "method": "isSameTree",
        "p": [1, 2, 3],
        "q": [1, 2, 3],
        "expected": True,
        "case_id": 1,
        "description": "Identical trees with three nodes"
    },
    {
        "method": "isSameTree",
        "p": [1, 2],
        "q": [1, None, 2],
        "expected": False,
        "case_id": 2,
        "description": "Trees with different structure"
    },
    {
        "method": "isSameTree",
        "p": [1, 2, 1],
        "q": [1, 1, 2],
        "expected": False,
        "case_id": 3,
        "description": "Trees with same length but different values"
    },
    {
        "method": "isSameTree",
        "p": [],
        "q": [],
        "expected": True,
        "case_id": 4,
        "description": "Empty trees are considered the same"
    },
    {
        "method": "isSameTree",
        "p": [1],
        "q": [1],
        "expected": True,
        "case_id": 5,
        "description": "Single node trees with same value"
    },
    {
        "method": "isSameTree",
        "p": [1],
        "q": [2],
        "expected": False,
        "case_id": 6,
        "description": "Single node trees with different values"
    },
    {
        "method": "isSameTree",
        "p": [1, 2, 3, 4, 5],
        "q": [1, 2, 3, 4, 5],
        "expected": True,
        "case_id": 7,
        "description": "Larger identical trees with multiple levels"
    }
]

run_tests()
