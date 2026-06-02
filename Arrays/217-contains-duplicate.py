"""
LeetCode 217: Contains Duplicate
Problem: Given an integer array nums, return true if any value appears at least twice 
in the array, and return false if every element is distinct.

Time Complexity Analysis:
- Brute Force: O(n²)
- Hash Set: O(n)

Space Complexity Analysis:
- Brute Force: O(1)
- Hash Set: O(n)
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
# TEST CASES
# ============================================================================

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 2, 3, 1], True),           # Duplicate at beginning and end
        ([1, 2, 3, 4], False),          # No duplicates
        ([99, 99], True),               # Adjacent duplicates
        ([1], False),                   # Single element
        ([], False),                    # Empty array
        ([1, 2, 3, 4, 5, 1], True),    # Duplicate far apart
        ([-1, -1], True),               # Negative duplicates
        ([1, 0, 1, 4, 1, 3], True),    # Multiple occurrences
    ]
    
    print("=" * 70)
    print("LeetCode 217: Contains Duplicate - All Solutions Test")
    print("=" * 70)
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        # Test Brute Force
        result_bf = containsDuplicate_bruteforce(nums)
        
        # Test Hash Set
        result_hs = containsDuplicate_hashset(nums)
        
        # Test Set Comparison
        result_sc = containsDuplicate_set_comparison(nums)
        
        # Check if all match expected output
        all_correct = (result_bf == expected and 
                       result_hs == expected and 
                       result_sc == expected)
        
        status = "✓ PASS" if all_correct else "✗ FAIL"
        print(f"\nTest {i}: {status}")
        print(f"  Input:     {nums}")
        print(f"  Expected:  {expected}")
        print(f"  BruteForce: {result_bf} | HashSet: {result_hs} | SetComp: {result_sc}")
    
    print("\n" + "=" * 70)
    print("RECOMMENDATION: Use HashSet approach for production code")
    print("- Best time complexity: O(n)")
    print("- Reasonable space trade-off: O(n)")
    print("=" * 70)
