

class Solution:
    def insertionSort(arr):

        for i in range(1, len(arr)):
            currentValue = arr[i]

            while arr[i - 1] > currentValue and i > 0:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                i -= 1

        return arr

    print(insertionSort(
        [11, 6, 3, 47, 8, 45, 3, 46, 8, 9, 54, 3, 57, 4]))
