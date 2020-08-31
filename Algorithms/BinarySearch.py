
# Given a binary tree and a target, return the index of the target
# Make it O(log(n))
def binarySearch(root: Tree, target: number):

    left = 0
    right = len(nums)-1

    while left <= right:
        midpoint = math.floor(left + (right - left) / 2)
        if nums[midpoint] < target:
            left = midpoint + 1
        elif nums[midpoint] > target:
            right = midpoint - 1
        else:
            return midpoint

    return -1
