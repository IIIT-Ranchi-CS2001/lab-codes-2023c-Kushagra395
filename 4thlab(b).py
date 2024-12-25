# Create a list of int using list comprehension [multiple input from keyboard].
# Find the mean, median, and mode of the given list (usage of specific modules
# such as statistics is strictly prohibited. Lab problems are for you to build-up
# logic and strengthen your understanding of the topic & its concepts)
nums = list(map(int, input("Enter numbers: ").split()))

# Mean
mean = sum(nums) / len(nums)

# Median
nums.sort()
median = nums[len(nums)//2] if len(nums) % 2 != 0 else (nums[len(nums)//2 - 1] + nums[len(nums)//2]) / 2

# Mode
mode = max(set(nums), key=nums.count)

print(f"Mean: {mean}, Median: {median}, Mode: {mode}")
