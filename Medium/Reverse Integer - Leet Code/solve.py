example1 = 1534236469


def reverse(x: int) -> int:
        num = list(str(abs(x)))
        left, right = 0, len(num) - 1

        while left < right:
            num[left], num[right] = num[right], num[left]
            left, right = left + 1, right - 1

        if int(''.join(num)) > 2**31:
            return 0

        if x < 0:
            return int(''.join(num)) * (-1)

        return int(''.join(num))
    
    
print(reverse(example1))
