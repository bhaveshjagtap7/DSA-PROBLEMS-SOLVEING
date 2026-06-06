"""
LeetCode 560: Subarray Sum Equals K

Problem Statement:
Given an array of integers nums and an integer k, return the total number of 
subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

Difficulty: Medium
Topics: Array, Hash Table, Prefix Sum
"""


# ============================================================================
# EXAMPLES
# ============================================================================
"""
Example 1:
Input: nums = [1, 1, 1], k = 2
Output: 2
Explanation: 
  Subarray [1, 1] starting at index 0: 1 + 1 = 2
  Subarray [1, 1] starting at index 1: 1 + 1 = 2

Example 2:
Input: nums = [1, 2, 3], k = 3
Output: 2
Explanation:
  Subarray [1, 2] starting at index 0: 1 + 2 = 3
  Subarray [3] starting at index 2: 3 = 3

Example 3:
Input: nums = [1, -1, 1, 1], k = 1
Output: 3
Explanation:
  Subarray [1] starting at index 0: 1 = 1
  Subarray [1, -1, 1] starting at index 1: 1 + (-1) + 1 = 1
  Subarray [1] starting at index 3: 1 = 1

Example 4:
Input: nums = [0, 0, 0], k = 0
Output: 6
Explanation:
  All possible subarrays: [0], [0, 0], [0, 0, 0], [0, 0], [0], [0]
  Each sums to 0, total count = 6

Example 5:
Input: nums = [3, 4, 7, 2, -3, 1, 4, 2], k = 7
Output: 4
Explanation:
  Subarrays: [3, 4], [7], [7, 2, -3, 1], [1, 4, 2]
"""



# ============================================================================
# APPROACH 1: BRUTE FORCE
# ============================================================================
"""
Strategy: Check every possible subarray by using nested loops.
- Outer loop: Starting index i
- Inner loop: Ending index j (j >= i)
- Calculate sum from i to j
- If sum equals k, increment count

Time Complexity: O(n³) or O(n²) depending on implementation
Space Complexity: O(1) - Only storing count
"""

def subarraySum_bruteforce(nums, k):
    """
    Brute force approach checking all subarrays.
    
    Args:
        nums: List of integers
        k: Target sum
    
    Returns:
        Number of subarrays whose sum equals k
    """
    array_length = len(nums)
    subarray_count = 0
    
    # Try all possible starting positions
    for start_index in range(array_length):
        current_sum = 0
        
        # Try all possible ending positions
        for end_index in range(start_index, array_length):
            # Add current element to running sum
            current_sum += nums[end_index]
            
            # Check if we found a subarray with sum k
            if current_sum == k:
                subarray_count += 1
    
    return subarray_count