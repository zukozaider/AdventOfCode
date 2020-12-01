## Part 1 Solution

def twoSum(nums, target):
    seen = {}
    for i, v in enumerate(nums):
        remaining = target - v
        if remaining in seen:
            return [remaining, v]
        seen[v] = i
    return []

values = twoSum(nums, 2020)
print(f"Part 1 Solution: {values[0]*values[1]}")


## Part 2 Solultion

def threeSum(nums, target):
	for i in range(len(nums) - 1):
		two_sum = twoSum(nums, target - nums[i])
		if two_sum:
			return[nums[i], two_sum[0], two_sum[1]]

values = threeSum(nums, 2020)
print(f"Part 2 Solution: {values[0]*values[1]*values[2]}")
