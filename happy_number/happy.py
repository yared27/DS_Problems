n = int(input("Enter a number"))

def isHappy( n: int) -> bool:
    vist = set()
    while n not in vist:
        vist.add(n)
        sum = 0
        while n:
            r = n%10
            n = n//10
            sum += r ** 2
        n = sum
        if n == 1:
            return True

    return False

print(isHappy(n))