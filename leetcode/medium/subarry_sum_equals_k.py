def subarray_sum(nums, k): 
	# initialize a dictonary to keep track of prefix sum and frequency 
	# count = 0 
	dict = {0:1} 
	count = 0 
	prefix_sum = 0
	

	# loop through elements in nums
	# add num to the current prefix_sum
	# check if there current sum - previous sum equals k
	for num in nums: 
		prefix_sum += num 

		if (prefix_sum - k) in dict: 
			count += dict[prefix_sum - k]

		dict[prefix_sum] = dict.get(prefix_sum, 0) + 1

	return count
