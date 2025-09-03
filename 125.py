# 125.py
from test.test_suite import run_tests


# 125. Valid Palindrome
#
# A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
#
# Given a string `s`, return `true` if it is a **palindrome**, or `false` otherwise.
#
# ### Constraints:
# - `1 <= s.length <= 2 * 10^5`
# - `s` consists only of printable ASCII characters.
#
# ### Examples:
#
# #### Example 1:
# **Input:** s = "A man, a plan, a canal: Panama"
# **Output:** true
# **Explanation:** After removing non-alphanumeric characters and converting to lowercase, `"amanaplanacanalpanama"` is a palindrome.
#
# #### Example 2:
# **Input:** s = "race a car"
# **Output:** false
# **Explanation:** After removing non-alphanumeric characters and converting to lowercase, `"raceacar"` is not a palindrome.
#
# #### Example 3:
# **Input:** s = " "
# **Output:** true
# **Explanation:** After removing non-alphanumeric characters, `s` is an empty string `""`, which is considered a palindrome.
#
# #### Example 4:
# **Input:** s = "0P"
# **Output:** false
# **Explanation:** After removing non-alphanumeric characters, `"0p"` is not a palindrome since `'0'` and `'p'` are different.
#
# #### Example 5:
# **Input:** s = "ab@a"
# **Output:** true
# **Explanation:** After removing `@`, the remaining string `"aba"` is a palindrome.
#
# ---

# 这道题字母和数字都算，用isalnum()，不用isalpha()

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         p1, p2 = 0, len(s) - 1
#
#         while p1 < p2:
#             if not (s[p1].isalnum()):
#                 p1 += 1
#                 continue
#             if not s[p2].isalnum():
#                 p2 -= 1
#                 continue
#             if s[p1].lower() != s[p2].lower():
#                 return False
#             else:
#                 p1 += 1
#                 p2 -= 1
#
#         return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l].isalnum() and s[r].isalnum():
                if not (s[l].lower() == s[r].lower()):
                    return False
                l += 1
                r -= 1
                continue
            else:
                if not s[l].isalnum(): l += 1
                if not s[r].isalnum(): r -= 1
        return True


# # LeetCode 125题解：验证回文串
#
# 我将对LeetCode 125号问题"验证回文串"进行详细分析和解决。
#
# ## 问题分析
#
# LeetCode 125要求判断一个字符串是否为回文串，考虑字母和数字字符，忽略大小写，忽略其他字符（如标点符号和空格）。
#
# 回文串的定义是正着读和倒着读都一样的字符串。例如，"A man, a plan, a canal: Panama"是回文串，因为去掉所有非字母数字字符并转换为小写后是"amanaplanacanalpanama"，正反读都一样。
#
# ### 边界情况和约束条件
#
# 1. 空字符串：按定义应该是回文串
# 2. 只有一个字符的字符串：也是回文串
# 3. 只包含非字母数字字符的字符串：去除这些字符后成为空字符串，也是回文串
# 4. 大小写混合的字符串：需要转换为统一大小写（通常是小写）
# 5. 包含特殊字符和空格的字符串：需要忽略这些字符
#
# ## 解决方案
#
# ### 解决方案一：过滤后反转比较
#
# 这是最直观的解决方案，包括三个步骤：
# 1. 过滤掉非字母数字字符，并将所有字符转换为小写
# 2. 将过滤后的字符串反转
# 3. 比较原始过滤字符串和反转后的字符串是否相等
#
# ```python
# def isPalindrome(s: str) -> bool:
#     # 过滤非字母数字字符，并转换为小写
#     filtered_chars = [c.lower() for c in s if c.isalnum()]
#     filtered_str = ''.join(filtered_chars)
#
#     # 反转字符串并比较
#     return filtered_str == filtered_str[::-1]
# ```
#
# #### 执行演示
# 以输入 `s = "A man, a plan, a canal: Panama"` 为例：
#
# ```
# 1. 过滤并转小写：
#    filtered_chars = ['a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a', 'c', 'a', 'n', 'a', 'l', 'p', 'a', 'n', 'a', 'm', 'a']
#    filtered_str = "amanaplanacanalpanama"
#
# 2. 反转比较：
#    filtered_str[::-1] = "amanaplanacanalpanama"
#    filtered_str == filtered_str[::-1] ? 是的，返回 True
# ```
#
# #### 边界情况验证
# - 空字符串 `""`: 过滤后仍为空字符串，反转后也是空字符串，结果为True
# - 只有一个字符 `"a"`: 过滤后是 `"a"`，反转后也是 `"a"`，结果为True
# - 只有非字母数字字符 `"!@#"`: 过滤后是空字符串，结果为True
# - 大小写混合 `"AbBa"`: 过滤并转换小写后是 `"abba"`，反转后也是 `"abba"`，结果为True
#
# #### 复杂度分析
# - 时间复杂度：O(n)，其中n是字符串长度。过滤、转换和反转操作都需要O(n)时间
# - 空间复杂度：O(n)，需要额外空间存储过滤后的字符串和反转后的字符串
#
# #### 优缺点
# 优点：
# - 代码简洁易懂
# - 逻辑清晰
#
# 缺点：
# - 需要额外空间存储过滤后的字符串
# - 创建新字符串的开销较大
#
# ### 解决方案二：双指针法
#
# 使用两个指针，一个从字符串开头向右移动，一个从字符串末尾向左移动，比较指向的字符是否相同：
#
# ```python
# def isPalindrome(s: str) -> bool:
#     left, right = 0, len(s) - 1
#
#     while left < right:
#         # 跳过非字母数字字符
#         while left < right and not s[left].isalnum():
#             left += 1
#         while left < right and not s[right].isalnum():
#             right -= 1
#
#         # 比较字符（忽略大小写）
#         if s[left].lower() != s[right].lower():
#             return False
#
#         left += 1
#         right -= 1
#
#     return True
# ```
#
# #### 执行演示
# 以输入 `s = "A man, a plan, a canal: Panama"` 为例：
#
# ```
# 初始：left = 0 ('A'), right = 29 ('a')
# 1. 比较 'a' 和 'a'，相等，left = 1, right = 28
# 2. left 指向空格，跳过，left = 2
# 3. 比较 'm' 和 'm'，相等，left = 3, right = 27
# 4. left 指向空格，跳过，left = 4
# 5. 比较 'a' 和 'a'，相等，left = 5, right = 26
# 6. left 指向空格，跳过，left = 6
# 7. 比较 'n' 和 'n'，相等，left = 7, right = 25
#
# ...（继续此过程）...
#
# 最终所有字符都匹配，返回 True
# ```
#
# #### 边界情况验证
# - 空字符串 `""`: left = 0, right = -1，不满足循环条件 left < right，直接返回True
# - 只有一个字符 `"a"`: left = 0, right = 0，不满足循环条件，直接返回True
# - 只有非字母数字字符 `"!@#"`: 会跳过所有字符，不进行比较，返回True
# - 大小写混合 `"AbBa"`: 比较时忽略大小写，返回True
#
# #### 复杂度分析
# - 时间复杂度：O(n)，其中n是字符串长度。在最坏情况下，需要遍历整个字符串
# - 空间复杂度：O(1)，只使用了常数级别的额外空间
#
# #### 优缺点
# 优点：
# - 空间效率高，只需O(1)额外空间
# - 避免了创建新字符串的开销
# - 发现不是回文串时可提前返回，不需要遍历整个字符串
#
# 缺点：
# - 代码稍复杂，有多个while循环嵌套
# - 需要仔细处理指针移动和边界条件
#
# ### 解决方案三：优化的过滤方法
#
# 先过滤，再使用双指针比较，结合了前两种方法的优点：
#
# ```python
# def isPalindrome(s: str) -> bool:
#     # 过滤非字母数字字符，并转换为小写
#     filtered_str = ''.join(c.lower() for c in s if c.isalnum())
#
#     # 使用双指针比较
#     left, right = 0, len(filtered_str) - 1
#     while left < right:
#         if filtered_str[left] != filtered_str[right]:
#             return False
#         left += 1
#         right -= 1
#
#     return True
# ```
#
# #### 执行演示
# 以输入 `s = "A man, a plan, a canal: Panama"` 为例：
#
# ```
# 1. 过滤并转小写：
#    filtered_str = "amanaplanacanalpanama"
#
# 2. 双指针比较：
#    初始：left = 0 ('a'), right = 20 ('a')
#    比较 'a' 和 'a'，相等，left = 1, right = 19
#    比较 'm' 和 'm'，相等，left = 2, right = 18
#    ...
#    所有字符都匹配，返回 True
# ```
#
# #### 边界情况验证
# 与方案一相同，所有边界情况都能正确处理。
#
# #### 复杂度分析
# - 时间复杂度：O(n)，其中n是字符串长度
# - 空间复杂度：O(n)，需要额外空间存储过滤后的字符串
#
# #### 优缺点
# 优点：
# - 逻辑清晰，易于理解
# - 处理非字母数字字符和大小写转换更简洁
#
# 缺点：
# - 需要O(n)额外空间
# - 总是需要遍历整个字符串进行过滤
#
# ## 解决方案比较
#
# | 解决方案 | 时间复杂度 | 空间复杂度 | 代码可读性 | 边界情况处理 | 面试适合度 |
# |---------|-----------|-----------|---------|------------|---------|
# | 过滤后反转比较 | O(n) | O(n) | 高 | 良好 | 中 |
# | 双指针法 | O(n) | O(1) | 中 | 良好 | 高 |
# | 优化的过滤方法 | O(n) | O(n) | 高 | 良好 | 中高 |
#
# ### 最佳解决方案
#
# **双指针法**是最优的解决方案，原因如下：
# 1. **空间效率**：只需O(1)额外空间，比其他方案更高效
# 2. **时间效率**：虽然所有方案的时间复杂度都是O(n)，但双指针法在发现不是回文串时可提前返回
# 3. **面试适合度**：面试中通常更看重空间优化，双指针是解决回文问题的经典方法
# 4. **边界情况处理**：能正确处理所有边界情况
#
# 虽然代码可读性略低于其他方案，但通过添加适当的注释可以提高可读性。在实际面试中，双指针法展示了对算法思想的理解和空间优化的意识，这是面试官高度重视的能力。
#
# 总结：在验证回文串这个问题中，双指针法在时间和空间上都达到了最优，是面试中最值得展示的解决方案。
test_cases = [
    {
        "method": "isPalindrome",
        "s": "A man, a plan, a canal: Panama",
        "expected": True,
        "case_id": 1
    },
    {
        "method": "isPalindrome",
        "s": "race a car",
        "expected": False,
        "case_id": 2
    },
    {
        "method": "isPalindrome",
        "s": " ",
        "expected": True,
        "case_id": 3
    },
    {
        "method": "isPalindrome",
        "s": "0P",
        "expected": False,
        "case_id": 4
    },
    {
        "method": "isPalindrome",
        "s": "ab@a",
        "expected": True,
        "case_id": 5
    }
]

run_tests()
