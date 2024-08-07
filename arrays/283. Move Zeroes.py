from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_non_zero = 0

        # Iterate through the array
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap elements if current element is non-zero
                nums[next_non_zero], nums[i] = nums[i], nums[next_non_zero]
                # Move the pointer to the next position
                next_non_zero += 1


# Example 1
nums1 = [0, 1, 0, 3, 12]
obj = Solution()
obj.moveZeroes(nums1)
print(nums1)  # Output: [1, 3, 12, 0, 0]

# Example 2
nums2 = [0]
obj.moveZeroes(nums2)
print(nums2)  # Output: [0]