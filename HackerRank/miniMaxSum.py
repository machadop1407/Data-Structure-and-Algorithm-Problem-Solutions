# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Example

# The minimum sum is  and the maximum sum is . The function prints

# 16 24

def miniMaxSum(arr):
    sumArray = []
    for i in arr:
        tempArr = arr.copy()
        tempArr.remove(i)
        sumArray.append(sum(tempArr))

    print(str(min(sumArray)) + " " + str(max(sumArray)))
