# 271. Encode and Decode Strings

# 设计一个算法，将字符串列表编码为单个字符串，以便可以通过网络传输，并在接收端解码回原始的字符串列表。
#
# 编码后的字符串必须包含足够的信息，以便能够准确地还原原始的字符串列表，即使字符串中包含特殊字符或为空。
#
# ### 约束条件：
# - `1 <= strs.length <= 200`
# - `0 <= strs[i].length <= 200`
# - `strs[i]` 可以包含任何有效的 ASCII 字符（共 256 个）
# - 编码和解码算法必须是无状态的（即不依赖于类成员变量、全局变量或静态变量）
# - 不允许使用如 `eval` 或 `serialize` 等库方法，必须自行实现编码/解码逻辑
#
# ### 示例 1:
# 输入: strs = ["Hello", "World"]
# 编码: "5:Hello5:World"
# 解码: ["Hello", "World"]
#
# ### 示例 2:
# 输入: strs = [""]
# 编码: "0:"
# 解码: [""]
#
# ### 示例 3:
# 输入: strs = ["C#", "&"]
# 编码: "2:C#1:&"
# 解码: ["C#", "&"]

from test.test_suite import run_tests
from typing import *


class Codec:
    def encode(self, strs: List[str]) -> str:
        return '#'.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        result = []
        i = 0
        while i < len(s):
            # 提取长度
            length_end = s.find('#', i)
            length = int(s[i:length_end])
            # 提取字符串
            string = s[length_end + 1:length_end + 1 + length]
            result.append(string)
            i = length_end + 1 + length
        return result


test_cases = [
    {
        "method": "encode_decode",
        "input": ["Hello", "World"],
        "expected": ["Hello", "World"],
        "case_id": 1,
        "description": "基本示例，两个普通字符串"
    },
    {
        "method": "encode_decode",
        "input": [""],
        "expected": [""],
        "case_id": 2,
        "description": "包含一个空字符串"
    },
    {
        "method": "encode_decode",
        "input": ["C#", "&"],
        "expected": ["C#", "&"],
        "case_id": 3,
        "description": "包含特殊字符的字符串"
    },
    {
        "method": "encode_decode",
        "input": ["", "abc", ""],
        "expected": ["", "abc", ""],
        "case_id": 4,
        "description": "混合空字符串和非空字符串"
    },
    {
        "method": "encode_decode",
        "input": ["a" * 200],
        "expected": ["a" * 200],
        "case_id": 5,
        "description": "包含最大长度字符串（200个字符）"
    },
    {
        "method": "encode_decode",
        "input": ["", "", ""],
        "expected": ["", "", ""],
        "case_id": 6,
        "description": "多个空字符串"
    },
    {
        "method": "encode_decode",
        "input": ["123:456", "789"],
        "expected": ["123:456", "789"],
        "case_id": 7,
        "description": "字符串中包含分隔符字符 ':'"
    }
]

# run_tests()

run_tests()
