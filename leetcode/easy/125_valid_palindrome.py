class Solution:
    def isPalindrome(self, s: str) -> bool:
        # process the string by making all lowercased and removing non-alphanumeric chars
        # set up two pointers: one on the right end and the other on the left end
        # set a while loop to ensure the left pointer won't go beyond the right one
            # if they are the same, move toward the center by one step
            # if not, return False 
        # return True
        new_str = s.replace(" ","")
        new_str = new_str.lower()
        new_str = "".join(char for char in new_str if char.isalnum())

        lpt = 0
        rpt = len(new_str)-1
        while lpt <= rpt: 
            if new_str[lpt] == new_str[rpt]:
                lpt += 1
                rpt -= 1
            else:
                return False
        return True
        
# Time, space: O(n), O(n)

-----------
# Optimized Solution
# Time, space: O(n), O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initialize two pointers
        # set while loop and skip non-alphanumeric char
        # compare the chars on either pointers, if not the same, return false
        # return True after the loop break

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l<r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
