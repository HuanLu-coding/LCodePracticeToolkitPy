# 297.py
from test.test_suite import run_tests
from typing import Optional
from libs.tree import TreeNode
from collections import deque


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """将二叉树序列化为字符串"""

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """从字符串反序列化为二叉树"""

        return root


test_cases = [
    {
        "method": ["serialize", "deserialize"],
        "args": [[1, 2, 3, None, None, 4, 5]],
        "expected": [1, 2, 3, None, None, 4, 5],
        "case_id": 1,
        "description": "标准二叉树含空节点"
    },
    {
        "method": ["serialize", "deserialize"],
        "args": [[]],
        "expected": [],
        "case_id": 2,
        "description": "空树"
    },
    {
        "method": ["serialize", "deserialize"],
        "args": [[1]],
        "expected": [1],
        "case_id": 3,
        "description": "单节点树"
    },
    {
        "method": ["serialize", "deserialize"],
        "args": [[1, 2, 3, 4, 5]],
        "expected": [1, 2, 3, 4, 5],
        "case_id": 4,
        "description": "完全二叉树多层"
    },
    {
        "method": ["serialize", "deserialize"],
        "args": [[5, 4, 7, 3, None, 2, None, -1, None, 9]],
        "expected": [5, 4, 7, 3, None, 2, None, -1, None, 9],
        "case_id": 5,
        "description": "不平衡树含负值"
    },
    {
        "method": ["serialize", "deserialize"],
        "args": [[1, None, 2, None, 3, None, 4, None, 5]],
        "expected": [1, None, 2, None, 3, None, 4, None, 5],
        "case_id": 6,
        "description": "右偏树（边界情况）"
    },
    {
        "method": ["serialize", "deserialize"],
        "args": [[1, 2, None, 3, None, 4, None, 5]],
        "expected": [1, 2, None, 3, None, 4, None, 5],
        "case_id": 7,
        "description": "左偏树（边界情况）"
    }
]

run_tests()
