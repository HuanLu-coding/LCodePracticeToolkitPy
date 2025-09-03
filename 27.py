class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0

        i = 0  # 慢指针，指向要填入的位置
        for j in range(len(nums)):  # 快指针，遍历整个数组
            if nums[j] != val:  # 如果不是要删除的元素
                nums[i] = nums[j]  # 放到慢指针位置
                i += 1  # 慢指针前进

        return i  # 返回新数组长度
