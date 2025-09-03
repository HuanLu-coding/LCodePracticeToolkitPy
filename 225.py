import collections


# 没有完美的方案能让所有操作都是 O(1) (使用队列模拟时)。必须做出权衡。
#
# 2个queues：符合题意
# 牺牲了 pop/top 效率来换取 push 的 O(1)。
# 实现（特别是 top 操作要保持状态）稍显复杂和微妙。
class MyStack:
    def __init__(self):
        self.q_main = collections.deque()  # 主要存储队列
        self.q_helper = collections.deque()  # 辅助队列

    def push(self, x: int) -> None:
        # 时间复杂度 O(1)
        self.q_main.append(x)

    def _move_elements(self):
        # 将 main 队列中除最后一个元素外的所有元素移到 helper 队列
        # 时间复杂度 O(n)
        while len(self.q_main) > 1:
            self.q_helper.append(self.q_main.popleft())

    def pop(self) -> int:
        # 时间复杂度 O(n)
        if self.empty():
            # raise IndexError("pop from empty stack")
            return -1

        self._move_elements()  # 移动 n-1 个元素
        # 此时 q_main 只剩最后一个元素（即栈顶）
        top_element = self.q_main.popleft()
        # 交换 main 和 helper，使 helper (现在包含剩余元素) 成为新的 main
        self.q_main, self.q_helper = self.q_helper, self.q_main
        return top_element

    def top(self) -> int:
        # 时间复杂度 O(n)
        if self.empty():
            # raise IndexError("top from empty stack")
            return -1

        self._move_elements()  # 移动 n-1 个元素
        # 查看 q_main 中仅剩的最后一个元素
        top_element = self.q_main[0]
        # 为了保持状态一致（所有元素都在 main 中），需要把这个元素也移到 helper
        self.q_helper.append(self.q_main.popleft())
        # 交换 main 和 helper
        self.q_main, self.q_helper = self.q_helper, self.q_main
        return top_element

    def empty(self) -> bool:
        # 时间复杂度 O(1)
        # 只需要检查主队列是否为空
        return len(self.q_main) == 0

    # 只用1个queue：
    # # 牺牲了 push 效率来换取 pop/top 的 O(1)。

    # def __init__(self):
    #     self.q = collections.deque()

    # def push(self, x: int) -> None:
    #     # 时间复杂度 O(n)
    #     n = len(self.q)
    #     self.q.append(x) # 1. 新元素入队尾
    #     # 2. 将队首的 n 个元素（原来的所有元素）依次移到队尾
    #     for _ in range(n):
    #         self.q.append(self.q.popleft())

    # def pop(self) -> int:
    #     # 时间复杂度 O(1)
    #     if self.empty():
    #         # 根据 LeetCode 假设，此情况不会发生
    #         # 但严谨实现可抛出异常或返回错误码
    #         # raise IndexError("pop from empty stack")
    #         return -1 # 示例性返回
    #     return self.q.popleft() # 最新元素在队首

    # def top(self) -> int:
    #     # 时间复杂度 O(1)
    #     if self.empty():
    #         # raise IndexError("top from empty stack")
    #         return -1
    #     return self.q[0] # collections.deque 允许 O(1) 访问队首元素

    # def empty(self) -> bool:
    #     # 时间复杂度 O(1)
    #     return len(self.q) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
