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

