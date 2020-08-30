# Write a function that takes an unsigned integer
# and return the number of '1' bits it has (also known as the Hamming weight).

class Solution:
    def hammingWeight(self, n: int) -> int:
        # bin is a method which converts integers into binary strings
        return bin(n).count('1')
