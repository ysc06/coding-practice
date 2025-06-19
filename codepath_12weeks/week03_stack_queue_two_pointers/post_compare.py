def post_compare(draft1, draft2):
    # use helper function to determin whehter two strings are the same
    if backspacing(draft1) == backspacing(draft2): 
        return True
    else:
        return False
def backspacing(str):
    # intiialize a stack
    stack = []
    # loop through str
    for i in str: 
        # if the char is "#"
        if i == "#":
            # if stack, pop stack[-1]
            if stack: 
                stack.pop()
            # else, continue 
        # else, append char to stack
        else:
            stack.append(i)

    # return "".join(stack)
    return "".join(stack)
