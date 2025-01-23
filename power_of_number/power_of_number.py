
dividend=int(input("Enter thed dividend"))
divisor=int(input("Enter the divisor"))

def gcfFinder(dividend,divisor):
    assert int(dividend)==dividend and int(divisor)==divisor,"The numbers are not integer"
    if divisor<0:
        divisor=-1*divisor
    if dividend<0:
        dividend=-1*dividend
    if divisor==0:
        return  dividend
    else:
        return gcfFinder(divisor,dividend % divisor)

print(gcfFinder(dividend,divisor))