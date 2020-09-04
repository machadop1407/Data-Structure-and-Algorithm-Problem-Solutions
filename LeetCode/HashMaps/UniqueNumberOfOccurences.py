# Given an array of integers arr, write a function
# that returns true if and only if the number of
# occurrences of each value in the array is unique.

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashMap = dict()

        for i in arr:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1

        hashSet = set()
        for key, value in hashMap.items():
            if value in hashSet:
                return False
            hashSet.add(value)

        return True
