#https://leetcode.com/problems/merge-sorted-array/description/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        for i in range(n):
         
            nums1[m+i] = nums2[i]
            
            for j in range(m+i,  -1, -1):
                
                
                if(j-1 >= 0 and nums1[j-1] > nums1[j]):
                    nums1[j], nums1[j-1] = nums1[j-1], nums1[j]
                else:
                    break
        return nums1
