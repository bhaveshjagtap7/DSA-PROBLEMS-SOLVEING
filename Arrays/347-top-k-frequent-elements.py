"""
LeetCode 347: Top K Frequent Elements

Problem Statement:
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.

Follow-up: Your algorithm's time complexity must be better than O(n log n), 
where n is the array's length.

Difficulty: Medium
Topics: Array, Hash Table, Divide and Conquer, Sorting, Heap, Bucket Sort, Counting
"""


# ============================================================================
# EXAMPLES
# ============================================================================
"""
Example 1:
Input: nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]
Explanation:
  Frequency: 1 appears 3 times, 2 appears 2 times, 3 appears 1 time
  Top 2 frequent elements: [1, 2] (3 and 2 occurrences)

Example 2:
Input: nums = [1], k = 1
Output: [1]
Explanation:
  Only one element, so top 1 frequent element is [1]

Example 3:
Input: nums = [1, 1, 2, 2, 2, 3, 3, 3, 3], k = 2
Output: [3, 2]
Explanation:
  Frequency: 3 appears 4 times, 2 appears 3 times, 1 appears 2 times
  Top 2: [3, 2]

Example 4:
Input: nums = [4, 1, -1, 2, -1, 2, 3], k = 2
Output: [-1, 2]
Explanation:
  Frequency: -1 appears 2 times, 2 appears 2 times (tie resolved arbitrarily)
  Other elements appear once

Example 5:
Input: nums = [5, 5, 5, 5, 3, 3, 3, 2, 2, 1], k = 3
Output: [5, 3, 2]
Explanation:
  Frequency: 5 appears 4 times, 3 appears 3 times, 2 appears 2 times
  Top 3: [5, 3, 2]
"""
