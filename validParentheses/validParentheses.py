st = input("Enter the parentheses")


def isValid(self, s: str) -> bool:
    st = []
    for i in s:
        if i == "(":
            st.append(i)
        elif i == "{":
            st.append(i)
        elif i == "[":
            st.append(i)
        elif st and i == ")" and st[-1] == "(":
            st.pop()
        elif st and i == "]" and st[-1] == "[":
            st.pop()
        elif st and i == "}" and st[-1] == "{":
            st.pop()
        else:
            return False
    return len(st) == 0
    print(isValid(st))