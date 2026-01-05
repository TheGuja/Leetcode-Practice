def sumFourDivisors(nums: List[int]) -> int:
    res = 0
    for num in nums:
        numDivisors = 0
        sum = 0
        
        for divisor in range(1, int(sqrt(num)) + 1):
            if num % divisor == 0:
                complement = num // divisor

                if divisor == complement:
                    numDivisors += 1
                    sum += divisor
                else:
                    numDivisors += 2
                    sum += divisor + complement

                if numDivisors > 4:
                    break

        if numDivisors == 4:
            res += sum

    return res