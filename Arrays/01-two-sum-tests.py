# LeetCode 1 - Two Sum | Test Cases

"""
Test Suite for Two Sum Problem
Covers: basic cases, edge cases, negative numbers, duplicates, large numbers
"""

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in seen:
                return [seen[remaining], i]
            seen[nums[i]] = i


# ============================================================================
# EDGE CASES AND TEST CASES
# ============================================================================
"""
Edge Cases to Consider:

1. Minimum size array (2 elements)
2. Duplicate numbers
3. Negative numbers
4. Zero values
5. Large numbers (within constraints)
6. Target is zero
7. Target is negative
8. Same number used twice (but different indices)
9. Multiple valid pairs (return any one)
10. Numbers at start/end of array
"""


def test_two_sum():
    solution = Solution()
    
    print("=" * 70)
    print("LeetCode 1: Two Sum - Comprehensive Test Suite")
    print("=" * 70)
    
    # Test 1: Basic case - example from problem
    result = solution.twoSum([2, 7, 11, 15], 9)
    expected = [0, 1]
    assert result == expected, f"Test 1 Failed: expected {expected}, got {result}"
    print("✓ Test 1 PASSED: Basic case [2, 7, 11, 15], target=9 → [0, 1]")
    
    # Test 2: Minimum size (2 elements)
    result = solution.twoSum([3, 3], 6)
    expected = [0, 1]
    assert result == expected, f"Test 2 Failed: expected {expected}, got {result}"
    print("✓ Test 2 PASSED: Minimum size [3, 3], target=6 → [0, 1]")
    
    # Test 3: Negative numbers
    result = solution.twoSum([-1, -2, -3, -4, -5], -8)
    expected = [2, 4]
    assert result == expected, f"Test 3 Failed: expected {expected}, got {result}"
    print("✓ Test 3 PASSED: Negative numbers [-1, -2, -3, -4, -5], target=-8 → [2, 4]")
    
    # Test 4: Mix of positive and negative
    result = solution.twoSum([3, -1, 2, -5, 7], 2)
    expected = [0, 1]
    assert result == expected, f"Test 4 Failed: expected {expected}, got {result}"
    print("✓ Test 4 PASSED: Mixed signs [3, -1, 2, -5, 7], target=2 → [0, 1]")
    
    # Test 5: Zero in array
    result = solution.twoSum([0, 4, 3, 0], 0)
    expected = [0, 3]
    assert result == expected, f"Test 5 Failed: expected {expected}, got {result}"
    print("✓ Test 5 PASSED: With zeros [0, 4, 3, 0], target=0 → [0, 3]")
    
    # Test 6: Target is zero
    result = solution.twoSum([-3, 4, 3, 90], 0)
    expected = [0, 2]
    assert result == expected, f"Test 6 Failed: expected {expected}, got {result}"
    print("✓ Test 6 PASSED: Target zero [-3, 4, 3, 90], target=0 → [0, 2]")
    
    # Test 7: Large numbers
    result = solution.twoSum([1000000, 1], 1000001)
    expected = [0, 1]
    assert result == expected, f"Test 7 Failed: expected {expected}, got {result}"
    print("✓ Test 7 PASSED: Large numbers [1000000, 1], target=1000001 → [0, 1]")
    
    # Test 8: Answer at end of array
    result = solution.twoSum([1, 2, 3, 4, 5], 9)
    expected = [3, 4]
    assert result == expected, f"Test 8 Failed: expected {expected}, got {result}"
    print("✓ Test 8 PASSED: Answer at end [1, 2, 3, 4, 5], target=9 → [3, 4]")
    
    # Test 9: Duplicates (different indices)
    result = solution.twoSum([5, 2, 5, 11], 10)
    expected = [0, 2]
    assert result == expected, f"Test 9 Failed: expected {expected}, got {result}"
    print("✓ Test 9 PASSED: Duplicates [5, 2, 5, 11], target=10 → [0, 2]")
    
    # Test 10: Unsorted array
    result = solution.twoSum([3, 2, 4], 6)
    expected = [1, 2]
    assert result == expected, f"Test 10 Failed: expected {expected}, got {result}"
    print("✓ Test 10 PASSED: Unsorted [3, 2, 4], target=6 → [1, 2]")
    
    # Test 11: Large array
    result = solution.twoSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19)
    expected = [8, 9]
    assert result == expected, f"Test 11 Failed: expected {expected}, got {result}"
    print("✓ Test 11 PASSED: Large array with 10 elements, target=19 → [8, 9]")
    
    # Test 12: Negative target
    result = solution.twoSum([1, -1, -2, 3], -3)
    expected = [1, 2]
    assert result == expected, f"Test 12 Failed: expected {expected}, got {result}"
    print("✓ Test 12 PASSED: Negative target [1, -1, -2, 3], target=-3 → [1, 2]")
    
    print("\n" + "=" * 70)
    print("ALL TESTS PASSED! ✓ (12/12)")
    print("=" * 70)


if __name__ == "__main__":
    test_two_sum()

