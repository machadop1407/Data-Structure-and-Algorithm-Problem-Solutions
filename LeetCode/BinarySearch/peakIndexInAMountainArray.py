# Let's call an array arr a mountain if the following properties hold:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... arr[i-1] < arr[i]
# arr[i] > arr[i+1] > ... > arr[arr.length - 1]
# Given an integer array arr that is guaranteed to be a mountain,
# return any i such that
# arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:

        left = 0
        right = len(A) - 1

        while left <= right:
            midpoint = math.floor((left+right) / 2)

            if A[midpoint - 1] < A[midpoint] and A[midpoint + 1] < A[midpoint]:
                return midpoint
            elif A[midpoint - 1] < A[midpoint]:
                left = midpoint
            else:
                right = midpoint

        return 0
