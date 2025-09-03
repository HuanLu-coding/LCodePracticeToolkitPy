# 80. Remove Duplicates from Sorted Array II
# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.
#
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
#
# ### Custom Judge:
# The judge will test your solution with the following code:
#
# ```
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
#
# int k = removeDuplicates(nums); // Calls your implementation
#
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# ```
#
# If all assertions pass, then your solution will be accepted.
#
# ### Constraints:
# - `1 <= nums.length <= 3 * 10^4`
# - `-10^4 <= nums[i] <= 10^4`
# - nums is sorted in non-decreasing order.
#
# ### Example 1:
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
#
# ### Example 2:
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
from test.test_suite import run_tests
from typing import *


# 由于数组是已排序的，相同的元素会聚在一起，这简化了重复项的识别和处理。
# 我们需要一个机制来跟踪当前正在处理的元素已经出现了多少次，
# 或者更巧妙地，只需要判断当前元素是否应该被保留（即是否是该元素的前两次出现）。
#
# 可以用一个指针（write_idx）指示结果数组的下一个写入位置，另一个指针（read_idx）遍历原始数组。
# 更简洁的判断条件:
#
# 考虑结果数组的前 write_idx 个元素 nums[0...write_idx-1]。这些是已经确定要保留的元素。
# 我要决定是否将 nums[read_idx] 放到 nums[write_idx]。
# 如果 write_idx < 2 (即结果数组中元素少于两个)，那么我总是可以放入 nums[read_idx]，因为它不可能是第三次或更多次出现。
# 如果 write_idx >= 2，我要放入 nums[read_idx] 的前提是，它不与 nums[write_idx - 1] 和 nums[write_idx - 2] 同时相同。因为如果 nums[read_idx] == nums[write_idx - 1] == nums[write_idx - 2]，那就意味着当前 nums[read_idx] 是该元素的第三次或更多次出现。
# 所以，只要 write_idx < 2 或者 nums[read_idx] 不等于 nums[write_idx - 2]，我就可以保留 nums[read_idx]。 这个条件 nums[read_idx] != nums[write_idx - 2] 巧妙地概括了是否是第三次或更多次出现的情况。如果 nums[read_idx] 是新元素，它肯定不等于 nums[write_idx - 2]。如果 nums[read_idx] 是第二次出现，它等于 nums[write_idx - 1] 但不等于 nums[write_idx - 2] (因为 nums[write_idx - 2] 是前一个不同的元素或当前元素的第一次出现)，所以条件 nums[read_idx] != nums[write_idx - 2] 成立。如果 nums[read_idx] 是第三次或更多次出现，它等于 nums[write_idx - 1] 并且等于 nums[write_idx - 2]，条件 nums[read_idx] != nums[write_idx - 2] 不成立。
#
# 解决方案: 双指针法 (Two Pointers)。
# 数据结构: 利用原数组 nums (in-place)。
# 算法:
# 1. 初始化写入指针 write 为 0。
# 2. 遍历数组，使用读取指针 read 从 0 到 len(nums) - 1。
# 3. 在每次迭代中，检查当前元素 nums[read] 是否应该被保留。保留的条件是：
#       write < 2 (始终保留前两个元素)
#       或者 nums[read] != nums[write - 2] (当前元素与写入位置前两个元素不同，意味着不是第三次或更多次出现)。
# 4. 如果满足保留条件，将 nums[read] 复制到 nums[write]，并递增 write。
# 5. 无论是否保留，都递增 read (隐式在 for 循环中完成)。
# 6. 遍历结束后，write 的值即为新长度。
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # 如果数组长度小于等于2，本身就符合条件，直接返回长度
        if len(nums) <= 2:
            return len(nums)

        # write 指针：表示下一个有效元素应该写入的位置
        # 它也代表了处理完成后，有效元素的数量（即新长度）
        write = 0

        # read 指针：遍历整个数组
        for read in range(len(nums)):
            # 判断当前元素 nums[read] 是否应该被保留
            # 保留的条件：
            # 1. write < 2：前两个位置总是可以写入，因为它们不可能是第三次或更多次出现
            # 2. nums[read] != nums[write - 2]：
            #    需要仔细理解 write - 2 为什么能用来判断是否是第三次出现。这是此算法中最巧妙也是最需要理解的地方。
            #    当 write >= 2 时，这个条件检查当前元素是否与“已确定保留部分”的倒数第三个元素不同。
            #    如果不同，说明 nums[read] 要么是一个新数字，要么是已保留数字的第二次出现。
            #    如果相同，说明 nums[read] 是已保留数字的第三次或更多次出现，不应保留。
            if write < 2 or nums[read] != nums[write - 2]:
                # 如果满足保留条件，将当前元素复制到 write 指针指向的位置
                nums[write] = nums[read]
                # 移动 write 指针到下一个待写入位置
                write += 1

        # write 的最终值即为新长度
        return write


# 本质上是用一个计数器`count`辅助双指针
# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         # write 指针：表示下一个有效元素应该写入的位置
#         write = 0
#         # count 变量：跟踪当前正在处理的元素已经连续出现了多少次
#         count = 0
#
#         # read 指针：遍历整个数组
#         for read in range(len(nums)):
#             # 检查当前元素 nums[read] 是否与前一个处理的元素相同
#             # 注意：这里的前一个元素是 nums[read-1] 在原始数组中的前一个，而不是 nums[write-1]
#             if read > 0 and nums[read] == nums[read - 1]:
#                 # 如果相同，计数增加
#                 count += 1
#             else:
#                 # 如果不同（是新元素），计数重置为 1
#                 count = 1
#
#             # 判断当前元素 nums[read] 是否应该被保留
#             # 只有当前元素在其连续序列中出现次数 <= 2 时才保留
#             if count <= 2:
#                 # 如果满足保留条件，将当前元素复制到 write 指针指向的位置
#                 nums[write] = nums[read]
#                 # 移动 write 指针到下一个待写入位置
#                 write += 1
#
#         # write 的最终值即为新长度
#         return write
#

test_cases = [
    {
        "method": "removeDuplicates",
        "nums": [1, 1, 1, 2, 2, 3],
        "expected": 5,
        "expected_nums": [1, 1, 2, 2, 3],
        "case_id": 1,
        "description": "Standard case with duplicates"
    },
    {
        "method": "removeDuplicates",
        "nums": [0, 0, 1, 1, 1, 1, 2, 3, 3],
        "expected": 7,
        "expected_nums": [0, 0, 1, 1, 2, 3, 3],
        "case_id": 2,
        "description": "Standard case with more duplicates"
    },
    {
        "method": "removeDuplicates",
        "nums": [1, 2, 3],
        "expected": 3,
        "expected_nums": [1, 2, 3],
        "case_id": 3,
        "description": "No duplicates beyond limit"
    },
    {
        "method": "removeDuplicates",
        "nums": [1, 1],
        "expected": 2,
        "expected_nums": [1, 1],
        "case_id": 4,
        "description": "Edge case: Exactly two duplicates"
    },
    {
        "method": "removeDuplicates",
        "nums": [1],
        "expected": 1,
        "expected_nums": [1],
        "case_id": 5,
        "description": "Edge case: Single element array"
    },
    {
        "method": "removeDuplicates",
        "nums": [1, 1, 1, 1, 1],
        "expected": 2,
        "expected_nums": [1, 1],
        "case_id": 6,
        "description": "Edge case: All same elements"
    },
    {
        "method": "removeDuplicates",
        "nums": [-1, -1, -1, 0, 0, 0, 1, 1, 1],
        "expected": 6,
        "expected_nums": [-1, -1, 0, 0, 1, 1],
        "case_id": 7,
        "description": "Negative and zero elements"
    }
]

run_tests()
