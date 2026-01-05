import math

def isThree(n: int) -> bool:
    numDivisors = 0

    for num in range(1, int(math.sqrt(n)) + 1):
        if n % num == 0:
            complement = n / num

            if complement == num:
                numDivisors += 1
            else:
                numDivisors += 2

            if numDivisors > 3:
                return False

    return numDivisors == 3