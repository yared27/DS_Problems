str_ex=input("Enter the string")
def find_longest(str_ex):
    max_len=0
    j =-1
    count={}
    for i,c in enumerate(str_ex):
        j=max(j,count.get(c,-1))
        max_len=max(max_len,i-j)
        count[c]=i
    return max_len
print(find_longest(str_ex))