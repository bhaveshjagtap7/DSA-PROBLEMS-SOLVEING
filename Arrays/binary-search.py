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
    array_length = len(nums)
    
    # Check each element one by one
    for current_index in range(array_length):
        # Check if current element matches target
        if nums[current_index] == target:
            return current_index
    
    # Target not found in entire array
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
    
    Interview Notes:
    ----------------
    KEY INSIGHT: Sorted array → Think Binary Search!
                 Each comparison eliminates half the search space.
    
    CRITICAL REQUIREMENTS:
    1. Array MUST be sorted (ascending or descending)
    2. Must achieve O(log n) time complexity
    
    APPROACH PROGRESSION (What to say in interview):
    1. Brute Force: Linear search → O(n)
    2. Binary Search: Divide and conquer → O(log n) ✓
    
    COMMON MISTAKES TO AVOID:
    ✗ mid = (left + right) / 2  ← Can overflow in some languages!
    ✓ mid = left + (right - left) // 2  ← Safer
    ✓ mid = (left + right) // 2  ← OK in Python (no int overflow)
    
    ✗ while left < right:  ← Might miss elements
    ✓ while left <= right:  ← Correct condition
    
    ✗ Forgetting to update left/right pointers
    ✓ left = mid + 1 and right = mid - 1
    
    FOLLOW-UP QUESTIONS:
    Q: What if array has duplicates?
       A: Return any valid index, or modify to find first/last occurrence
    
    Q: What if we want to find insertion position?
       A: Return left pointer when not found (see Insert Position problem)
    
    Q: Recursive vs Iterative?
       A: Iterative is better (no recursion stack space)
    
    Q: What about rotated sorted array?
       A: Modified binary search (different problem)
    """
    # Initialize left and right pointers for search space
    left_pointer = 0
    right_pointer = len(nums) - 1
    
    # Continue searching while there are elements to check
    while left_pointer <= right_pointer:
        # Calculate middle index (safe from overflow in Python)
        middle_index = (left_pointer + right_pointer) // 2
        middle_value = nums[middle_index]
        
        # Check if we found the target
        if middle_value == target:
            return middle_index  # Found target at middle
        
        # Target must be in right half (larger values)
        elif middle_value < target:
            left_pointer = middle_index + 1  # Eliminate left half
        
        # Target must be in left half (smaller values)
        else:
            right_pointer = middle_index - 1  # Eliminate right half
    
    # Search space exhausted, target not in array
    return -1


# ============================================================================
# INTERVIEW KEY OBSERVATIONS
# ============================================================================
"""
🎯 KEY OBSERVATIONS FOR INTERVIEWS:

1. WHY BINARY SEARCH IS POWERFUL
   For n = 1,000,000 elements:
   - Linear Search: ~500,000 comparisons (average)
   - Binary Search: ~20 comparisons (log₂(1,000,000))
   - That's 25,000x FASTER!

2. THE LOGARITHMIC MAGIC
   Each iteration cuts problem size in HALF:
   n → n/2 → n/4 → n/8 → ... → 1
   
   Number of steps = log₂(n)
   
   Examples:
   - 10 elements → 4 steps
   - 100 elements → 7 steps
   - 1,000 elements → 10 steps
   - 1,000,000 elements → 20 steps
   - 1,000,000,000 elements → 30 steps (!!)

3. SEARCH SPACE VISUALIZATION
   [1, 3, 5, 7, 9, 11, 13]  target = 11
    L           M        R   
   
   Step 1: mid=7, 7<11 → search right
           [9, 11, 13]
            L   M   R
   
   Step 2: mid=11, 11==11 → FOUND!

4. PREREQUISITE: WHY SORTED?
   - Sorted array has ORDER property
   - If nums[mid] < target, ALL elements left of mid are < target
   - If nums[mid] > target, ALL elements right of mid are > target
   - This guarantees we can eliminate half safely
   
   Unsorted → Can't make this guarantee → Must check all O(n)

5. LOOP INVARIANT
   Property that's always true:
   "If target exists, it's in range [left, right]"
   
   - Initially: [0, n-1] contains all elements ✓
   - After each step: range shrinks but property holds ✓
   - Exit: left > right means target not in any range

6. BOUNDARY CONDITIONS
   Critical to get right:
   - while left <= right (not just <)
   - left = mid + 1 (not mid)
   - right = mid - 1 (not mid)
   
   Getting these wrong → infinite loops or missed elements!

7. INTEGER OVERFLOW (Language Dependent)
   In Java/C++:
   ✗ mid = (left + right) / 2  ← Can overflow if left+right > INT_MAX
   ✓ mid = left + (right - left) / 2  ← Safe
   
   In Python:
   ✓ mid = (left + right) // 2  ← Safe (no int overflow in Python)

8. RECURSIVE VS ITERATIVE
   Iterative (shown above):
   - Space: O(1)
   - Faster (no function call overhead)
   - Preferred in interviews ✓
   
   Recursive:
   - Space: O(log n) call stack
   - More elegant but less efficient
   - OK to mention but implement iterative

9. WHAT INTERVIEWERS WANT TO HEAR
   ✓ "Array is sorted, so binary search is appropriate"
   ✓ "This achieves O(log n) time complexity"
   ✓ "I'll use two pointers to track search space"
   ✓ "Each iteration eliminates half the elements"
   ✓ "Critical to handle boundary conditions correctly"

10. RELATED PROBLEMS & PATTERNS
    - Search Insert Position (LeetCode 35)
    - First Bad Version (LeetCode 278)
    - Search in Rotated Sorted Array (LeetCode 33)
    - Find Minimum in Rotated Sorted Array (LeetCode 153)
    - Search a 2D Matrix (LeetCode 74)
    
    Pattern: "Sorted" or "monotonic" → Consider Binary Search!
"""


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
