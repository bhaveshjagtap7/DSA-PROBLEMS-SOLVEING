"""
LeetCode 217: Contains Duplicate

Problem: Given an integer array nums, return true if any value appears at least twice 
in the array, and return false if every element is distinct.

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Time Complexity Analysis:
- Brute Force: O(n²)
- Hash Set: O(n)

Space Complexity Analysis:
- Brute Force: O(1)
- Hash Set: O(n)
"""


# ============================================================================
# EDGE CASES TO CONSIDER
# ============================================================================
"""
1. Empty array → Return False
2. Single element → Return False (no duplicate possible)
3. Two identical elements → Return True
4. All elements same → Return True
5. No duplicates → Return False
6. Duplicate at start and end → Return True
7. Adjacent duplicates → Return True
8. Negative numbers → Handle correctly
9. Zeros → Handle correctly
10. Large numbers → Within constraints
11. Multiple duplicates → Return True (early)
"""

# ============================================================================
# APPROACH 1: BRUTE FORCE (Nested Loop)
# ============================================================================
"""
Strategy: Compare every element with every other element.
- For each element at index i, check if it exists in the remaining array.
- If found, return True.
- If no duplicate found after all comparisons, return False.

Time Complexity: O(n²) - Two nested loops
Space Complexity: O(1) - No extra space used
"""

def containsDuplicate_bruteforce(nums):
    """
    Brute force approach using nested loops.
    
    Args:
        nums: List of integers
    
    Returns:
        Boolean - True if duplicate exists, False otherwise
    """
    # Check every element against every other element
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # If we find matching elements, duplicate exists
            if nums[i] == nums[j]:
                return True
    
    # No duplicates found
    return False


# ============================================================================
# APPROACH 2: OPTIMIZED - HASH SET
# ============================================================================
"""
Strategy: Use a set to track elements we've already seen.
- Iterate through the array once.
- For each element, check if it's already in the set.
- If yes, we found a duplicate → return True.
- If no, add it to the set and continue.
- If loop completes without finding duplicate → return False.

Why HashSet is efficient:
- Set lookup/insertion is O(1) on average
- We only iterate through the array once: O(n)
- Trade space O(n) for time O(n) instead of O(n²)

Time Complexity: O(n) - Single pass through array
Space Complexity: O(n) - Hash set stores up to n elements
"""

def containsDuplicate_hashset(nums):
    """
    Optimized approach using Hash Set.
    Best solution for this problem.
    
    Args:
        nums: List of integers
    
    Returns:
        Boolean - True if duplicate exists, False otherwise
    
    Interview Notes:
    ----------------
    KEY INSIGHT: We don't need to count occurrences, just detect if seen before.
                 Set is perfect: O(1) insert and lookup.
    
    APPROACH PROGRESSION (What to say in interview):
    1. Brute Force: Compare all pairs → O(n²)
    2. Sorting: Sort then check adjacent → O(n log n)
    3. Hash Set: Track seen elements → O(n) ✓ OPTIMAL
    
    FOLLOW-UP QUESTIONS:
    Q: Can we do better than O(n) time?
       A: No, we must check every element at least once.
    
    Q: What if we can't use extra space?
       A: Sorting is O(n log n) time, O(1) space (in-place sort)
    
    Q: What about counting frequency?
       A: Use hash map instead of set, but not needed here.
    """
    seen = set()  # Create empty set to track seen elements
    
    # Iterate through each number in the array
    for num in nums:
        # If number already in set, we found a duplicate
        if num in seen:
            return True
        
        # Add number to set for future lookups
        seen.add(num)
    
    # No duplicates found
    return False


# ============================================================================
# INTERVIEW KEY OBSERVATIONS
# ============================================================================
"""
🎯 KEY OBSERVATIONS FOR INTERVIEWS:

1. PROBLEM SIMPLIFICATION
   - Don't need to find WHICH elements are duplicates
   - Don't need to COUNT duplicates
   - Just need to DETECT if any duplicate exists
   - This means SET (not map/dict) is sufficient

2. SET vs DICTIONARY
   - Set: Stores only values, checks existence
   - Dictionary: Stores key-value pairs
   - For this problem: Set is cleaner and sufficient ✓

3. EARLY EXIT OPTIMIZATION
   - Return True immediately when first duplicate found
   - No need to check remaining elements
   - Best case: O(1) if duplicate is first two elements
   - Worst case: O(n) if no duplicate (must check all)

4. COMPLEXITY COMPARISON
   Approach       Time        Space      Notes
   ───────────────────────────────────────────────────
   Brute Force    O(n²)       O(1)       Too slow ✗
   Sorting        O(n log n)  O(1)*      *Modifies array
   Hash Set       O(n)        O(n)       Optimal ✓
   Set Length     O(n)        O(n)       Python trick

5. PYTHON TRICK (One-liner)
   return len(nums) != len(set(nums))
   
   How it works:
   - set() automatically removes duplicates
   - If lengths differ, duplicates existed
   - Elegant but less explicit about algorithm
   - Good to mention after explaining main approach

6. WHY THIS IS "EASY"
   - Straightforward problem statement
   - Classic hash set pattern
   - No complex logic or edge cases
   - Common in real-world scenarios

7. REAL-WORLD APPLICATIONS
   - Validating unique usernames
   - Checking duplicate IDs
   - Data validation
   - Database constraint checks

8. WHAT INTERVIEWERS WANT TO HEAR
   ✓ "I'll use a hash set for O(1) lookups"
   ✓ "This is a time-space tradeoff"
   ✓ "We can exit early when duplicate found"
   ✓ "Set is better than dict since we don't need values"
   ✓ "There's also a Python one-liner using len comparison"

9. COMMON MISTAKES TO AVOID
   ✗ Using nested loops (O(n²))
   ✗ Sorting then comparing (O(n log n) when O(n) exists)
   ✗ Using dictionary when set is sufficient
   ✗ Forgetting negative numbers work fine
   ✗ Not considering single element edge case

10. RELATED PROBLEMS
    - Contains Duplicate II (with index distance constraint)
    - Contains Duplicate III (with value range constraint)
    - Find the Duplicate Number
    - Unique Email Addresses
"""


# ============================================================================
# APPROACH 3: EVEN MORE OPTIMIZED - Early Exit with len() comparison
# ============================================================================
"""
Alternative insight:
- If we create a set from the array and its length < original array length,
  then duplicates must exist.
- This is Python-specific and leverages set's automatic duplicate removal.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def containsDuplicate_set_comparison(nums):
    """
    One-liner approach comparing lengths.
    Elegant but less explicit about the algorithm.
    
    Args:
        nums: List of integers
    
    Returns:
        Boolean - True if duplicate exists, False otherwise
    """
    return len(nums) != len(set(nums))


# ============================================================================
# DRY RUN EXAMPLES
# ============================================================================
"""
DRY RUN 1: HashSet Approach for [1, 2, 3, 1]

Array: [1, 2, 3, 1]
Goal: Find if any duplicate exists

Initial: seen = {}

Iteration 1: num = 1
  Is 1 in seen? No
  Add 1 to seen
  seen = {1}

Iteration 2: num = 2
  Is 2 in seen? No
  Add 2 to seen
  seen = {1, 2}

Iteration 3: num = 3
  Is 3 in seen? No
  Add 3 to seen
  seen = {1, 2, 3}

Iteration 4: num = 1
  Is 1 in seen? YES! → Duplicate found
  Return True ✓

---

DRY RUN 2: HashSet Approach for [1, 2, 3, 4]

Array: [1, 2, 3, 4]
Goal: Find if any duplicate exists

Initial: seen = {}

Iteration 1: num = 1
  Is 1 in seen? No
  Add 1 to seen
  seen = {1}

Iteration 2: num = 2
  Is 2 in seen? No
  Add 2 to seen
  seen = {1, 2}

Iteration 3: num = 3
  Is 3 in seen? No
  Add 3 to seen
  seen = {1, 2, 3}

Iteration 4: num = 4
  Is 4 in seen? No
  Add 4 to seen
  seen = {1, 2, 3, 4}

Loop ends, no duplicate found
Return False ✓

---

DRY RUN 3: HashSet Approach for [5, 5]

Array: [5, 5]
Goal: Find if any duplicate exists

Initial: seen = {}

Iteration 1: num = 5
  Is 5 in seen? No
  Add 5 to seen
  seen = {5}

Iteration 2: num = 5
  Is 5 in seen? YES! → Duplicate found
  Return True ✓
"""


# ============================================================================
# TEST CASES
# ============================================================================

if __name__ == "__main__":
    # Test cases with edge cases
    test_cases = [
        # (input, expected, description)
        ([1, 2, 3, 1], True, "Basic duplicate at start and end"),
        ([1, 2, 3, 4], False, "No duplicates"),
        ([99, 99], True, "Adjacent duplicates"),
        ([1], False, "Single element"),
        ([], False, "Empty array"),
        ([1, 2, 3, 4, 5, 1], True, "Duplicate far apart"),
        ([-1, -1], True, "Negative duplicates"),
        ([1, 0, 1, 4, 1, 3], True, "Multiple occurrences"),
        ([0, 0], True, "Zero duplicates"),
        ([1, 2, 3, 4, 5], False, "Sequential no duplicates"),
        ([5, 4, 3, 2, 1], False, "Reverse sequential no duplicates"),
        ([-5, -4, -3, -2, -1], False, "Negative sequential no duplicates"),
        ([1000000, 999999, 1000000], True, "Large numbers with duplicate"),
        ([1, 1, 1, 1, 1], True, "All elements same"),
        ([10, 20, 30, 10], True, "Duplicate in middle"),
    ]
    
    print("=" * 70)
    print("LeetCode 217: Contains Duplicate - All Solutions Test")
    print("=" * 70)
    
    for i, (nums, expected, desc) in enumerate(test_cases, 1):
        # Test Brute Force
        result_bf = containsDuplicate_bruteforce(nums[:])  # Pass copy
        
        # Test Hash Set
        result_hs = containsDuplicate_hashset(nums[:])  # Pass copy
        
        # Test Set Comparison
        result_sc = containsDuplicate_set_comparison(nums[:])  # Pass copy
        
        # Check if all match expected output
        all_correct = (result_bf == expected and 
                       result_hs == expected and 
                       result_sc == expected)
        
        status = "✓ PASS" if all_correct else "✗ FAIL"
        print(f"\nTest {i}: {status}")
        print(f"  Desc:      {desc}")
        print(f"  Input:     {nums}")
        print(f"  Expected:  {expected}")
        print(f"  Results:   BF={result_bf} | HS={result_hs} | SC={result_sc}")
    
    print("\n" + "=" * 70)
    print(f"SUMMARY: {len(test_cases)} tests completed")
    print("RECOMMENDATION: Use HashSet approach for production code")
    print("- Best time complexity: O(n)")
    print("- Reasonable space trade-off: O(n)")
    print("=" * 70)
