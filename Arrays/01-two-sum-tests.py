# LeetCode 1 - Two Sum | Test Cases

```python
def test_two_sum():
    solution = Solution()
    
    # Test 1: Basic case
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    print("✓ Test 1 passed: [2, 7, 11, 15], target=9 → [0, 1]")
    
    # Test 2: Negative numbers
    assert solution.twoSum([-1, -2, -3, 5, 6], 3) == [2, 3]
    print("✓ Test 2 passed: [-1, -2, -3, 5, 6], target=3 → [2, 3]")
    
    # Test 3: Duplicates
    assert solution.twoSum([3, 3], 6) == [0, 1]
    print("✓ Test 3 passed: [3, 3], target=6 → [0, 1]")
    
    # Test 4: Large numbers
    assert solution.twoSum([1000000, 1], 1000001) == [1, 0]
    print("✓ Test 4 passed: [1000000, 1], target=1000001 → [1, 0]")
    
    print("\nAll tests passed! ✓")

if __name__ == "__main__":
    test_two_sum()
```
