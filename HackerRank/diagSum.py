# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# For example, the square matrix  is shown below:


def diagonalDifference(arr):
    leftDiagSum = 0
    rightDiagSum = 0

    step = 0

    for i in range(len(arr)):
        leftDiagSum += arr[step][step]
        step += 1

    stepBack = len(arr[0]) - 1
    step = 0
    for i in range(len(arr)):
        rightDiagSum += arr[step][stepBack]
        stepBack -= 1
        step += 1

    return abs(leftDiagSum - rightDiagSum)
