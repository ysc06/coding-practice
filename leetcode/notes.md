# LC560: Subarray Sum Equals K #
**Pattern Matching:** Prefix sum + hash map pattern 
**Description:**
Count the number of continuous subarrays that sum up to a given k. 

** Thought Process:**
I initially tried a one-sum approach that only accumulated values from index 0.This failed to capture subarrays that started **anywhere else** in the array. 

**Approach:**
- Initialize a count variable, and a frequency dictionary: key is prefix_sum; value is frequency. 
- Loop through `nums`, add num to `prefix_sum`. 
- At each step, If `prefix_sum - k` appears in a dictionary, add the frequency to `count`. 
- Increment the count of the current `dict[prefix_sum]` 

**What I Learned:**  
- If `prefix_sum - k` is in the dictionary, a subarray ending at the current index sums to `k`.
- Subarrays can start from **any index**, not just from the beginning.

# LC 125. Valid Palindrome #
**Easy**
**Two Pointers**
**Thought Process:** 
Initial approach used string preprocessing → two pointers, but that caused O(n) space due to new string creation.
**Approach:**
- Initialize left, right pointers.
- While left < right:
    - Skip non-alphanumeric chars using .isalnum().
    - Compare lowercase chars at both pointers.
    - If mismatch → return False; else, move inward.
**What I learned:**
- .isalnum() filters alphanumerics.
- ''.join() works on lists/strings.
- Two pointers avoid extra space — O(1) space.
- Step by step filters: the outer `while l < r` drives the process; the inner `while` skips invalid chars

# LC 20. Valid Parenthesis #
**Easy**
**Stack**
**Thought Process:**
At first, I didn’t clearly separate the logic for open/close/invalid characters. I also made small mistakes like treating loop variables as indices. Once I grouped conditions by character type (open, close, invalid), the logic became clearer.
**Approach:**
- Use a dictionary: closed → open bracket mapping
- Loop through each character:
    - If it's an open bracket: stack.append()
    - If it's a closing bracket:
        - Return False if stack is empty or top doesn’t match
        - Else stack.pop()
    - Else (invalid character): return False
- After loop, return not stack
**What I learned:**
- Use hashmaps for fast lookup
- return not stack returns True if stack is empty
- Separating logic into clear branches improves readability and avoids logic errors

# LC 155. Min Stack #
**Mid**
**Stack**
**Thought process:**
I used `self.lst` to store stack values and initially set `self.minimum = float('inf')` to track the minimum. However, I overlooked the case where the minimum could be popped. This made me realize the importance of maintaining a history of minimums to keep `getMin()` accurate and efficient.
**Approach:**
- Initialize two stacks, one for all values(`self.lst`), and one for tracking minimums(`self.history`).
- In `push(val)`, alwasy append to `self.lst` if `self.history` is empty or `val<=self.history[-1]`, also append `val` to `self.history`.
- In `pop()`, remove the top of `self.lst`. If the popped value equals `self.history[-1]`, also pop from `self.history` to keep the minimum in sync. 
**What I learned:**
- To maintain the correct minimum, it is important to compare values during both `push(val)` and `pop()`. Tracking historical minimums ensures `getMin()` remains accurate even after popping values.
