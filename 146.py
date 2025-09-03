# 146. LRU Cache
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
# - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# - int get(int key) Return the value of the key if the key exists, otherwise return -1.
# - void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
#   If the number of keys exceeds the capacity from this operation, evict the least recently used key.
#
# The functions get and put must each run in O(1) average time complexity.
#
# ### Constraints:
# - 1 <= capacity <= 3000
# - 0 <= key <= 10^4
# - 0 <= value <= 10^5
# - At most 2 * 10^5 calls will be made to get and put.
#
# ### Example 1:
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
from collections import OrderedDict


# 具体总结：
#
# 方案	                    时间复杂度   get/put	简单性	    面试可接受性
# HashMap + 双向链表（标准）	O(1)	            一般（指针多）	✅ 标准且优秀
# HashMap + 堆	            O(log n)	        复杂（堆调整）	❌ 不符合 O(1) 要求
# HashMap + 单向链表	        删除需要遍历 O(n)	    简单	        ❌ 不符合 O(1)
# HashMap + 数组/列表	    插入/删除 O(n)	    简单	        ❌ 不符合 O(1)
# 直接库现成（如OrderedDict）	O(1)	            极其简单	    ✅（但是面试可能不让用库）
# 🌟 最后要点（面试时）：
# 	•	面试时如果你直接说：“我知道有 OrderedDict 这种现成库，但如果要求自己实现，我会用 HashMap + 双向链表组合”，
# 这句话会让面试官对你印象非常好，因为你展现了：
# 	•	知识广度（知道标准库解决方案）；
# 	•	基础扎实（能手动实现）；
# 	•	时间观念（知道要权衡实现复杂度和面试时间）。
# 以下solution Runtime 134ms, Beats 63.86%
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # 移到末尾表示最近使用
        return self.cache[key]

    # 对于 put(key, value) 操作，需要将键标记为最近使用。
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)  # 移除最久未使用的项

# 以下solution Runtime 151ms, Beats 44.48%
#
# class ListNode:
#     def __init__(self, key=0, value=0):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None
#
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = {}  # 哈希表：key -> node
#         # 哑节点
#         self.head = ListNode()
#         self.tail = ListNode()
#         self.head.next = self.tail
#         self.tail.prev = self.head
#
#     def _add_to_head(self, node):
#         """将节点插入到头部"""
#         node.prev = self.head
#         node.next = self.head.next
#         self.head.next.prev = node
#         self.head.next = node
#
#     def _remove_node(self, node):
#         """从链表中删除节点"""
#         node.prev.next = node.next
#         node.next.prev = node.prev
#
#     def _move_to_head(self, node):
#         """将节点移动到头部"""
#         self._remove_node(node)
#         self._add_to_head(node)
#
#     def _remove_tail(self):
#         """移除并返回尾部节点"""
#         node = self.tail.prev
#         self._remove_node(node)
#         return node
#
#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         node = self.cache[key]
#         self._move_to_head(node)
#         return node.value
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             node = self.cache[key]
#             node.value = value
#             self._move_to_head(node)
#         else:
#             node = ListNode(key, value)
#             self.cache[key] = node
#             self._add_to_head(node)
#             if len(self.cache) > self.capacity:
#                 tail_node = self._remove_tail()
#                 del self.cache[tail_node.key]


# ### LeetCode 问题 #146: LRU Cache 分析与解决方案
#
# 以下是对 LeetCode #146（LRU Cache）的全面分析和解决方案，涵盖问题评估、解决方案实现、测试用例验证、性能分析和方案比较。分析将以科学严谨的态度进行，保持批判性、诚实性和彻底性，同时以简洁、直接的中文呈现，降低认知负担，便于记忆。
#
# ---
#
# ## 问题评估
#
# ### 0. LRU 缓存的背景
# LRU（Least Recently Used，最近最少使用）缓存是一种缓存淘汰策略，当缓存容量满时，优先淘汰最久未使用的元素。LRU 缓存支持以下操作：
# - **get(key)**：获取键对应的值，若键不存在返回 -1，同时将该键标记为最近使用。
# - **put(key, value)**：插入或更新键值对，若键已存在则更新值，若缓存满则移除最久未使用的键值对，再插入新键值对。
#
# LRU 缓存的关键是高效维护键值对的访问顺序，通常需要：
# - O(1) 时间复杂度的 get 和 put 操作。
# - 数据结构支持快速查找、插入、删除和更新访问顺序。
#
# ### 1. 问题陈述分析
# LeetCode #146 要求实现一个 LRUCache 类，支持以下操作：
# - **初始化**：`LRUCache(int capacity)`，设置缓存容量。
# - **get(int key)**：返回键对应的值，若不存在返回 -1，将键标记为最近使用。
# - **put(int key, int value)**：插入或更新键值对，若键存在则更新值，若缓存满则移除最久未使用的键值对，再插入新键值对。
#
# **关键要求**：
# - 所有操作（get 和 put）需在 O(1) 时间复杂度内完成。
# - 键值对需按最近使用顺序维护，最近使用的键在“头部”，最久未使用的在“尾部”。
#
# ### 2. 边界情况与约束
# **约束**：
# - 1 <= capacity <= 3000
# - 0 <= key <= 10^4
# - 0 <= value <= 10^5
# - 最多调用 2 * 10^5 次 get 和 put。
#
# **边界情况**：
# - **容量为 1**：插入新键值对后立即淘汰旧键值对。
# - **键不存在**：get 返回 -1，put 需插入新键值对。
# - **键已存在**：get 返回值并更新访问顺序，put 更新值并更新访问顺序。
# - **缓存满**：put 需移除最久未使用的键值对。
# - **频繁访问同一键**：需正确更新访问顺序，不影响其他键。
# - **空缓存**：get 应返回 -1，put 应正常插入。
#
# ### 3. 人类思维与优化过程
# **直觉方法**：
# - 直觉上，LRU 缓存需要快速查找键值对（想到哈希表）和维护访问顺序（想到链表）。
# - 哈希表提供 O(1) 查找，但无法直接维护顺序。
# - 链表（特别是双向链表）便于插入、删除和移动节点，但查找慢。
#
# **分析方法**：
# - **问题分解**：
#   - get：查找键（O(1)），返回值，移动到最近使用位置（O(1)）。
#   - put：查找键（O(1)），更新或插入，移除最久未使用（O(1)）。
# - **数据结构选择**：
#   - 哈希表存储键到节点的映射，节点包含值和链表指针。
#   - 双向链表维护访问顺序，头部为最近使用，尾部为最久未使用。
# - **优化目标**：
#   - 所有操作 O(1)。
#   - 代码简洁，易于实现和调试。
#   - 鲁棒处理边界情况。
#
# **混合方法**：
# - 结合直觉（哈希表 + 链表）和分析（O(1) 要求），选择哈希表 + 双向链表。
# - 设计节点移动逻辑，确保插入、删除、更新顺序高效。
# - 验证边界情况（如容量 1、键不存在）确保鲁棒性。
#
# ### 4. 解决方案设计
# **数据结构**：
# - **哈希表**（字典）：`key -> node`，存储键到双向链表节点的映射。
# - **双向链表**：节点包含`key, value, prev, next`，便于 O(1) 删除和插入。
#   - 哑节点`head`和`tail`简化边界操作。
#   - 最近使用的节点靠近`head`，最久未使用的靠近`tail`。
#
# **算法**：
# - **get(key)**：
#   - 在哈希表中查找键，若不存在返回 -1。
#   - 获取节点的值，将节点移动到链表头部（最近使用）。
# - **put(key, value)**：
#   - 若键存在，更新节点值，移动到头部。
#   - 若键不存在，创建新节点，插入到头部，添加到哈希表。
#   - 若缓存满，移除尾部节点（最久未使用），从哈希表删除对应键。
# - **辅助操作**：
#   - `move_to_head(node)`：将节点移动到链表头部。
#   - `remove_node(node)`：从链表中删除节点。
#   - `add_to_head(node)`：将节点插入到链表头部。
#   - `remove_tail()`：移除并返回尾部节点。
#
# ---
#
# ## 解决方案 1：哈希表 + 双向链表
#
# ### 1. 实现
#
# ```python
# class ListNode:
#     def __init__(self, key=0, value=0):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None
#
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = {}  # 哈希表：key -> node
#         # 哑节点
#         self.head = ListNode()
#         self.tail = ListNode()
#         self.head.next = self.tail
#         self.tail.prev = self.head
#
#     def _add_to_head(self, node):
#         """将节点插入到头部"""
#         node.prev = self.head
#         node.next = self.head.next
#         self.head.next.prev = node
#         self.head.next = node
#
#     def _remove_node(self, node):
#         """从链表中删除节点"""
#         node.prev.next = node.next
#         node.next.prev = node.prev
#
#     def _move_to_head(self, node):
#         """将节点移动到头部"""
#         self._remove_node(node)
#         self._add_to_head(node)
#
#     def _remove_tail(self):
#         """移除并返回尾部节点"""
#         node = self.tail.prev
#         self._remove_node(node)
#         return node
#
#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         node = self.cache[key]
#         self._move_to_head(node)
#         return node.value
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             node = self.cache[key]
#             node.value = value
#             self._move_to_head(node)
#         else:
#             node = ListNode(key, value)
#             self.cache[key] = node
#             self._add_to_head(node)
#             if len(self.cache) > self.capacity:
#                 tail_node = self._remove_tail()
#                 del self.cache[tail_node.key]
# ```
#
# ### 2. 执行演示（测试用例）
# **测试用例**：
# ```python
# cache = LRUCache(2)
# cache.put(1, 1)  # 缓存: [(1,1)]
# cache.put(2, 2)  # 缓存: [(2,2), (1,1)]
# print(cache.get(1))  # 返回 1, 缓存: [(1,1), (2,2)]
# cache.put(3, 3)  # 移除 (2,2), 缓存: [(3,3), (1,1)]
# print(cache.get(2))  # 返回 -1
# cache.put(4, 4)  # 移除 (1,1), 缓存: [(4,4), (3,3)]
# print(cache.get(1))  # 返回 -1
# print(cache.get(3))  # 返回 3, 缓存: [(3,3), (4,4)]
# print(cache.get(4))  # 返回 4, 缓存: [(4,4), (3,3)]
# ```
#
# **调用栈跟踪**：
# - **put(1, 1)**：
#   - 创建节点`n1(key=1, value=1)`。
#   - `cache[1] = n1`, `_add_to_head(n1)`。
#   - 链表：`head <-> n1 <-> tail`。
#   - 缓存：`{1: n1}`。
# - **put(2, 2)**：
#   - 创建节点`n2(key=2, value=2)`。
#   - `cache[2] = n2`, `_add_to_head(n2)`。
#   - 链表：`head <-> n2 <-> n1 <-> tail`。
#   - 缓存：`{1: n1, 2: n2}`。
# - **get(1)**：
#   - `cache[1] = n1`，返回`n1.value = 1`。
#   - `_move_to_head(n1)`：`_remove_node(n1)`, `_add_to_head(n1)`。
#   - 链表：`head <-> n1 <-> n2 <-> tail`。
#   - 返回 1。
# - **put(3, 3)**：
#   - 缓存满（len=2, capacity=2）。
#   - 创建节点`n3(key=3, value=3)`。
#   - `cache[3] = n3`, `_add_to_head(n3)`。
#   - 链表：`head <-> n3 <-> n1 <-> n2 <-> tail`。
#   - 移除尾部：`_remove_tail()`返回`n2`, `del cache[2]`。
#   - 链表：`head <-> n3 <-> n1 <-> tail`。
#   - 缓存：`{1: n1, 3: n3}`。
# - **get(2)**：
#   - `2 not in cache`，返回 -1。
# - **后续操作**类似，确保节点移动和删除正确。
#
# **结果**：
# - 输出：`1, -1, -1, 3, 4`，符合预期。
#
# ### 3. 边界测试用例验证
# - **容量为 1**（`capacity=1`）：
#   - `put(1,1)`：缓存`[(1,1)]`。
#   - `put(2,2)`：移除`(1,1)`，插入`(2,2)`，缓存`[(2,2)]`。
#   - `get(1)`：返回 -1。
#   - **验证**：`_remove_tail()`和`del cache[key]`正确移除旧节点，新节点插入头部。
# - **键不存在**：
#   - `get(999)`：`999 not in cache`，返回 -1。
#   - **验证**：哈希表查找 O(1)，无副作用。
# - **频繁访问同一键**：
#   - `get(1)`多次：每次`_move_to_head(n1)`，链表保持`n1`在头部。
#   - **验证**：`_move_to_head`正确更新顺序，不影响其他节点。
# - **空缓存**：
#   - `get(1)`在空缓存：返回 -1。
#   - **验证**：`cache`为空，逻辑无异常。
#
# ### 4. Big O 分析
# - **时间复杂度**：
#   - get：哈希表查找 O(1)，移动节点 O(1)，总计 O(1)。
#   - put：哈希表查找/插入 O(1)，链表操作（插入/删除）O(1)，总计 O(1)。
# - **空间复杂度**：
#   - O(capacity)：哈希表存储`capacity`个键值对，双向链表存储`capacity`个节点。
#   - 哑节点和指针为常数空间。
#
# ### 5. 优缺点评估
# **优点**：
# - O(1) 时间复杂度满足要求。
# - 代码结构清晰，辅助函数模块化，易于维护。
# - 双向链表和哈希表结合，直观实现 LRU 逻辑。
# - 鲁棒处理所有边界情况（容量 1、键不存在等）。
#
# **缺点**：
# - 实现较复杂，需仔细管理链表指针，可能引入指针错误。
# - 空间使用较高（每个节点存储 key、value、prev、next）。
# - 代码量较多，面试中需快速实现，可能耗时。
#
# ---
#
# ## 解决方案 2：哈希表 + 有序字典（Python OrderedDict）
#
# ### 1. 实现
#
# ```python
# from collections import OrderedDict
#
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = OrderedDict()  # 有序字典，维护访问顺序
#
#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         value = self.cache[key]
#         self.cache.move_to_end(key)  # 移动到末尾（最近使用）
#         return value
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.cache[key] = value
#             self.cache.move_to_end(key)
#         else:
#             self.cache[key] = value
#             if len(self.cache) > self.capacity:
#                 self.cache.popitem(last=False)  # 移除最久未使用（首项）
# ```
#
# ### 2. 执行演示（测试用例）
# **测试用例**：同解决方案 1。
# **调用栈跟踪**：
# - **put(1, 1)**：
#   - `cache[1] = 1`，OrderedDict：`[(1,1)]`。
# - **put(2, 2)**：
#   - `cache[2] = 2`，OrderedDict：`[(1,1), (2,2)]`。
# - **get(1)**：
#   - `cache[1] = 1`，`move_to_end(1)`。
#   - OrderedDict：`[(2,2), (1,1)]`。
#   - 返回 1。
# - **put(3, 3)**：
#   - 缓存满，`cache[3] = 3`。
#   - OrderedDict：`[(2,2), (1,1), (3,3)]`。
#   - `popitem(last=False)`移除`(2,2)`。
#   - OrderedDict：`[(1,1), (3,3)]`。
# - **get(2)**：
#   - `2 not in cache`，返回 -1。
# - **后续操作**类似。
#
# **结果**：输出`1, -1, -1, 3, 4`，正确。
#
# ### 3. 边界测试用例验证
# - **容量为 1**：
#   - `put(1,1)`：`[(1,1)]`。
#   - `put(2,2)`：`popitem(last=False)`移除`(1,1)`，插入`(2,2)`。
#   - **验证**：OrderedDict 的`popitem`正确移除首项。
# - **键不存在**：
#   - `get(999)`：返回 -1。
#   - **验证**：OrderedDict 查找 O(1)。
# - **频繁访问同一键**：
#   - `get(1)`多次：`move_to_end(1)`保持`1`在末尾。
#   - **验证**：OrderedDict 正确维护顺序。
# - **空缓存**：
#   - `get(1)`：返回 -1。
#   - **验证**：空 OrderedDict 无异常。
#
# ### 4. Big O 分析
# - **时间复杂度**：
#   - get：哈希表查找 O(1)，`move_to_end` O(1)，总计 O(1)。
#   - put：哈希表插入 O(1)，`move_to_end`或`popitem` O(1)，总计 O(1)。
# - **空间复杂度**：
#   - O(capacity)：OrderedDict 存储`capacity`个键值对。
#
# ### 5. 优缺点评估
# **优点**：
# - 代码极其简洁，利用 Python 内置 OrderedDict，减少实现负担。
# - O(1) 时间复杂度，性能与方案 1 相同。
# - 易于调试，内置数据结构减少指针管理错误。
# - 面试中快速实现，代码量少。
#
# **缺点**：
# - 依赖 Python 特定库（OrderedDict），可能不适用于其他语言。
# - 不展示底层数据结构实现，可能在面试中被要求手动实现链表。
# - 对 OrderedDict 内部实现不透明，难以优化。
#
# ---
#
# ## 解决方案比较
#
# | 标准                  | 方案 1: 哈希表 + 双向链表                     | 方案 2: 哈希表 + OrderedDict                 |
# |-----------------------|---------------------------------------------|---------------------------------------------|
# | **适合面试**          | 适合展示数据结构能力，需较多时间实现和调试。 | 快速实现，适合时间紧张，但可能需解释 OrderedDict。 |
# | **时间复杂度**        | get/put: O(1)                               | get/put: O(1)                               |
# | **空间复杂度**        | O(capacity)                                 | O(capacity)                                 |
# | **代码可读性**        | 模块化但复杂，需理解链表操作。               | 简洁直观，依赖内置库，易读。                 |
# | **边界情况处理**      | 显式处理所有边界，鲁棒性强。                 | 依赖 OrderedDict，边界处理可靠。             |
#
# **最优方案选择**：
# - **方案 2（OrderedDict）**是面试中的首选，因为：
#   - **快速实现**：代码简洁，5-10 分钟内完成，适合 45 分钟面试。
#   - **高可读性**：逻辑清晰，减少出错风险。
#   - **O(1) 性能**：与方案 1 等效。
#   - **边界处理可靠**：Python 内置库经过充分测试。
# - **方案 1（双向链表）**适合以下场景：
#   - 面试官要求手动实现底层数据结构。
#   - 非 Python 环境（无 OrderedDict）。
#   - 需要展示对链表和哈希表的深入理解。
# - **批判性评价**：
#   - 方案 1 更通用，但实现复杂，容易出错（指针管理）。
#   - 方案 2 依赖 Python 特性，可能被质疑“偷懒”，需准备解释 OrderedDict 底层（哈希表 + 双向链表）。
#   - 两者性能相当，方案 2 的简洁性和可靠性使其更适合快速面试场景。
#
# **最终推荐**：优先使用方案 2（OrderedDict），若面试官要求手动实现链表或使用其他语言，切换到方案 1。
#
# ---
#
# ### 总结
# - **科学严谨性**：通过分解问题、分析约束、验证边界、比较方案，确保分析全面。
# - **批判性**：指出方案 1 的复杂性和方案 2 的语言依赖，客观评价优缺点。
# - **低认知负担**：结构化分析（背景、评估、方案、比较），清晰分段，便于理解和记忆。
# - **改进空间**：方案 1 可进一步优化链表操作代码（如减少冗余函数），方案 2 可搭配伪代码解释 OrderedDict 底层。
#

#
# 你提出了一个很实际的问题：在面试中，为了实现 LRU 缓存（Least Recently Used Cache），我们肯定会用哈希表来保证 O(1) 的查找和更新，但仅仅为了维护访问顺序（时间戳或最近使用记录），是否非得用链表，甚至双向链表？这种实现似乎复杂且耗时，尤其在时间有限的面试场景下。你还提到 Python 的 `deque`（双端队列）操作更简洁舒服，能否用它替代链表来维护顺序？下面我将完整分析这个问题，回答你的疑惑。
#
# ---
#
# #### 1. LRU 缓存的核心需求
# LRU 缓存要求 `get`（获取）和 `put`（插入/更新）操作都在 **O(1) 时间复杂度** 内完成。这意味着：
# - **查找**：通过键快速找到值（哈希表解决，O(1)）。
# - **更新顺序**：每次访问或插入时，将键移动到“最近使用”位置（通常是头部）。
# - **删除**：缓存满时，移除“最久未使用”的键（通常是尾部）。
#
# 你说得对，哈希表是必须的，因为它解决了 O(1) 查找和更新的问题。但维护访问顺序是另一个挑战，我们需要评估用双向链表和 `deque` 的优劣。
#
# ---
#
# #### 2. 双向链表方案：为什么常用但显得“愚蠢”？
# **实现方式**：
# - 用哈希表（`dict`）存储 `key -> node`，节点包含值和指针（`prev`, `next`）。
# - 双向链表维护访问顺序：头部是最近使用，尾部是最久未使用。
# - `get(key)`：找到节点，删除并移到头部（O(1)）。
# - `put(key, value)`：更新或插入节点，移到头部，若满则删除尾部（O(1)）。
#
# **优点**：
# - **O(1) 操作**：通过指针，删除任意节点和插入到头部都是 O(1)。
# - **通用性**：不依赖特定语言特性，适用于 C++、Java 等。
#
# **缺点**：
# - **复杂**：手动管理 `prev` 和 `next` 指针，代码量大，容易出错。
# - **面试中的负担**：时间有限时，实现和调试链表可能拖慢进度，显得“笨重”。
#
# 你的感觉没错：在面试中花大量时间写链表维护顺序，确实有点“愚蠢”，尤其当语言提供更简洁的工具时。
#
# ---
#
# #### 3. 用 Python `deque` 维护顺序的可行性
# 你提到 `deque`（双端队列）操作更舒服，比如 `appendleft`（插头部）、`append`（插尾部）、`popleft`（删头部）、`pop`（删尾部）都是 O(1)。那么，能否用 `deque` 替代双向链表呢？让我们分析一下。
#
# **`deque` 的特性**：
# - Python 的 `deque` 内部实现是双向链表，但通过简洁的 API 屏蔽了指针操作。
# - **O(1) 操作**：头部和尾部的插入/删除。
# - **O(n) 操作**：查找或删除任意位置的元素（需要遍历）。
#
# **尝试方案**：
# - 用 `deque` 存储键的顺序（头部为最近使用，尾部为最久未使用）。
# - 用哈希表存储 `key -> value`。
# - `get(key)`：查找值，将键从 `deque` 中删除并重新插入到头部。
# - `put(key, value)`：更新哈希表，将键从 `deque` 中删除（若存在）并插入到头部，若满则移除尾部键。
#
# **问题**：
# - **删除指定键**：`deque` 不支持 O(1) 删除任意元素。例如，`deque = [3, 2, 1]`，`get(2)` 需要先找到 2（O(n) 遍历），删除（O(1)），再插入头部（O(1)），总时间为 **O(n)**。
# - **移动到头部**：每次 `get` 或 `put` 都需要将键移到头部，但 `deque` 无法 O(1) 移动中间元素。
#
# **结论**：
# - `deque` 无法满足 LRU 缓存的 O(1) 要求，因为删除或移动任意元素需要 O(n) 时间。
# - 虽然 `deque` 的 API 比手动链表舒服，但它不适合直接用于 LRU 缓存。
#
# ---
#
# #### 4. 改进尝试：`deque` + 哈希表存索引
# **思路**：
# - `deque` 存键，哈希表存 `key -> (value, index)`，`index` 是键在 `deque` 中的位置。
# - `get(key)`：通过哈希表找到 `index`，删除 `deque[index]`，插入到头部。
#
# **问题**：
# - **删除 `deque[index]`**：Python `deque` 的中间删除操作是 O(n)，因为需要移动后续元素。
# - **更新索引**：删除后，`deque` 中后续元素的索引变了，哈希表中所有相关索引需更新，仍然是 O(n)。
#
# **结论**：
# - 这种方法依然无法达到 O(1)，`deque` 的局限性在于无法 O(1) 删除任意元素。
#
# ---
#
# #### 5. 更好的方法：Python 的 `OrderedDict`
# 既然双向链表复杂，`deque` 又不行，有没有更优解？在 Python 中，答案是 **是的**——使用 `collections.OrderedDict`。
#
# **`OrderedDict` 的优势**：
# - 内部实现是哈希表 + 双向链表，支持 O(1) 操作。
# - 提供 `move_to_end(key)`（将键移到末尾）和 `popitem(last=False)`（移除最老的项），均为 O(1)。
# - API 简洁，代码量少。
#
# **实现**：
# ```python
# from collections import OrderedDict
#
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = OrderedDict()
#
#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         self.cache.move_to_end(key)  # 移到末尾表示最近使用
#         return self.cache[key]
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.cache[key] = value
#             self.cache.move_to_end(key)
#         else:
#             self.cache[key] = value
#             if len(self.cache) > self.capacity:
#                 self.cache.popitem(last=False)  # 移除最久未使用的项
# ```
#
# **为什么推荐**：
# - **O(1) 时间**：满足 LRU 缓存需求。
# - **简洁高效**：面试中快速实现，减少出错。
# - **语言特性**：展示你对 Python 的掌握。
#
# ---
#
# #### 6. 面试中的策略
# - **Python 环境**：
#   - 优先用 `OrderedDict`，既满足 O(1) 要求，又简洁省时。
#   - 如果面试官要求手动实现，再用双向链表 + 哈希表。
# - **其他语言**：
#   - JavaScript：用 `Map`（按插入顺序迭代）。
#   - Java：用 `LinkedHashMap`。
#   - C++：无内置结构，需实现双向链表 + 哈希表。
# - **时间有限**：
#   - 选择语言内置的有序映射（如 `OrderedDict`），快速完成。
# - **展示能力**：
#   - 准备双向链表方案，解释其 O(1) 原理，展示数据结构功底。
#
# ---
#
# #### 7. 最终回答你的问题
# - **双向链表复杂吗？** 是的，在面试中手动实现确实耗时且容易出错，显得“愚蠢”。
# - **有更好的方法吗？** 在 Python 中有！用 `OrderedDict` 是最优选择，简洁且高效。
# - **可以用 `deque` 吗？** 不行，虽然操作舒服，但无法 O(1) 删除任意元素，`get` 和 `put` 会退化到 O(n)。
#
# **建议**：
# - 面试中，如果用 Python，直接用 `OrderedDict` 实现 LRU 缓存，既满足要求又节省时间。
# - 如果需要展示数据结构能力，准备双向链表 + 哈希表的方案。
# - 放弃 `deque`，它不适合这个场景。
#
# 希望这个分析解答了你的疑问！如果还有其他想法或场景想讨论，随时告诉我。
