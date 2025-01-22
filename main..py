s1=input("Enter the strng")
s2=input("Enter the second Element")
# arr=list(s1)
# ar1=list(s2)
def is_agagma(s1,s2):
    for i in range(len(s1)):
        if s1[i] not in s2:
            return False

    return True

print(is_agagma(s1,s2))
