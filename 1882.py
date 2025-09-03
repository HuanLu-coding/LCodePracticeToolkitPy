# https://leetcode.com/problems/process-tasks-using-servers/description/
# 1882. Process Tasks Using Servers

# You are given two 0-indexed integer arrays servers and tasks of lengths n​​​​​​ and m​​​​​​ respectively. servers[i] is the weight of the i​​​​​​th​​​​ server, and tasks[j] is the time needed to process the j​​​​​​th​​​​ task in seconds.
#
# Tasks are assigned to the servers using a task queue. Initially, all servers are free, and the queue is empty.
#
# At second j, the jth task is inserted into the queue (starting with the 0th task being inserted at second 0). As long as there are free servers and the queue is not empty, the task in the front of the queue will be assigned to a free server with the smallest weight, and in case of a tie, it is assigned to a free server with the smallest index.
#
# If there are no free servers and the queue is not empty, we wait until a server becomes free and immediately assign the next task. If multiple servers become free at the same time, then multiple tasks from the queue will be assigned in order of insertion following the weight and index priorities above.
#
# A server that is assigned task j at second t will be free again at second t + tasks[j].
#
# Build an array ans​​​​ of length m, where ans[j] is the index of the server the j​​​​​​th task will be assigned to.
#
# Return the array ans​​​​.
#
# ### Constraints:
# - servers.length == n
# - tasks.length == m
# - 1 <= n, m <= 2 * 10^5
# - 1 <= servers[i], tasks[j] <= 2 * 10^5
#
# ### Example 1:
# Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]
# Output: [2,2,0,2,1,2]
# Explanation: Events in chronological order go as follows:
# - At second 0, task 0 is added and processed using server 2 until second 1.
# - At second 1, server 2 becomes free. Task 1 is added and processed using server 2 until second 3.
# - At second 2, task 2 is added and processed using server 0 until second 5.
# - At second 3, server 2 becomes free. Task 3 is added and processed using server 2 until second 5.
# - At second 4, task 4 is added and processed using server 1 until second 5.
# - At second 5, all servers become free. Task 5 is added and processed using server 2 until second 7.
#
# ### Example 2:
# Input: servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
# Output: [1,4,1,4,1,3,2]
# Explanation: Events in chronological order go as follows:
# - At second 0, task 0 is added and processed using server 1 until second 2.
# - At second 1, task 1 is added and processed using server 4 until second 2.
# - At second 2, servers 1 and 4 become free. Task 2 is added and processed using server 1 until second 4.
# - At second 3, task 3 is added and processed using server 4 until second 7.
# - At second 4, server 1 becomes free. Task 4 is added and processed using server 1 until second 9.
# - At second 5, task 5 is added and processed using server 3 until second 7.
# - At second 6, task 6 is added and processed using server 2 until second 7.

from test.test_suite import run_tests
from typing import *
import heapq


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n = len(servers)
        m = len(tasks)
        ans = [0] * m

        # 初始化空闲服务器堆（权重，索引）
        free = []
        for i in range(n):
            heapq.heappush(free, (servers[i], i))

        # 忙碌的服务器堆（释放时间，权重，索引）
        busy = []
        tasks_queue = deque()

        current_time = 0

        for j in range(m):
            # 将任务j加入队列
            tasks_queue.append((j, tasks[j]))
            current_time = max(current_time, j)

            # 释放所有可用的服务器
            while busy and busy[0][0] <= current_time:
                release_time, weight, idx = heapq.heappop(busy)
                heapq.heappush(free, (weight, idx))

            # 分配任务到可用服务器
            while free and tasks_queue:
                task_idx, duration = tasks_queue.popleft()
                weight, idx = heapq.heappop(free)
                ans[task_idx] = idx
                heapq.heappush(busy, (current_time + duration, weight, idx))

        # 处理剩余的任务
        while tasks_queue:
            # 无可用服务器时，时间跳跃到最近的释放时间
            if not free:
                if not busy:
                    break  # 防止无忙碌服务器时的错误
                current_time = busy[0][0]
                while busy and busy[0][0] <= current_time:
                    release_time, weight, idx = heapq.heappop(busy)
                    heapq.heappush(free, (weight, idx))

            # 分配任务
            while free and tasks_queue:
                task_idx, duration = tasks_queue.popleft()
                weight, idx = heapq.heappop(free)
                ans[task_idx] = idx
                heapq.heappush(busy, (current_time + duration, weight, idx))

        return ans


test_cases = [
    {
        "method": "assignTasks",
        "servers": [3, 3, 2],
        "tasks": [1, 2, 3, 2, 1, 2],
        "expected": [2, 2, 0, 2, 1, 2],
        "case_id": 1,
        "description": "Example 1 from problem statement"
    },
    {
        "method": "assignTasks",
        "servers": [5, 1, 4, 3, 2],
        "tasks": [2, 1, 2, 4, 5, 2, 1],
        "expected": [1, 4, 1, 4, 1, 3, 2],
        "case_id": 2,
        "description": "Example 2 from problem statement"
    },
    {
        "method": "assignTasks",
        "servers": [1],
        "tasks": [1, 2, 3],
        "expected": [0, 0, 0],
        "case_id": 3,
        "description": "Edge case: Only one server available"
    },
    {
        "method": "assignTasks",
        "servers": [10, 63, 95, 16, 85, 57, 83, 95, 6, 29, 71],
        "tasks": [70, 31, 83, 15, 32, 67, 98, 65, 56, 48, 38, 90, 5],
        "expected": [8, 0, 3, 9, 5, 1, 10, 6, 4, 2, 7, 9, 0],
        "case_id": 4,
        "description": "Large test case with varied server weights and task times"
    },
    {
        "method": "assignTasks",
        "servers": [1, 1, 1, 1, 1],
        "tasks": [1, 1, 1, 1, 1],
        "expected": [0, 1, 2, 3, 4],
        "case_id": 5,
        "description": "Edge case: All servers have same weight, tasks assigned by index"
    },
    {
        "method": "assignTasks",
        "servers": [5, 4, 3, 2, 1],
        "tasks": [10, 10, 10, 10, 10],
        "expected": [4, 3, 2, 1, 0],
        "case_id": 6,
        "description": "Edge case: All tasks take same time, servers assigned by weight"
    },
    {
        "method": "assignTasks",
        "servers": [10, 5, 1],
        "tasks": [5, 4, 3, 2, 1, 6, 7, 8],
        "expected": [2, 2, 0, 1, 2, 0, 2, 1],
        "case_id": 7,
        "description": "Multiple servers becoming free at the same time"
    }
]

run_tests()
