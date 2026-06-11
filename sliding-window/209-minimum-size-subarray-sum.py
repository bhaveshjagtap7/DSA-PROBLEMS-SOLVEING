"""
LeetCode 209 - Minimum Size Subarray Sum

Problem Statement:
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Constraints:
- 1 <= target <= 10^9
- 1 <= nums[i] <= 10^4
- 1 <= nums.length <= 10^5

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""

def minSubArrayLenBruteForce(target: int, nums: list[int]) -> int:
    """
    Brute Force Approach:
    Iterate through all possible subarrays, calculate their sums, and check if they are >= target.
    Since we want the minimal length, we track the minimum length found.
    """
    n = len(nums)
    min_len = float('inf')
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum >= target:
                min_len = min(min_len, j - i + 1)
                break
                
    return 0 if min_len == float('inf') else min_len

