"""
LeetCode 704: Binary Search

Problem Statement:
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, return its index. Otherwise, 
return -1.

You must write an algorithm with O(log n) time complexity.

Example:
- Input: nums = [-1,0,3,1,4,5,2,6], target = 0
- Output: 1
- Explanation: 0 is at index 1

- Input: nums = [5], target = 5
- Output: 0

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All integers in nums are unique.
- nums is sorted in ascending order.

Problem Type: Array, Binary Search
Topic: Divide and Conquer
Difficulty: Easy
"""


# ============================================================================
# APPROACH 1: BRUTE FORCE - LINEAR SEARCH
# ============================================================================
def search_bruteforce(nums, target):
    """
    Brute Force Approach: Linear Search
    
    Strategy: Simply iterate through the array and check each element.
    
    Time Complexity: O(n) - We might need to check every element
    Space Complexity: O(1) - No extra space used
    
    Why it's suboptimal:
    - For a sorted array, we're not leveraging the sorted property
    - In worst case, we scan entire array (when target is at end or missing)
    - Not suitable for large datasets
    
    Args:
        nums: Sorted list of integers
        target: Integer to search for
    
    Returns:
        Index of target if found, -1 otherwise
    """
    # Iterate through each element
    for i in range(len(nums)):
        # Found target
        if nums[i] == target:
            return i
    
    # Target not found
    return -1



# ============================================================================
# APPROACH 2: OPTIMIZED - BINARY SEARCH (RECOMMENDED)
# ============================================================================
def search_binary(nums, target):
    """
    Optimized Binary Search Approach
    
    Strategy: Divide and conquer using two pointers.
    - Start with left at beginning, right at end
    - Calculate middle point
    - Compare mid element with target
    - If equal, return index
    - If mid < target, search right half (move left pointer)
    - If mid > target, search left half (move right pointer)
    - Continue until found or search space exhausted
    
    Why it's optimal:
    - Each iteration eliminates half of remaining elements
    - Dramatically faster for large datasets
    - Must work on SORTED arrays
    
    Time Complexity: O(log n) - Each step halves search space
    Space Complexity: O(1) - Only using two pointer variables
    
    Args:
        nums: Sorted list of integers
        target: Integer to search for
    
    Returns:
        Index of target if found, -1 otherwise
    """
    # Initialize two pointers
    left = 0
    right = len(nums) - 1
    
    # Continue while search space is valid
    while left <= right:
        # Calculate middle index
        mid = (left + right) // 2
        
        # Found target
        if nums[mid] == target:
            return mid
        
        # Target is in right half
        elif nums[mid] < target:
            left = mid + 1
        
        # Target is in left half
        else:
            right = mid - 1
    
    # Target not found
    return -1


class Solution(object):
    """LeetCode 704 Binary Search Solution"""
    
    def search(self, nums, target):
        """Search for target in sorted array."""
        return search_binary(nums, target)
