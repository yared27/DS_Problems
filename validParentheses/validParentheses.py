st = input("Enter the parentheses")


def isValid(self, s: str) -> bool:
    dic = {")": "(", "}": "{", "]": "["}
    st = []
    for i in s:
        if i in dic:
            if st and st[-1] == dic[i]:
                st.pop()
            else:
                return False
        else:
            st.append(i)
    return len(st) == 0
    print(isValid(st))