# Given an array of integers where 1 ≤ a[i] ≤ n
# (n = size of array), some elements appear twice
# and others appear once.

# Find all the elements of [1, n] inclusive that
# do not appear in this array.

# Could you do it without extra space and in O(n)
# runtime? You may assume the returned list does not
# count as extra space.

def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
     size = len(nums)
      hashSet = set()

       for i in nums:
            hashSet.add(i)

        arr = []
        for i in range(1, size+1):
            if i not in hashSet:
                arr.append(i)

        return arr
