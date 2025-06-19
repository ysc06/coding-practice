# Set 1 Problem 6: Post Editor #

**Description:**
Reverse the character in each word of a post, preserving the word order and spacing. 

**Approach:**
- Split the string by spaces to get individual words  
- Loop through the list, reverse each word (`word[::-1]`), and add to a queue or result list  
- Join the reversed words using `" ".join(...)` to return the final sentence

**What I Learned:**  
- Using a nested loop to append each character individually ends up saving letters, not whole words  
- Slicing with `w[::-1]` looks simple, but it performs internal looping under the hood to reverse the string efficiently  


