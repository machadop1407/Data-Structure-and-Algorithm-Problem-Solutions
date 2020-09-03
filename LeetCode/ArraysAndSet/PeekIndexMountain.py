# Let's call an array A a mountain if the following properties hold:

# A.length >= 3
# There exists some 0 < i < A.length - 1
# such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:

        left = 0
        right = len(A)-1

        while left <= right:
            midpoint = math.floor((left + right)/2)

            if A[midpoint] > A[midpoint - 1] and A[midpoint] > A[midpoint + 1]:
                return midpoint

            elif A[midpoint] < A[midpoint - 1]:
                right = midpoint
            else:
                left = midpoint

        return left
