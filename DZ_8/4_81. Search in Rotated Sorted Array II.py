#https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        i = 0
        j = len(nums) - 1

        while i <= j:
            middle = (i + j) // 2

            if nums[middle] == target:  
                return True
            
            if nums[middle] == nums[i]:
                i += 1
                continue
            
            if nums[j] >= nums[middle]:           
                if nums[middle] < target <= nums[j]:                   
                    i = middle + 1
                else:     
                    j = middle - 1
            else:
                if nums[i] <= target < nums[middle]:                   
                    j = middle - 1        
                else:            
                    i = middle + 1  

        return False
