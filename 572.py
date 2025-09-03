# 572.py
from test.test_suite import run_tests

from typing import Optional
from libs.tree import TreeNode
from collections import deque


# 遍历s的每个节点，检查子树。
# 树比较：用isSameTree判断两棵树是否相同。
# 边缘处理：特别注意空树逻辑。
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if not p and not q:
#             return True
#         if not p or not q:
#             return False
#         return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
#
#     # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#     #     if not subRoot:  # 空树是任何树的子树
#     #         return True
#     #     if not root:  # 非空树不是空树的子树
#     #         return False
#     #     return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,
#     #                                                                                                   subRoot)
#
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         if subRoot is None: return True
#         if root is None: return False
#
#         q = deque([root])
#
#         while q:
#             node = q.popleft()
#             if node.val == subRoot.val and self.isSameTree(node, subRoot):
#                 return True
#             if node.left:
#                 q.append(node.left)
#             if node.right:
#                 q.append(node.right)
#
#         return False
class Solution:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#"
        return f"[{root.val}]{self.serialize(root.left)}{self.serialize(root.right)}"

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        root_str = self.serialize(root)
        sub_str = self.serialize(subRoot)
        return sub_str in root_str


# 代码解释
# 序列化函数：
# 递归遍历树，每个非空节点格式为 ^val，空节点标记为 #。
# 结果用逗号拼接成字符串，确保结构唯一。
# 匹配判断：直接检查子树的序列化字符串是否包含在主树的字符串中。
# 复杂度分析
# 时间复杂度：O(n + m)，序列化和子串匹配均为线性时间。
# 空间复杂度：O(n + m)，存储序列化字符串。

# 边界案例处理
# 主树为空：直接返回 False。
# 子树为空：根据题意视为 True（但LeetCode测试用例中子树不为空）。
# 数值边界：序列化时添加分隔符，避免数值粘连导致误判（如 12 和 1,2）。
# 方案优缺点
# 优点：
# 时间复杂度低，适合大规模数据。
# 代码简洁，逻辑直观。
#
# 缺点：
# 生成长字符串可能占用较多内存。
# 依赖字符串操作效率（Python中优化较好）。
# class Solution:
#     def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
#         def serialize(node):
#             res = []
#
#             def helper(n):
#                 if not n:
#                     res.append('#')
#                     return
#                 res.append('^' + str(n.val))  # 用 ^ 分隔防止数值粘连
#                 helper(n.left)
#                 helper(n.right)
#
#             helper(node)
#             return ','.join(res)  # 用逗号分隔各节点
#
#         main_str = serialize(root)
#         sub_str = serialize(subRoot)
#         return sub_str in main_str


#

# class Solution:
#     def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
#         def serialize(node):
#             if not node:
#                 return "#"
#             return f"^{node.val}^{serialize(node.left)}^{serialize(node.right)}"
#
#         s_str = serialize(s)
#         t_str = serialize(t)
#         return self.kmp_search(s_str, t_str) != -1
#
#     def kmp_search(self, haystack, needle):
#         if not needle:
#             return 0
#         lps = [0] * len(needle)
#         length = 0
#         i = 1
#         while i < len(needle):
#             if needle[i] == needle[length]:
#                 length += 1
#                 lps[i] = length
#                 i += 1
#             else:
#                 if length != 0:
#                     length = lps[length - 1]
#                 else:
#                     lps[i] = 0
#                     i += 1
#         i = 0
#         j = 0
#         while i < len(haystack):
#             if haystack[i] == needle[j]:
#                 i += 1
#                 j += 1
#                 if j == len(needle):
#                     return i - j
#             else:
#                 if j != 0:
#                     j = lps[j - 1]
#                 else:
#                     i += 1
#         return -1


# serialize解法的复杂度：
# 序列化：
# root：  O(n)，  n 为节点数。
# subRoot： O(m)， m 为节点数。
# 子串查找：
# 朴素方法（如 Python 的 in）：O(n⋅m)。
# KMP 算法：O(n+m)。
#
# 总复杂度： O(n+m)（使用 KMP）。

test_cases = [
    {
        "method": "isSubtree",
        "root": [3, 4, 5, 1, 2],
        "subRoot": [4, 1, 2],
        "expected": True,
        "case_id": 1,
        "description": "subRoot is an exact subtree of root"
    }, {
        "method": "isSubtree",
        "root": [3, 4, 5, 1, 2, None, None, None, None, 0],
        "subRoot": [4, 1, 2],
        "expected": False,
        "case_id": 2,
        "description": "subRoot is structurally different from any subtree in root"
    }, {
        "method": "isSubtree",
        "root": [1],
        "subRoot": [1],
        "expected": True,
        "case_id": 3,
        "description": "Both root and subRoot are single node trees with the same value"
    }, {
        "method": "isSubtree",
        "root": [1, 2, 3],
        "subRoot": [2, 3],
        "expected": False,
        "case_id": 4,
        "description": "subRoot has a structure that does not match any subtree in root"
    }, {
        "method": "isSubtree",
        "root": [3, 4, 5, 1, 2, None, None, None, None, 0],
        "subRoot": [1],
        "expected": True,
        "case_id": 5,
        "description": "subRoot is a single node that exists in root as a leaf node"
    }, {
        "method": "isSubtree",
        "root": [3, 4, 5, 1, 2, None, None, 0],
        "subRoot": [4, 1, 2],
        "expected": False,
        "case_id": 6,
        "description": "subRoot structure appears in root but has an extra node"
    },
    {
        "method": "isSubtree",
        "root": [4, 1, 2, 3, 4, 5, 6, None, None, None, None, None, None, None, None],
        "subRoot": [4, 5, 6, None, None, None, None],
        "expected": False,
        "case_id": 7,
        "description": ""
    }
]

run_tests()
