"""
LeetCode 643 - Maximum Average Subarray I

Problem Statement:
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value
and return this value. Any answer with a calculation error less than 10^-5 will be accepted.

Example Input/Output:

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

Example 3:
Input: nums = [0,0,0,0,0], k = 2
Output: 0.00000

Constraints:
- n == nums.length
- 1 <= k <= n <= 10^5
- -10^4 <= nums[i] <= 10^4

Brute Force Approach:
The brute force approach considers every possible subarray of length k and calculates
the average for each. We iterate through all starting positions from 0 to n-k,
compute the sum of k elements starting at each position, and track the maximum sum.

Time Complexity: O(n*k) - For each of (n-k+1) positions, we sum k elements
Space Complexity: O(1) - Only using a few variables
"""

def findMaxAverage_brute_force(nums, k):
    """
    Brute force solution to find maximum average subarray of length k.
    
    Args:
        nums: List of integers
        k: Length of subarray
    
    Returns:
        Maximum average value as float
    """
    n = len(nums)
    max_sum = float('-inf')
    
    for i in range(n - k + 1):
        current_sum = 0
        for j in range(i, i + k):
            current_sum += nums[j]
        max_sum = max(max_sum, current_sum)
    
    return max_sum / k
