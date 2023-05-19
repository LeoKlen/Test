#https://leetcode.com/problems/minimum-time-to-repair-cars/
import math
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        i = 0
        j = min(ranks) * cars * cars

        while i<j:
            middle = (i + j) // 2
            count = 0
            
            for rank in ranks:
                count += math.floor((middle / rank) ** 0.5)

            if cars > count:
                i = middle + 1
            else:
                j = middle

        return j
