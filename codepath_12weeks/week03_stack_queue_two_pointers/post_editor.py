from collections import deque


def edit_post(post):
  # intiialize a queue 
    queue = deque() 

  # break the string into individual element in a list 
    lst = post.split()
  # loop through the list, reverse individal word
    
    for i in lst:
        i = i[::-1]
        queue.append(i)
        
  # join each element into a string and return 
    ans = " ".join(queue)
    return ans


print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog")) 
