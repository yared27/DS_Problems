num=input("Enter the number")
def is_palindrom(n):
    l=0
    r=len(num)-1
    while l<=r:
        if n[l]!=n[r]:
            return False
        l+=1
        r-=1
    return True
print(is_palindrom(num))
l="yared"
print(l[0])