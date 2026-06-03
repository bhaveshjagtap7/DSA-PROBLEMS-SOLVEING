"""
LeetCode 169: Majority Element

Problem Statement:
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Constraints:
- n == nums.length
- 1 <= n <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9

Follow-up: Could you solve the problem in linear time and in O(1) space?

Difficulty: Easy
Topics: Array, Hash Table, Divide and Conquer, Sorting, Counting
"""


# ============================================================================
# EXAMPLES
# ============================================================================
"""
Example 1:
Input: nums = [3, 2, 3]
Output: 3
Explanation: 3 appears 2 times, which is more than ⌊3/2⌋ = 1

Example 2:
Input: nums = [2, 2, 1, 1, 1, 2, 2]
Output: 2
Explanation: 2 appears 4 times, which is more than ⌊7/2⌋ = 3

Example 3:
Input: nums = [1]
Output: 1
Explanation: 1 appears 1 time, which is more than ⌊1/2⌋ = 0

Example 4:
Input: nums = [6, 5, 5]
Output: 5
Explanation: 5 appears 2 times, which is more than ⌊3/2⌋ = 1

Example 5:
Input: nums = [10, 9, 9, 9, 10]
Output: 9
Explanation: 9 appears 3 times, which is more than ⌊5/2⌋ = 2
"""



# ============================================================================
# APPROACH 1: BRUTE FORCE
# ============================================================================
"""
Strategy: Count occurrences of each element using nested loops.
For each element, count how many times it appears in the array.
If count > n/2, return that element.

Time Complexity: O(n²) - Nested loops
Space Complexity: O(1) - No extra space used
"""

def majorityElement_bruteforce(nums):
    """
    Brute force approach with nested loops.
    
    Args:
        nums: List of integers
    
    Returns:
        The majority element (appears more than n/2 times)
    """
    array_length = len(nums)
    majority_threshold = array_length // 2
    
    # Check each element
    for current_element in nums:
        occurrence_count = 0
        
        # Count how many times current element appears
        for element in nums:
            if element == current_element:
                occurrence_count += 1
        
        # If count exceeds threshold, we found majority element
        if occurrence_count > majority_threshold:
            return current_element



# ============================================================================
# APPROACH 2: HASH MAP (Better Approach)
# ============================================================================
"""
Strategy: Use hash map to count frequency of each element in single pass.
Store counts in dictionary, then find element with count > n/2.

Time Complexity: O(n) - Single pass through array
Space Complexity: O(n) - Hash map stores up to n unique elements
"""

def majorityElement_hashmap(nums):
    """
    Hash map approach for counting element frequencies.
    
    Args:
        nums: List of integers
    
    Returns:
        The majority element (appears more than n/2 times)
    """
    array_length = len(nums)
    majority_threshold = array_length // 2
    
    # Dictionary to store element frequencies
    frequency_map = {}
    
    # Count frequency of each element
    for element in nums:
        frequency_map[element] = frequency_map.get(element, 0) + 1
        
        # Early exit: if we found majority element, return immediately
        if frequency_map[element] > majority_threshold:
            return element
