x = 2.0
n = 10

def myPow(x: float, n: int) -> float:
    if n == 0:
            return 1.0

    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0
    current_product = x

    while n:
        if n % 2 == 1:
            result *= current_product
        
        current_product *= current_product
        n //= 2

    return result  

print(myPow(x, n))
