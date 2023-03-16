#https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if nums.count(0) == len(nums):
            return nums

        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                nums.append(nums[i])
                nums.pop(i)
        return nums
