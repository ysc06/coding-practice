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

# Set 1 Problem 5: Content Cleaner # 
**Description:**
Clean a string by removing any pairs of adjascent characters where one is the lowercase of the letter and the other one is the uppercase version. Return the clean string.

**Approach:**
- Handle edge cases (e.g., empty string or single character)
- Initialize an empty stack
- Loop through each character in the input post:
	- If the stack is not empty, and the current character is the same letter with opposite case as the top of the stack,pop the top character (cancel the pair)
	- Otherwise:Push the current character onto the stack
- At the end, join all characters in the stack into a single string and return it.

**What I Learned:**
- Alwasy check if the stack is not empty befoe accessing `stack[-1]` to avoid `IndexError`
- Use `"".join(stack)` to combine characters without spaces between them
