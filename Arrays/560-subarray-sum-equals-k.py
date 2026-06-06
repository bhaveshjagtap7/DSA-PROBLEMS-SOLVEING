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



# ============================================================================
# PREFIX SUM CONCEPT EXPLANATION
# ============================================================================
"""
PREFIX SUM DEFINITION:
Prefix sum array stores cumulative sums from start of array.

For nums = [a, b, c, d]:
  prefix_sum[0] = a
  prefix_sum[1] = a + b
  prefix_sum[2] = a + b + c
  prefix_sum[3] = a + b + c + d

KEY INSIGHT:
Sum of subarray from i to j = prefix_sum[j] - prefix_sum[i-1]

Example: nums = [1, 2, 3, 4]
  Sum from index 1 to 2 (elements [2, 3]):
  prefix_sum[2] = 1 + 2 + 3 = 6
  prefix_sum[0] = 1
  Sum = 6 - 1 = 5 (2 + 3 = 5) ✓

TRANSFORMING THE PROBLEM:
We need: subarray_sum(i, j) = k
Which means: prefix_sum[j] - prefix_sum[i-1] = k

Rearranging: prefix_sum[j] - k = prefix_sum[i-1]

CRITICAL OBSERVATION:
If we're at position j and compute current prefix_sum, we need to know 
how many previous positions i-1 had prefix_sum equal to (current_prefix_sum - k).

Why? Because:
  current_prefix_sum - previous_prefix_sum = k
  means subarray from (previous_index + 1) to current_index has sum k

So problem reduces to:
For each position j, count how many previous positions i had:
  prefix_sum[i] = current_prefix_sum - k

This is where hash map optimization comes in!
"""



# ============================================================================
# APPROACH 2: PREFIX SUM ARRAY
# ============================================================================
"""
Strategy: Use prefix sum array to compute subarray sums efficiently.

1. Build prefix sum array
   - prefix[i] = sum of nums[0] to nums[i]
   
2. For each pair (i, j) with i <= j:
   - subarray_sum = prefix[j] - prefix[i-1] (or just prefix[j] if i=0)
   - Count if equals k

Time Complexity: O(n²) - Still nested loops but sum calculation is O(1)
Space Complexity: O(n) - Store prefix sum array
"""

def subarraySum_prefix_array(nums, k):
    """
    Prefix sum array approach for computing subarray sums.
    
    Args:
        nums: List of integers
        k: Target sum
    
    Returns:
        Number of subarrays whose sum equals k
    """
    array_length = len(nums)
    subarray_count = 0
    
    # Build prefix sum array
    prefix_sums = [0] * array_length
    prefix_sums[0] = nums[0]
    
    for i in range(1, array_length):
        prefix_sums[i] = prefix_sums[i - 1] + nums[i]
    
    # Check all subarrays using prefix sums
    for start_index in range(array_length):
        for end_index in range(start_index, array_length):
            # Compute subarray sum using prefix sums
            if start_index == 0:
                current_sum = prefix_sums[end_index]
            else:
                current_sum = prefix_sums[end_index] - prefix_sums[start_index - 1]
            
            # Check if sum equals target
            if current_sum == k:
                subarray_count += 1
    
    return subarray_count



# ============================================================================
# APPROACH 3: HASH MAP OPTIMIZATION
# ============================================================================
"""
Strategy: Use hash map to track frequency of prefix sums.

Key Insight: 
We need: prefix_sum[j] - prefix_sum[i-1] = k
Which means: prefix_sum[j] - k = prefix_sum[i-1]

So at position j, we look for how many previous positions i-1 had
prefix_sum equal to (current_prefix_sum - k).

Algorithm:
1. Initialize hash map with {0: 1} (prefix sum of empty subarray before start)
2. Traverse array, compute running prefix sum
3. For each position:
   - Check if (prefix_sum - k) exists in hash map
   - If yes, add its frequency to count
   - Update hash map with current prefix_sum frequency

Time Complexity: O(n) - Single pass through array
Space Complexity: O(n) - Hash map stores up to n unique prefix sums
"""

def subarraySum_hashmap(nums, k):
    """
    Hash map optimized solution using prefix sums.
    
    Args:
        nums: List of integers
        k: Target sum
    
    Returns:
        Number of subarrays whose sum equals k
    """
    subarray_count = 0
    running_prefix_sum = 0
    
    # Hash map to store frequency of prefix sums seen so far
    # Initialize with {0: 1} to handle subarrays starting from index 0
    prefix_sum_frequency = {0: 1}
    
    # Process each element in array
    for current_element in nums:
        # Update running prefix sum
        running_prefix_sum += current_element
        
        # Check if (running_prefix_sum - k) exists in hash map
        # This means there's a subarray ending at current position with sum k
        required_prefix_sum = running_prefix_sum - k
        
        if required_prefix_sum in prefix_sum_frequency:
            subarray_count += prefix_sum_frequency[required_prefix_sum]
        
        # Update frequency of current prefix sum in hash map
        if running_prefix_sum in prefix_sum_frequency:
            prefix_sum_frequency[running_prefix_sum] += 1
        else:
            prefix_sum_frequency[running_prefix_sum] = 1
    
    return subarray_count



# ============================================================================
# FINAL OPTIMIZED SOLUTION
# ============================================================================
"""
Optimal Solution: Single pass with hash map

Key Components:
1. Hash map to track prefix sum frequencies
2. Single pass through array
3. Mathematical insight: current_sum - target_sum = needed_sum

Algorithm Steps:
Initialize:
  count = 0
  prefix_sum = 0
  sum_frequency = {0: 1}  # Important for subarrays starting at index 0

For each element:
  1. Add to prefix_sum
  2. Check if (prefix_sum - k) exists in hash map
  3. If yes, add frequency to count
  4. Update hash map with current prefix_sum

Time Complexity: O(n) - Single pass
Space Complexity: O(n) - Hash map in worst case
"""

def subarraySum_optimized(nums, k):
    """
    Optimal solution using hash map and prefix sums.
    
    Args:
        nums: List of integers
        k: Target sum
    
    Returns:
        Number of subarrays whose sum equals k
    
    Complexity:
        Time: O(n) - Single pass through array
        Space: O(n) - Hash map for prefix sums
    """
    subarray_count = 0
    running_prefix_sum = 0
    prefix_sum_frequency = {0: 1}  # Initialize with prefix sum 0
    
    for num in nums:
        # Update current cumulative sum
        running_prefix_sum += num
        
        # Check if we have seen the required prefix sum
        required_prefix_sum = running_prefix_sum - k
        
        if required_prefix_sum in prefix_sum_frequency:
            subarray_count += prefix_sum_frequency[required_prefix_sum]
        
        # Update frequency of current prefix sum
        prefix_sum_frequency[running_prefix_sum] = prefix_sum_frequency.get(running_prefix_sum, 0) + 1
    
    return subarray_count


class Solution(object):
    """LeetCode 560: Subarray Sum Equals K"""
    
    def subarraySum(self, nums, k):
        """
        Return total number of contiguous subarrays whose sum equals k.
        
        Args:
            nums: List of integers
            k: Target sum
        
        Returns:
            Number of subarrays with sum equal to k
        """
        return subarraySum_optimized(nums, k)



# ============================================================================
# COMPLEXITY ANALYSIS
# ============================================================================
"""
APPROACH COMPARISON:

Approach              Time         Space        Notes
────────────────────────────────────────────────────────────────────
Brute Force           O(n³)        O(1)         Check all subarrays
Improved Brute Force  O(n²)        O(1)         Running sum optimization
Prefix Sum Array      O(n²)        O(n)         Store prefix sums
Hash Map Optimized    O(n)         O(n)         Optimal! ✓

WHY HASH MAP IS OPTIMAL:
- Must check all subarrays → At least O(n²) with brute force
- Hash map reduces to O(n) by eliminating inner loop
- Mathematical insight: current_sum - target_sum = needed_sum
- Trade space for time: O(n) space saves O(n²) time

TIME COMPLEXITY DETAILS:
Brute Force (nested loops):
  Outer loop: n iterations
  Inner loop: n/2 average iterations
  Sum calculation: j-i operations (O(n) worst)
  Total: O(n³) worst case

Hash Map Optimized:
  Single pass through array: O(n)
  Hash map operations: O(1) average case
  Total: O(n) ✓

SPACE COMPLEXITY DETAILS:
Brute Force: O(1) - Only count variable
Prefix Sum Array: O(n) - Store prefix sums
Hash Map: O(n) - Store up to n unique prefix sums

SCALABILITY:
For n = 20,000 (max constraint):
- Brute Force: ~4 trillion operations (way too slow!)
- Hash Map: ~20,000 operations (fast) ✓

RECOMMENDATION: Use hash map optimized solution!
"""
