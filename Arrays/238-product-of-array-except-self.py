"""
LeetCode 238: Product of Array Except Self

Problem Statement:
Given an integer array nums, return an array answer such that answer[i] is equal 
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operator.

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow-up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)

Difficulty: Medium
Topics: Array, Prefix Sum
"""


# ============================================================================
# EXAMPLES
# ============================================================================
"""
Example 1:
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
Explanation:
  answer[0] = 2 * 3 * 4 = 24 (product of all except nums[0])
  answer[1] = 1 * 3 * 4 = 12 (product of all except nums[1])
  answer[2] = 1 * 2 * 4 = 8  (product of all except nums[2])
  answer[3] = 1 * 2 * 3 = 6  (product of all except nums[3])

Example 2:
Input: nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]
Explanation:
  answer[0] = 1 * 0 * (-3) * 3 = 0
  answer[1] = (-1) * 0 * (-3) * 3 = 0
  answer[2] = (-1) * 1 * (-3) * 3 = 9
  answer[3] = (-1) * 1 * 0 * 3 = 0
  answer[4] = (-1) * 1 * 0 * (-3) = 0

Example 3:
Input: nums = [2, 3, 4, 5]
Output: [60, 40, 30, 24]
Explanation:
  answer[0] = 3 * 4 * 5 = 60
  answer[1] = 2 * 4 * 5 = 40
  answer[2] = 2 * 3 * 5 = 30
  answer[3] = 2 * 3 * 4 = 24
"""



# ============================================================================
# APPROACH 1: BRUTE FORCE
# ============================================================================
"""
Strategy: For each position i, calculate product of all elements except i.
Use nested loops to multiply all elements except current index.

Time Complexity: O(n²) - For each element, iterate through array
Space Complexity: O(1) - Only output array (doesn't count as extra space)
"""

def productExceptSelf_bruteforce(nums):
    """Brute force approach with nested loops."""
    n = len(nums)
    result = []
    
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        result.append(product)
    
    return result
