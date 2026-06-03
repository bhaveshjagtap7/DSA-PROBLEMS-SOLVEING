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
