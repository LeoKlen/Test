#https://leetcode.com/problems/search-a-2d-matrix/description/
def in_list(matrix,true_list,target, i, j):

    middle = (i + j) // 2

    if i > j:
        return False

    if matrix[true_list][middle] == target:
        return True

    if matrix[true_list][middle] < target:
        return in_list(matrix, true_list, target, middle + 1, j)
    else:
        return in_list(matrix, true_list, target, i, middle - 1)

    
    
    
    
    
    #if middle == targ:
    if target >  matrix[true_list][middle]:
        return in_list(matrix, true_list,target, middle + 1, j)
    if target <  matrix[true_list][middle]:
        return in_list(matrix, true_list,target, i, middle - 1)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                return in_list(matrix, i, target, 0, len(matrix[0])-1)

        return False
