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

"""
Sliding Window Explanation:
The sliding window technique is an optimization for problems involving subarrays of fixed length.
Instead of recalculating the sum from scratch for each position, we maintain a "window" of k elements.

Key insight: When we slide the window by one position:
- We remove the element that's leaving the window (leftmost element)
- We add the element that's entering the window (new rightmost element)
- The new sum = old sum - outgoing_element + incoming_element

This reduces the time complexity from O(n*k) to O(n) because each element is added
and subtracted from the sum exactly once.

Example with nums = [1,12,-5,-6,50,3], k = 4:
- Window 1: [1,12,-5,-6] -> sum = 2
- Slide: remove 1, add 50 -> new sum = 2 - 1 + 50 = 51
- Window 2: [12,-5,-6,50] -> sum = 51
- Slide: remove 12, add 3 -> new sum = 51 - 12 + 3 = 42
- Window 3: [-5,-6,50,3] -> sum = 42
- Maximum sum = 51, average = 51/4 = 12.75
"""

def findMaxAverage_sliding_window(nums, k):
    """
    Optimized sliding window solution to find maximum average subarray of length k.
    
    Args:
        nums: List of integers
        k: Length of subarray
    
    Returns:
        Maximum average value as float
    """
    # Initialize the sum of the first window
    current_sum = sum(nums[:k])
    max_sum = current_sum
    
    # Slide the window across the array
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum / k

"""
Complexity Analysis for Optimized Sliding Window:

Time Complexity: O(n)
- We compute the sum of the first k elements once, which takes O(k) time.
- Then, we iterate from index k to n-1. In each step of the loop, we perform a constant number of operations: one addition, one subtraction, one comparison, and one assignment. This takes O(1) time per step.
- The loop runs (n - k) times.
- Therefore, the total time complexity is O(k) + O(n - k) = O(n), where n is the number of elements in the array.

Space Complexity: O(1)
- We only use a few variables (current_sum, max_sum, i) to track the window sum and the maximum sum.
- No extra space that scales with the input size is allocated.
"""

# ============================================================================
# EDGE CASES TO CONSIDER
# ============================================================================
"""
1. k = 1 (Minimum allowed window size):
   - In this case, the maximum average subarray is just the maximum element of the array.
   - Example: nums = [1, 12, -5], k = 1 -> Output: 12.0
2. k = n (Window size equals array length):
   - The only subarray of length k is the entire array.
   - Example: nums = [1, 12, -5], k = 3 -> Output: 2.66667
3. All negative numbers:
   - Make sure we initialize max_sum correctly (cannot initialize to 0; must initialize to the first window's sum).
   - Example: nums = [-1, -2, -3], k = 2 -> Output: -1.5 (subarray [-1, -2])
4. All identical elements:
   - Example: nums = [5, 5, 5, 5], k = 2 -> Output: 5.0
5. Alternating signs:
   - Example: nums = [1, -1, 1, -1], k = 2 -> Output: 0.0
"""

# ============================================================================
# DRY RUN
# ============================================================================
"""
DRY RUN: Sliding Window Approach
Input: nums = [1, 12, -5, -6, 50, 3], k = 4

1. Initial Window (first k elements):
   - Window: nums[0:4] = [1, 12, -5, -6]
   - current_sum = 1 + 12 + (-5) + (-6) = 2
   - max_sum = 2

2. Iteration (i goes from k to len(nums) - 1, i.e., 4 to 5):
   - i = 4:
     - Element entering: nums[4] = 50
     - Element leaving: nums[4 - 4] = nums[0] = 1
     - current_sum = 2 + 50 - 1 = 51
     - Is current_sum (51) > max_sum (2)? Yes -> max_sum = 51
     
   - i = 5:
     - Element entering: nums[5] = 3
     - Element leaving: nums[5 - 4] = nums[1] = 12
     - current_sum = 51 + 3 - 12 = 42
     - Is current_sum (42) > max_sum (51)? No -> max_sum remains 51

3. Return result:
   - max_sum / k = 51 / 4 = 12.75
"""

# ============================================================================
# TEST CASES
# ============================================================================

if __name__ == "__main__":
    test_cases = [
        # (nums, k, expected, description)
        ([1, 12, -5, -6, 50, 3], 4, 12.75, "Standard test case with positive and negative numbers"),
        ([5], 1, 5.0, "Single element array with k=1"),
        ([0, 4, 0, 3, 2], 1, 4.0, "Array with zeros and k=1"),
        ([-1], 1, -1.0, "Single negative element"),
        ([-1, -12, -5, -6, -50, -3], 4, -6.0, "All negative numbers"),
        ([1, 2, 3, 4, 5], 5, 3.0, "k equals length of array"),
        ([5, 5, 5, 5], 2, 5.0, "All elements identical"),
        ([0, 0, 0, 0], 2, 0.0, "All zeros"),
    ]
    
    print("=" * 70)
    print("LeetCode 643: Maximum Average Subarray I - Tests")
    print("=" * 70)
    
    for i, (nums, k, expected, desc) in enumerate(test_cases, 1):
        result_bf = findMaxAverage_brute_force(nums, k)
        result_sw = findMaxAverage_sliding_window(nums, k)
        
        # Check correctness (accept calculation error < 10^-5)
        bf_pass = abs(result_bf - expected) < 1e-5
        sw_pass = abs(result_sw - expected) < 1e-5
        
        status = "PASS" if (bf_pass and sw_pass) else "FAIL"
        print(f"\nTest {i}: {status}")
        print(f"  Desc:      {desc}")
        print(f"  Input:     nums={nums}, k={k}")
        print(f"  Expected:  {expected}")
        print(f"  Results:   Brute Force = {result_bf} | Sliding Window = {result_sw}")
    
    print("\n" + "=" * 70)
