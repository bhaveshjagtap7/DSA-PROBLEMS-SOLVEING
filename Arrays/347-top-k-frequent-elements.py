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



# ============================================================================
# APPROACH 1: BRUTE FORCE
# ============================================================================
"""
Strategy: Count frequency of each element, then sort by frequency.
- Build frequency dictionary
- Convert to list of (element, frequency) pairs
- Sort by frequency (descending)
- Take first k elements

Time Complexity: O(n log n) - Sorting dominates
Space Complexity: O(n) - Store frequency dictionary and list
"""

def topKFrequent_bruteforce(nums, k):
    """
    Brute force approach using frequency counting and sorting.
    
    Args:
        nums: List of integers
        k: Number of most frequent elements to return
    
    Returns:
        List of k most frequent elements
    """
    # Count frequency of each element
    frequency_map = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1
    
    # Convert to list of (element, frequency) pairs
    frequency_pairs = list(frequency_map.items())
    
    # Sort by frequency in descending order
    # Key: frequency (second element of tuple)
    # Reverse: True for descending order
    frequency_pairs.sort(key=lambda x: x[1], reverse=True)
    
    # Extract first k elements
    result = []
    for i in range(k):
        result.append(frequency_pairs[i][0])
    
    return result



# ============================================================================
# FREQUENCY MAP EXPLANATION
# ============================================================================
"""
FREQUENCY COUNTING STRATEGY:

Step 1: Count Occurrences
- Use hash map (dictionary) to count frequency of each element
- Key: element value
- Value: count of occurrences

Example: nums = [1, 1, 2, 1, 2, 3]
  frequency_map = {
      1: 3,
      2: 2,
      3: 1
  }

Step 2: Why Frequency Map is Efficient
- Counting frequency: O(n) time (single pass through array)
- Hash map operations: O(1) average case for insert/lookup
- Memory: O(u) where u = number of unique elements

PROBLEM TRANSFORMATION:
After counting frequencies, the problem becomes:
"Find k elements with highest values in frequency map"

This can be approached in multiple ways:
1. Sorting (O(u log u)) - Simple but not optimal for large u
2. Max-Heap (O(u log k)) - Better when k << u
3. Bucket Sort (O(n)) - Optimal when frequencies are bounded

HEAP-BASED OPTIMIZATION:
- Instead of sorting all u elements (O(u log u))
- Use min-heap of size k to track top k elements
- Insert elements into heap: O(u log k)
- Extract top k: O(k log k)
- Total: O(u log k) which is better than O(u log u) when k << u

BUCKET SORT APPROACH:
- Create array of buckets where index = frequency
- Bucket[i] contains elements with frequency i
- Since max frequency ≤ n, create array of size n+1
- Traverse buckets from highest to lowest frequency
- Collect k elements
- Time: O(n), Space: O(n)

KEY INSIGHTS:
- Problem asks for "better than O(n log n)"
- Frequency counting is O(n), not the bottleneck
- Need to optimize the "find top k" step
- Heap approach meets follow-up requirement
"""
