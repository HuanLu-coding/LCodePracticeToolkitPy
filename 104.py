# 104.py
from test.test_suite import run_tests

from typing import Optional
from collections import deque
from libs.tree import TreeNode
from pprint import pprint
from libs.tree import tree_to_list


# Depth和Level的计数一致，要算上所有node（所以比,height:经过的edge数,大1）

class Solution:
    # BFS Iterative version
    # Level order traversal
    # 计算Level数
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if root is None: return 0
    #     q = []
    #     level = 1
    #     # 应该使用collections.deque()的popleft()方法
    #     q.append(root)
    #     while len(q):
    #         node = q.pop(0)
    #         if node is None: continue
    #         # 对None子节点的处理不够优雅:
    #         if node.left or node.right:
    #             # 错误地假设每次添加子节点就意味着深度增加:
    #             q.append(node.left)
    #             q.append(node.right)
    #             level += 1
    #             # print(', level: ', level)
    #     return level
    #
    # BFS 从上到下遍历，depth 单调递增，最后一个节点的深度即最大深度，直接返回 depth 即可。
    # 改进：直接返回最后一次的 depth，去掉 max_depth：
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     queue = deque([(root, 1)])
    #     while queue:
    #         node, depth = queue.popleft()
    #         if node.left:
    #             queue.append((node.left, depth + 1))
    #         if node.right:
    #             queue.append((node.right, depth + 1))
    #     return depth

    # BFS Iterative version 2
    # 逻辑：使用 BFS 按层遍历，每处理完一层，depth 增加 1。内层循环处理当前层的所有节点，并将下一层节点加入队列。
    # 队列：每层节点入队，最坏情况下最后一层约为n/2，空间为O(n)。

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     queue = deque([root])
    #     depth = 0
    #     while queue:
    #         depth += 1
    #         level_size = len(queue)  # 缓存层大小
    #         for _ in range(level_size):
    #             # popleft() 和 append() 均为 O(1)
    #             node = queue.popleft()
    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)
    #     return depth、
    # 后序遍历求高度 版本
    # 深度是node到root的距离
    # 高度反过来
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     left_depth = self.maxDepth(root.left)
    #     right_depth = self.maxDepth(root.right)
    #     return max(left_depth, right_depth) + 1
    # 以上解法，使用的是post-order traversal，其实是在求root的高度，恰好等于farthest leaf的深度
    # 约束条件：
    # 树中节点数范围为 [0, 10^4]。
    # 节点值范围为 [-100, 100]。
    # 栈溢出风险：递归深度取决于树的高度 h，
    # 在最坏情况下（树退化为单链表），h = n = 10^4。
    # Python 的默认递归限制约为 1000（可通过 sys.setrecursionlimit 调整，但 LeetCode 环境通常不允许修改）。
    # 当 n = 10^4 时，递归栈深度可能达到 10,000，远超默认限制，因此 确实可能导致栈溢出。
    # 节点值影响：
    # 节点值范围 [-100, 100] 与深度计算无关，因此不会影响溢出。
    # 结论：
    # 在约束条件下，递归解法在极端情况下（高度接近 10^4）会导致栈溢出。对于 LeetCode 的实际测试用例，通常树不会如此极端，但理论上存在风险。
    # 改进建议：使用迭代法（如 BFS 或基于栈的 DFS）可完全避免溢出，但这超出当前问题范围。
    #
    # 前序遍历求深度 版本
    # 从根节点出发到叶子节点，深度逐渐增加，采用前序遍历（pre - order traversal）

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def preorder(node, current_depth):
            if not node:
                return current_depth - 1  # 叶子节点的深度
            max_depth = current_depth  # 初始化为当前深度
            max_depth = max(max_depth, preorder(node.left, current_depth + 1))
            max_depth = max(max_depth, preorder(node.right, current_depth + 1))
            return max_depth

        return preorder(root, 1)


test_cases = [
    {
        "method": "maxDepth",
        "root": [3, 9, 20, None, None, 15, 7],
        "expected": 3,
        "case_id": 1,
        "description": "Standard binary tree with depth of 3"
    }, {
        "method": "maxDepth",
        "root": [1, None, 2],
        "expected": 2,
        "case_id": 2,
        "description": "Tree with only right child"
    }, {
        "method": "maxDepth",
        "root": [],
        "expected": 0,
        "case_id": 3,
        "description": "Empty tree"
    }, {
        "method": "maxDepth",
        "root": [1],
        "expected": 1,
        "case_id": 4,
        "description": "Single node tree"
    }, {
        "method": "maxDepth",
        "root": [1, 2],
        "expected": 2,
        "case_id": 5,
        "description": "Tree with only left child"
    },
    {
        "method": "maxDepth",
        "root": [1, 2, 3, 4, 5, 6, 7, 8, None, None, None, None, None, None, None],
        "expected": 4,
        "case_id": 6,
        "description": "Complete binary tree with depth of 4"
    }
]

run_tests()
