import math

def maxMatrixSum(matrix) -> int:
    numNegatives = 0
    minValue = math.inf
    totalSum = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            curr = matrix[row][col]
            minValue = min(minValue, abs(curr))

            if curr < 0:
                numNegatives += 1

            totalSum += abs(curr)

    if numNegatives % 2 == 0:
        return totalSum
    else: # numNegatives % 2 == 1
        return totalSum - (2 * minValue)
    