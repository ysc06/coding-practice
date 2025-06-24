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
- Alwasy check if the stack is not empty before accessing `stack[-1]` to avoid `IndexError`
- Use `"".join(stack)` to combine characters without spaces between them

# Set 1 Problem 7: Post Compare#
**Description:**
Given two strings, determine whether they are equal after typed into a text editor. `#` characters represent a backspace, deleting character just before it. 

**Approach:**
- Create a helper function `def backspacing(str)` that returns the final version of a string after simulating typing into a text editor.
- Initialize a stack, loop through the string
    - If the char is `#` and if stack is not empty, pop the last element
    - If the char is not `#`, append  it to the stack
- Use `"".join(stack)` to combine characters in the stack into a single string and return it. 
- In the main function
    - Compare weither `backspacing(draf1)` is equal to `backspacing(draf2)`
    - If they are equal, return True; otherwise, return False 

**What I Learned:**
- Breaking the problem into small, testable helpful functions like `backspacing()` to improve clarity. 
- Alwasy check `if stack:` before popping to avoid `IndexError`.


#Assessment Problem 1: Valid Parenthesis# 
**Pattern: Stack: Matching**
** Description:**
Given a string of brackets `'(){}[]'`, return `True` if all brackets are correctly matched and closed in the right order. A valid string: 1.Matches each opening with the same type of closing, 2.Maintains correct nesting/order

** Thought Process:**
Started by considering edge cases (like empty strings or a single character). I struggled a bit with writing the correct conditions—especially knowing when to check if the stack is empty. Once I realized that stack-matching problems follow a standard logic, the approach became clear.

**Approach:**
- Initialize a stack and a dictionary
- Loop through elements in the string:
    - if it is an **open bracket** -> append to the stack
    - if it is a **closing bracket**, 
        - if the stack is empty, return `False`
         - if `stack[-1]` is the corresponding opening bracket -> `pop`
         - Othersie, return `False`
         
**What I Learned:**
- Stack matching problems follows a standard pattern
- For efficiency and readability, use a dictionary for bracket matching
