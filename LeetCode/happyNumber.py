# Write an algorithm to determine if a number n is "happy".

# A happy number is a number defined by the following process: Starting
# with any positive integer, replace the number by the sum of the squares of
# its digits, and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1. Those numbers
# for which this process ends in 1 are happy numbers.

# Return True if n is a happy number, and False if not.

import math


class Solution:
    def isHappy(self, n: int) -> bool:

        hashSet = set()  # creates the set

        while n != 1:  # loops untill the answer is found
            currentNumber = n
            summ = 0  # currentSum between digits
            while currentNumber is not 0:  # if currentNumber is 0, then the digits have been added
                # square and add the currentDigit
                summ += (currentNumber % 10) ** 2
                # Divide number by 10 and round down
                currentNumber = math.floor(currentNumber / 10)
            if summ in hashSet:  # check if summ is already in set, if so, then it is on a cycle
                return False
            hashSet.add(summ)  # add summ to set
            n = summ

        return True
