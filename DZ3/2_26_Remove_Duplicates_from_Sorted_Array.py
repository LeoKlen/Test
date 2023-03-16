#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution:
    def removeDuplicates(self, data: List[int]) -> int:
        
        l = 0

        for r in range(1, len(data)):
            if data[r] != data[l]:
                l+=1
            data[l] = data[r]

        return l+1
