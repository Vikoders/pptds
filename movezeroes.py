def moveZeroes(nums):
    n = len(nums)
    left = 0  # pointer for non-zero elements

    # Iterate through the array and move non-zero elements to the left
    for i in range(n):
        if nums[i] != 0:
            nums[left] = nums[i]
            left += 1

    # Fill the remaining elements with zeroes
    for i in range(left, n):
        nums[i] = 0

    return nums
    
# Example 1
nums1 = [0, 1, 0, 3, 12]
print(moveZeroes(nums1))
# Output: [1, 3, 12, 0, 0]

# Example 2
nums2 = [0]
print(moveZeroes(nums2))
# Output: [0]