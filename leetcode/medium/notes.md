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
