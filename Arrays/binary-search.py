"""
LeetCode 704: Binary Search

Problem Statement:
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, return its index. Otherwise, 
return -1.

You must write an algorithm with O(log n) time complexity.

Example:
- Input: nums = [-1,0,3,5,9,12], target = 9
- Output: 4
- Explanation: 9 is at index 4

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
# EDGE CASES TO CONSIDER
# ============================================================================
"""
1. Single element array (target found)
2. Single element array (target not found)
3. Target at first index
4. Target at last index
5. Target in middle
6. Target not in array (too small)
7. Target not in array (too large)
8. Target not in array (in between values)
9. Two element array
10. All negative numbers
11. All positive numbers
12. Mix of negative and positive
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


# ============================================================================
# COMPLEXITY ANALYSIS
# ============================================================================
'''
TIME COMPLEXITY COMPARISON:

Approach              Best    Average   Worst     Notes
                    ─────────────────────────────────────
Linear Search        O(1)    O(n/2)    O(n)      Simple, slow
Binary Search        O(1)    O(log n)  O(log n)  Fast, sorted only

SPACE COMPLEXITY:
- Brute Force:    O(1) - Only variable storage
- Binary Search:  O(1) - Only two pointers

WHY BINARY SEARCH IS SUPERIOR:
- For array of 1,000,000 elements:
  - Linear Search:  ~500,000 iterations in average case
  - Binary Search:  ~20 iterations (log2(1,000,000) ~= 20)
  - Binary is 25,000x FASTER!

- For array of 1 billion elements:
  - Linear Search:  ~500 million iterations
  - Binary Search:  ~30 iterations
  - Binary is 16.7 million x FASTER!

RECOMMENDATION:
Always use Binary Search for sorted arrays to achieve O(log n) efficiency.
'''



# ============================================================================
# DRY RUN EXAMPLES
# ============================================================================
"""
DRY RUN 1: Binary Search for target = 7 in [1, 3, 5, 7, 9, 11, 13]

Array: [1, 3, 5, 7, 9, 11, 13]
        0  1  2  3  4   5   6  (indices)
Target: 7

Iteration 1:
  left = 0, right = 6
  mid = (0 + 6) // 2 = 3
  nums[3] = 7
  7 == 7? YES! Return 3 ✓

---

DRY RUN 2: Binary Search for target = 11 in [1, 3, 5, 7, 9, 11, 13]

Array: [1, 3, 5, 7, 9, 11, 13]
        0  1  2  3  4   5   6
Target: 11

Iteration 1:
  left = 0, right = 6
  mid = (0 + 6) // 2 = 3
  nums[3] = 7
  7 < 11? YES → Search right half
  left = mid + 1 = 4

Iteration 2:
  left = 4, right = 6
  mid = (4 + 6) // 2 = 5
  nums[5] = 11
  11 == 11? YES! Return 5 ✓

---

DRY RUN 3: Binary Search for target = 2 in [1, 3, 5, 7, 9]

Array: [1, 3, 5, 7, 9]
        0  1  2  3  4
Target: 2 (NOT in array)

Iteration 1:
  left = 0, right = 4
  mid = (0 + 4) // 2 = 2
  nums[2] = 5
  5 > 2? YES → Search left half
  right = mid - 1 = 1

Iteration 2:
  left = 0, right = 1
  mid = (0 + 1) // 2 = 0
  nums[0] = 1
  1 < 2? YES → Search right half
  left = mid + 1 = 1

Iteration 3:
  left = 1, right = 1
  mid = (1 + 1) // 2 = 1
  nums[1] = 3
  3 > 2? YES → Search left half
  right = mid - 1 = 0

Iteration 4:
  left = 1, right = 0
  left > right? YES → Exit loop
  Return -1 (not found) ✓

---

DRY RUN 4: Binary Search for target = 1 in [1, 3, 5, 7, 9]

Array: [1, 3, 5, 7, 9]
        0  1  2  3  4
Target: 1 (first element)

Iteration 1:
  left = 0, right = 4
  mid = (0 + 4) // 2 = 2
  nums[2] = 5
  5 > 1? YES → Search left half
  right = mid - 1 = 1

Iteration 2:
  left = 0, right = 1
  mid = (0 + 1) // 2 = 0
  nums[0] = 1
  1 == 1? YES! Return 0 ✓
"""


# ============================================================================
# TEST CASES AND EXAMPLES
# ============================================================================
if __name__ == "__main__":
    test_cases = [
        # (nums, target, expected, description)
        ([-1, 0, 3, 5, 9, 12], 9, 4, "Target in right half"),
        ([5], 5, 0, "Single element match"),
        ([5], -5, -1, "Single element no match"),
        ([-1, 0, 3, 5, 9, 12], 2, -1, "Target not found"),
        ([1, 3, 5, 7, 9], 9, 4, "Target at end"),
        ([1, 3, 5, 7, 9], 1, 0, "Target at start"),
        ([1, 3, 5, 7, 9], 5, 2, "Target in middle"),
        ([1, 3, 5, 7, 9], 2, -1, "Target between values"),
        ([2, 5], 5, 1, "Two elements - found"),
        ([2, 5], 3, -1, "Two elements - not found"),
        ([-10, -5, 0, 5, 10], -10, 0, "Negative at start"),
        ([-10, -5, 0, 5, 10], 10, 4, "Positive at end"),
        ([-10, -5, 0, 5, 10], 0, 2, "Zero in middle"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 0, "Large array - first"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 9, "Large array - last"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 4, "Large array - middle"),
    ]
    
    solution = Solution()
    
    print("=" * 70)
    print("LeetCode 704: Binary Search - Comprehensive Test Results")
    print("=" * 70)
    
    passed = 0
    failed = 0
    
    for i, (nums, target, expected, desc) in enumerate(test_cases, 1):
        result = solution.search(nums, target)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        
        if result == expected:
            passed += 1
        else:
            failed += 1
        
        print(f"\nTest {i}: {status}")
        print(f"  Desc:     {desc}")
        print(f"  Array:    {nums}")
        print(f"  Target:   {target}")
        print(f"  Expected: {expected}, Got: {result}")
    
    print("\n" + "=" * 70)
    print(f"SUMMARY: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("Binary Search Approach: Time O(log n) | Space O(1)")
    print("=" * 70)
