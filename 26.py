class Solution:
    def removeDuplicates(nums):
        if not nums: return 0

        # 使用双指针技术
        # i 是慢指针，也是新数组的索引
        i = 0

        # j 是快指针，用于遍历数组
        for j in range(1, len(nums)):
            # 当发现一个新元素时
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
