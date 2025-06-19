def clean_post(post):
# if len(post)< 2, return post
    if len(post) < 2:
        return post 
 # loop through post
    stack = []
    for i in post: 
    # if matching with the elemnt on the stack, pop 
        if stack and i != stack[-1] and i.lower() == stack[-1].lower(): # must make sure stack is not empty otherwise index out of range # opposite case. Latter is lowercase. 
            stack.pop() # must read the prompt carefully aA and Aa both need to be cleaned 
    # else, add to stack
        else:
            stack.append(i)
# if stack not empty, return stack 

    return "".join(stack) # join, empty string

print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 

