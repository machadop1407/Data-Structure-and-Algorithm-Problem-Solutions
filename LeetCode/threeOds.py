# Given an integer array arr, return true if there are three
# consecutive odd numbers in the array. Otherwise, return false.

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        oddCount = 0

        for i in arr:
            if i % 2 is not 0:
                oddCount += 1
                if oddCount == 3:
                    return True
            else:
                oddCount = 0

        return False
