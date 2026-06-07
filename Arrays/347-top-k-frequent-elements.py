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



# ============================================================================
# FREQUENCY COUNTING IMPLEMENTATION
# ============================================================================
"""
Efficient frequency counting implementation.

Key optimizations:
1. Use dictionary.get() for concise counting
2. Handle both positive and negative numbers
3. Memory efficient: O(u) where u = unique elements
"""

def build_frequency_map(nums):
    """
    Count frequency of each element in array.
    
    Args:
        nums: List of integers
    
    Returns:
        Dictionary mapping element -> frequency count
    
    Time Complexity: O(n)
    Space Complexity: O(u) where u = number of unique elements
    """
    frequency_dict = {}
    
    for element in nums:
        # Increment count for current element
        # Using get() with default value 0
        frequency_dict[element] = frequency_dict.get(element, 0) + 1
    
    return frequency_dict


def get_frequency_pairs(nums):
    """
    Create list of (element, frequency) pairs from array.
    
    Args:
        nums: List of integers
    
    Returns:
        List of tuples (element, frequency)
    
    Useful for sorting or heap operations.
    """
    frequency_map = build_frequency_map(nums)
    return list(frequency_map.items())



# ============================================================================
# APPROACH 2: HEAP-BASED OPTIMIZATION
# ============================================================================
"""
Strategy: Use min-heap of size k to track top k frequent elements.

Min-Heap Property: Smallest element at root
We want top k LARGEST frequencies, so we keep smallest in heap to replace.

Algorithm:
1. Build frequency dictionary: O(n)
2. For each (element, frequency) pair:
   - Push (frequency, element) into heap
   - If heap size > k, pop smallest (root)
3. Extract elements from heap: O(k log k)
4. Return elements

Heap operations:
- Push: O(log k)
- Pop: O(log k)
- Total for u unique elements: O(u log k)

Time Complexity: O(n + u log k) ≈ O(n log k) worst case
Space Complexity: O(n + k) ≈ O(n)
"""

import heapq

def topKFrequent_heap(nums, k):
    """
    Heap-based solution for top k frequent elements.
    
    Args:
        nums: List of integers
        k: Number of most frequent elements to return
    
    Returns:
        List of k most frequent elements
    
    Time Complexity: O(n + u log k) where u = unique elements
    Space Complexity: O(n + k)
    """
    # Step 1: Count frequencies
    frequency_map = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1
    
    # Step 2: Use min-heap of size k
    # Heap stores tuples: (frequency, element)
    # Min-heap keeps smallest frequency at root
    heap = []
    
    for element, frequency in frequency_map.items():
        # Push (frequency, element) into heap
        heapq.heappush(heap, (frequency, element))
        
        # If heap exceeds size k, remove element with smallest frequency
        if len(heap) > k:
            heapq.heappop(heap)
    
    # Step 3: Extract elements from heap
    # Elements in heap are (frequency, element), need just element
    result = []
    while heap:
        frequency, element = heapq.heappop(heap)
        result.append(element)
    
    # Heap stores smallest k frequencies, but we want largest
    # So result is in increasing frequency order, reverse it
    return result[::-1]



# ============================================================================
# FINAL OPTIMIZED SOLUTION: BUCKET SORT APPROACH
# ============================================================================
"""
Optimal Solution: Bucket Sort (Count Sort for frequencies)

Key Insight:
Maximum frequency of any element ≤ n (array length)
We can create array of size n+1 where index = frequency

Algorithm:
1. Count frequency of each element: O(n)
2. Create bucket array of size n+1
   - bucket[i] = list of elements with frequency i
3. Traverse buckets from highest to lowest frequency
4. Collect k elements

Time Complexity: O(n) - Beats O(n log n) requirement
Space Complexity: O(n) - Bucket array and frequency map

Why it's optimal:
- Frequency counting: O(n)
- Bucket creation: O(n)
- Bucket traversal: O(n)
- Total: O(n) ✓
"""

def topKFrequent_bucket(nums, k):
    """
    Bucket sort solution - optimal O(n) time complexity.
    
    Args:
        nums: List of integers
        k: Number of most frequent elements to return
    
    Returns:
        List of k most frequent elements
    
    Complexity:
        Time: O(n) - Linear time
        Space: O(n) - Bucket array and frequency map
    """
    array_length = len(nums)
    
    # Step 1: Count frequencies
    frequency_map = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1
    
    # Step 2: Create bucket array
    # Index = frequency, Value = list of elements with that frequency
    # Size n+1 because frequency can be from 1 to n
    bucket_array = [[] for _ in range(array_length + 1)]
    
    for element, frequency in frequency_map.items():
        bucket_array[frequency].append(element)
    
    # Step 3: Collect top k frequent elements
    result = []
    
    # Traverse from highest frequency (n) to lowest (1)
    for frequency in range(array_length, 0, -1):
        # Get elements with current frequency
        elements_at_frequency = bucket_array[frequency]
        
        # Add elements to result
        for element in elements_at_frequency:
            result.append(element)
            
            # Stop when we have k elements
            if len(result) == k:
                return result
    
    return result


class Solution(object):
    """LeetCode 347: Top K Frequent Elements"""
    
    def topKFrequent(self, nums, k):
        """
        Return k most frequent elements using bucket sort approach.
        
        Args:
            nums: List of integers
            k: Number of most frequent elements to return
        
        Returns:
            List of k most frequent elements (any order)
        
        Complexity:
            Time: O(n) - Linear time, meets follow-up requirement
            Space: O(n) - Frequency map and bucket array
        """
        return topKFrequent_bucket(nums, k)



# ============================================================================
# COMPLEXITY ANALYSIS
# ============================================================================
"""
APPROACH COMPARISON:

Approach              Time         Space        Notes
────────────────────────────────────────────────────────────────────
Brute Force           O(n log n)   O(n)         Sorting dominates
Heap-Based            O(n log k)   O(n + k)     Better when k << n
Bucket Sort           O(n)         O(n)         Optimal! ✓

WHY BUCKET SORT IS OPTIMAL:
- Follow-up requires better than O(n log n)
- Bucket sort achieves O(n) linear time
- Uses counting/bucket sort concept for frequencies
- Maximum frequency ≤ n, so bucket array of size n+1 works
- Linear in both time and space

TIME COMPLEXITY BREAKDOWN:

Brute Force (Sorting):
  Frequency counting: O(n)
  Sort u elements:    O(u log u) where u = unique elements
  Extract k:          O(k)
  Total:              O(n + u log u) ≈ O(n log n) worst case

Heap-Based:
  Frequency counting: O(n)
  Heap operations:    O(u log k) where u = unique elements
  Extract k:          O(k log k)
  Total:              O(n + u log k) ≈ O(n log k)

Bucket Sort:
  Frequency counting: O(n)
  Bucket creation:    O(u) ≈ O(n)
  Bucket traversal:   O(n) (worst case visit each bucket)
  Total:              O(n) ✓

SPACE COMPLEXITY BREAKDOWN:

Brute Force: O(n) - Frequency dictionary + sorted list
Heap-Based:  O(n + k) - Frequency dict + heap of size k
Bucket Sort: O(n) - Frequency dict + bucket array of size n+1

WHY BUCKET SIZE n+1?
- Frequency ranges from 1 to n (array length)
- Need index n for elements appearing n times
- Plus index 0 for consistency (though unused)
- Example: n = 5 → buckets[0..5] (6 buckets)

FOLLOW-UP REQUIREMENT:
Problem asks for "better than O(n log n)"
- Bucket Sort: O(n) ✓ (beats requirement)
- Heap-Based: O(n log k) ✓ (better when k small)
- Brute Force: O(n log n) ✗ (doesn't beat requirement)

RECOMMENDATION: Use Bucket Sort for optimal O(n) solution!
"""



# ============================================================================
# EDGE CASES AND TEST CASES
# ============================================================================
"""
Edge Cases to Consider:

1. Single element array
   - [5], k = 1 → [5]
   - Always returns the only element

2. All elements same
   - [1, 1, 1, 1], k = 1 → [1]
   - Only one unique element

3. All elements distinct
   - [1, 2, 3, 4], k = 2 → any 2 elements (order doesn't matter)
   - Each frequency = 1, tie resolved arbitrarily

4. Negative numbers
   - [-1, -2, -1, -3], k = 2 → [-1, -2] or [-1, -3]
   - Handles negative values correctly

5. k = number of unique elements
   - Returns all elements (any order)
   - Example: [1, 2, 2, 3], k = 2 → [2, 1] or [2, 3]

6. k = 1
   - Returns single most frequent element
   - If ties, any of the most frequent elements

7. Large array with small k
   - [1...100000], k = 5 → Fast with heap/bucket approaches
   - Tests scalability

8. Frequency ties
   - [1, 1, 2, 2, 3], k = 2 → [1, 2] (both frequency 2)
   - Any tie-breaking order acceptable

9. Empty array
   - Not possible per constraints (1 ≤ nums.length)

10. k larger than unique elements
    - Not possible per constraints (1 ≤ k ≤ unique elements)
"""


if __name__ == "__main__":
    test_cases = [
        # (nums, k, expected_sets, description)
        ([1, 1, 1, 2, 2, 3], 2, [{1, 2}], "Basic example"),
        ([1], 1, [{1}], "Single element"),
        ([1, 1, 2, 2, 2, 3, 3, 3, 3], 2, [{3, 2}], "Clear top 2"),
        ([4, 1, -1, 2, -1, 2, 3], 2, [{-1, 2}], "With negatives"),
        ([5, 5, 5, 5, 3, 3, 3, 2, 2, 1], 3, [{5, 3, 2}], "Top 3 elements"),
        ([1, 2, 3, 4], 2, [any 2 of {1, 2, 3, 4}], "All distinct"),
        ([1, 1, 1, 1], 1, [{1}], "All elements same"),
        ([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 1, [{4}], "Single most frequent"),
        ([-1, -1, -2, -3], 2, [{-1, -2}, {-1, -3}], "Negative frequencies"),
        ([1, 1, 2, 2, 3, 3, 4, 4], 3, [any 3 of {1, 2, 3, 4}], "All ties"),
    ]
    
    print("=" * 80)
    print("LeetCode 347: Top K Frequent Elements - Test Results")
    print("=" * 80)
    
    passed = 0
    failed = 0
    
    for i, (nums, k, expected_sets, description) in enumerate(test_cases, 1):
        # Test optimized solution
        result = topKFrequent_bucket(nums[:])
        
        # Check if result matches any expected set
        result_set = set(result)
        is_correct = any(result_set == expected for expected in expected_sets)
        
        status = "✓ PASS" if is_correct else "✗ FAIL"
        if is_correct:
            passed += 1
        else:
            failed += 1
        
        print(f"\nTest {i}: {status}")
        print(f"  Description: {description}")
        print(f"  Input:       nums={nums}, k={k}")
        print(f"  Expected:    Any of {expected_sets}")
        print(f"  Got:         {result}")
    
    print("\n" + "=" * 80)
    print(f"SUMMARY: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("Optimal Solution: Bucket Sort - Time O(n) | Space O(n)")
    print("=" * 80)
