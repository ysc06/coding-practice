def isvalid(s):
    # initialize a stack 
    st = []
    # loop through elements in the string
    dic = {')' : '(' , ']' : '[' , '}' : '{' }
    for i in s:
        # if open brackets, append to stack
        if i in dic.values():
            st.append(i)
        # if closing brackets,
        else:
            if not st:
                return False  
            else:
                if dic[i] == st[-1]:
                    st.pop()
                else:
                    return False

            # if stack is empty, return False 
    return True if not st else False 
