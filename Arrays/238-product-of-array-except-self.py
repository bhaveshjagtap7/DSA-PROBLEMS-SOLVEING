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
    """
    Brute force approach with nested loops.
    
    Args:
        nums: List of integers
    
    Returns:
        List where result[i] = product of all elements except nums[i]
    """
    array_length = len(nums)
    result_array = []
    
    # For each position in array
    for current_index in range(array_length):
        current_product = 1
        
        # Multiply all elements except the one at current_index
        for multiply_index in range(array_length):
            if multiply_index != current_index:
                current_product *= nums[multiply_index]
        
        result_array.append(current_product)
    
    return result_array



# ============================================================================
# APPROACH 2: PREFIX AND SUFFIX PRODUCTS (Optimized)
# ============================================================================
"""
Strategy: Use prefix and suffix product arrays.

Key Insight:
For each position i, the result is:
  result[i] = (product of all elements before i) × (product of all elements after i)
  result[i] = prefix[i-1] × suffix[i+1]

We can precompute:
- prefix[i] = product of nums[0] to nums[i]
- suffix[i] = product of nums[i] to nums[n-1]

Time Complexity: O(n) - Three separate passes
Space Complexity: O(n) - Two additional arrays for prefix and suffix
"""

def productExceptSelf_prefix_suffix(nums):
    """
    Optimized approach using prefix and suffix product arrays.
    
    Args:
        nums: List of integers
    
    Returns:
        List where result[i] = product of all elements except nums[i]
    """
    array_length = len(nums)
    
    # Step 1: Build prefix products array
    # prefix[i] = product of all elements from index 0 to i
    prefix_products = [1] * array_length
    prefix_products[0] = nums[0]
    
    for i in range(1, array_length):
        prefix_products[i] = prefix_products[i - 1] * nums[i]

    
    # Step 2: Build suffix products array
    # suffix[i] = product of all elements from index i to n-1
    suffix_products = [1] * array_length
    suffix_products[array_length - 1] = nums[array_length - 1]
    
    for i in range(array_length - 2, -1, -1):
        suffix_products[i] = suffix_products[i + 1] * nums[i]
