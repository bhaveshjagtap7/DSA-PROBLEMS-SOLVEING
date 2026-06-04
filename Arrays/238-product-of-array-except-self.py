"""
LeetCode 238: Product of Array Except Self

Problem Statement:
Given an integer array nums, return an array answer such that answer[i] is equal 
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operator.

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow-up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)

Difficulty: Medium
Topics: Array, Prefix Sum
"""


# ============================================================================
# EXAMPLES
# ============================================================================
"""
Example 1:
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
Explanation:
  answer[0] = 2 * 3 * 4 = 24 (product of all except nums[0])
  answer[1] = 1 * 3 * 4 = 12 (product of all except nums[1])
  answer[2] = 1 * 2 * 4 = 8  (product of all except nums[2])
  answer[3] = 1 * 2 * 3 = 6  (product of all except nums[3])

Example 2:
Input: nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]
Explanation:
  answer[0] = 1 * 0 * (-3) * 3 = 0
  answer[1] = (-1) * 0 * (-3) * 3 = 0
  answer[2] = (-1) * 1 * (-3) * 3 = 9
  answer[3] = (-1) * 1 * 0 * 3 = 0
  answer[4] = (-1) * 1 * 0 * (-3) = 0

Example 3:
Input: nums = [2, 3, 4, 5]
Output: [60, 40, 30, 24]
Explanation:
  answer[0] = 3 * 4 * 5 = 60
  answer[1] = 2 * 4 * 5 = 40
  answer[2] = 2 * 3 * 5 = 30
  answer[3] = 2 * 3 * 4 = 24
"""



# ============================================================================
# APPROACH 1: BRUTE FORCE
# ============================================================================
"""
Strategy: For each position i, calculate product of all elements except i.
Use nested loops to multiply all elements except current index.

Time Complexity: O(n²) - For each element, iterate through array
Space Complexity: O(1) - Only output array (doesn't count as extra space)
"""

def productExceptSelf_bruteforce(nums):
    """
    Brute force approach with nested loops.
    
    Args:
        nums: List of integers
    
    Returns:
        List where result[i] = product of all elements except nums[i]
    """
    array_length = len(nums)
    result_array = []
    
    # For each position in array
    for current_index in range(array_length):
        current_product = 1
        
        # Multiply all elements except the one at current_index
        for multiply_index in range(array_length):
            if multiply_index != current_index:
                current_product *= nums[multiply_index]
        
        result_array.append(current_product)
    
    return result_array



# ============================================================================
# APPROACH 2: PREFIX AND SUFFIX PRODUCTS (Optimized)
# ============================================================================
"""
Strategy: Use prefix and suffix product arrays.

Key Insight:
For each position i, the result is:
  result[i] = (product of all elements before i) × (product of all elements after i)
  result[i] = prefix[i-1] × suffix[i+1]

We can precompute:
- prefix[i] = product of nums[0] to nums[i]
- suffix[i] = product of nums[i] to nums[n-1]

Time Complexity: O(n) - Three separate passes
Space Complexity: O(n) - Two additional arrays for prefix and suffix
"""

def productExceptSelf_prefix_suffix(nums):
    """
    Optimized approach using prefix and suffix product arrays.
    
    Args:
        nums: List of integers
    
    Returns:
        List where result[i] = product of all elements except nums[i]
    """
    array_length = len(nums)
    
    # Step 1: Build prefix products array
    # prefix[i] = product of all elements from index 0 to i
    prefix_products = [1] * array_length
    prefix_products[0] = nums[0]
    
    for i in range(1, array_length):
        prefix_products[i] = prefix_products[i - 1] * nums[i]

    
    # Step 2: Build suffix products array
    # suffix[i] = product of all elements from index i to n-1
    suffix_products = [1] * array_length
    suffix_products[array_length - 1] = nums[array_length - 1]
    
    for i in range(array_length - 2, -1, -1):
        suffix_products[i] = suffix_products[i + 1] * nums[i]

    
    # Step 3: Build result array
    # result[i] = prefix[i-1] × suffix[i+1]
    result_array = [1] * array_length
    
    for i in range(array_length):
        # Product of all elements before i
        left_product = prefix_products[i - 1] if i > 0 else 1
        
        # Product of all elements after i
        right_product = suffix_products[i + 1] if i < array_length - 1 else 1
        
        result_array[i] = left_product * right_product
    
    return result_array


# ============================================================================
# APPROACH 3: SPACE-OPTIMIZED O(1) SOLUTION
# ============================================================================
"""
Strategy: Build result array by computing prefix and suffix on-the-fly.

Instead of storing prefix and suffix arrays, we:
1. First pass (left to right): Store prefix products in result array
2. Second pass (right to left): Multiply by suffix products

This achieves O(n) time with O(1) extra space!

Time Complexity: O(n) - Two passes through array
Space Complexity: O(1) - Only output array (doesn't count)
"""

def productExceptSelf_optimized(nums):
    """
    Space-optimized O(1) solution.
    
    Args:
        nums: List of integers
    
    Returns:
        List where result[i] = product of all elements except nums[i]
    """
    array_length = len(nums)
    result_array = [1] * array_length
    
    # Pass 1: Fill result with prefix products
    # result[i] = product of all elements before index i
    prefix_product = 1
    for i in range(array_length):
        result_array[i] = prefix_product
        prefix_product *= nums[i]
    
    # Pass 2: Multiply by suffix products
    # result[i] *= product of all elements after index i
    suffix_product = 1
    for i in range(array_length - 1, -1, -1):
        result_array[i] *= suffix_product
        suffix_product *= nums[i]
    
    return result_array


class Solution(object):
    """LeetCode 238: Product of Array Except Self"""
    
    def productExceptSelf(self, nums):
        """
        Return array where each element is product of all others.
        
        Args:
            nums: List of integers
        
        Returns:
            List where result[i] = product of all elements except nums[i]
        """
        return productExceptSelf_optimized(nums)



# ============================================================================
# COMPLEXITY ANALYSIS
# ============================================================================
"""
APPROACH COMPARISON:

Approach              Time         Space        Notes
────────────────────────────────────────────────────────────────────
Brute Force          O(n²)        O(1)         Simple, too slow
Division Trick       O(n)         O(1)         Not allowed (uses division)
Prefix/Suffix Arrays O(n)         O(n)         Good, uses extra space
Space-Optimized      O(n)         O(1)         Optimal! ✓

WHY WE CAN'T USE DIVISION:
The obvious solution would be:
1. Calculate total product of all elements
2. For each index i, result[i] = total_product / nums[i]

But this has problems:
- Problem explicitly says "without using division operator"
- Doesn't work if any element is 0
- Integer division can lose precision

WHY SPACE-OPTIMIZED IS BEST:
- Linear time O(n): Two passes through array
- Constant space O(1): Only output array (which doesn't count)
- No division needed: Uses multiplication only
- Handles zeros correctly: No special cases needed
- Production-ready: Clean, efficient, robust

SCALABILITY:
For n = 100,000 elements:
- Brute Force:   ~10 billion operations (O(n²)) - Too slow!
- Optimized:     ~200,000 operations (2n) - Fast! ✓

TIME COMPLEXITY BREAKDOWN (Optimized):
- Pass 1 (prefix):  O(n)
- Pass 2 (suffix):  O(n)
- Total:            O(n)

SPACE COMPLEXITY BREAKDOWN (Optimized):
- Result array:     O(n) - Required output, doesn't count
- prefix_product:   O(1) - Single variable
- suffix_product:   O(1) - Single variable
- Total extra:      O(1) ✓

RECOMMENDATION: Use space-optimized approach for production!
"""



# ============================================================================
# EDGE CASES
# ============================================================================
"""
Edge Cases to Consider:

1. Array with zeros
   - Single zero: [1, 2, 0, 4] → [0, 0, 8, 0]
     Only the position with 0 gets non-zero product
   
   - Multiple zeros: [0, 0, 2] → [0, 0, 0]
     All products become 0

2. Array with negative numbers
   - [-1, 2, -3, 4] → Product signs alternate correctly
   - Algorithm handles negatives naturally

3. Minimum size array
   - [a, b] → [b, a]
     Each element is product of the other

4. All ones
   - [1, 1, 1, 1] → [1, 1, 1, 1]
     Identity case

5. Array with 1 and other numbers
   - [1, 2, 3] → [6, 3, 2]
     Ones don't affect products

6. Large numbers (within constraints)
   - Problem guarantees product fits in 32-bit integer
   - No overflow concerns

7. Mix of positive, negative, and zero
   - [2, -3, 0, 4] → Handles all signs correctly

8. Boundary values
   - nums[i] can be -30 to 30
   - Array length can be 2 to 100,000

IMPORTANT NOTES:
- Algorithm handles ALL edge cases naturally
- No special checks needed for zeros or negatives
- Prefix/suffix multiplication works universally
- Output array guaranteed to fit in 32-bit integers
"""


# ============================================================================
# TEST CASES
# ============================================================================

if __name__ == "__main__":
    test_cases = [
        # (input, expected, description)
        ([1, 2, 3, 4], [24, 12, 8, 6], "Basic case"),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0], "With zero in middle"),
        ([2, 3], [3, 2], "Minimum size (2 elements)"),
        ([1, 1, 1, 1], [1, 1, 1, 1], "All ones"),
        ([2, 3, 4, 5], [60, 40, 30, 24], "All positive"),
        ([-1, -2, -3], [-6, -3, -2], "All negative"),
        ([0, 0], [0, 0], "All zeros"),
        ([5, 0, 2, 0], [0, 0, 0, 0], "Multiple zeros"),
        ([1, 0], [0, 1], "Zero at end"),
        ([0, 1], [1, 0], "Zero at start"),
        ([2, -3, 4, -5], [-60, 40, -30, 24], "Mixed signs"),
    ]
    
    print("=" * 80)
    print("LeetCode 238: Product of Array Except Self - Test Results")
    print("=" * 80)
    
    passed = 0
    failed = 0
    
    for i, (nums, expected, description) in enumerate(test_cases, 1):
        # Test optimized solution
        result = productExceptSelf_optimized(nums[:])
        
        status = "✓ PASS" if result == expected else "✗ FAIL"
        if result == expected:
            passed += 1
        else:
            failed += 1
        
        print(f"\nTest {i}: {status}")
        print(f"  Description: {description}")
        print(f"  Input:       {nums}")
        print(f"  Expected:    {expected}")
        print(f"  Got:         {result}")
    
    print("\n" + "=" * 80)
    print(f"SUMMARY: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("Space-Optimized Solution: Time O(n) | Space O(1)")
    print("=" * 80)



# ============================================================================
# DRY RUN: SPACE-OPTIMIZED SOLUTION
# ============================================================================
"""
DRY RUN: nums = [1, 2, 3, 4]

Goal: result[i] = product of all elements except nums[i]
Expected output: [24, 12, 8, 6]

PASS 1: Build prefix products (left to right)
────────────────────────────────────────────────
Goal: result[i] = product of all elements BEFORE index i

Initial state:
  nums = [1, 2, 3, 4]
  result = [1, 1, 1, 1]
  prefix_product = 1

i=0: result[0] = prefix_product = 1
     prefix_product *= nums[0] = 1 * 1 = 1
     result = [1, 1, 1, 1]

i=1: result[1] = prefix_product = 1
     prefix_product *= nums[1] = 1 * 2 = 2
     result = [1, 1, 1, 1]

i=2: result[2] = prefix_product = 2
     prefix_product *= nums[2] = 2 * 3 = 6
     result = [1, 1, 2, 1]

i=3: result[3] = prefix_product = 6
     prefix_product *= nums[3] = 6 * 4 = 24
     result = [1, 1, 2, 6]

After Pass 1: result = [1, 1, 2, 6]
(Each position has product of all elements to its left)

PASS 2: Multiply by suffix products (right to left)
────────────────────────────────────────────────
Goal: Multiply result[i] by product of all elements AFTER index i

Initial state:
  result = [1, 1, 2, 6]
  suffix_product = 1

i=3: result[3] *= suffix_product = 6 * 1 = 6
     suffix_product *= nums[3] = 1 * 4 = 4
     result = [1, 1, 2, 6]

i=2: result[2] *= suffix_product = 2 * 4 = 8
     suffix_product *= nums[2] = 4 * 3 = 12
     result = [1, 1, 8, 6]

i=1: result[1] *= suffix_product = 1 * 12 = 12
     suffix_product *= nums[1] = 12 * 2 = 24
     result = [1, 12, 8, 6]

i=0: result[0] *= suffix_product = 1 * 24 = 24
     suffix_product *= nums[0] = 24 * 1 = 24
     result = [24, 12, 8, 6]

Final Answer: [24, 12, 8, 6] ✓

VERIFICATION:
  result[0] = 24 = 2 * 3 * 4 ✓ (all except nums[0])
  result[1] = 12 = 1 * 3 * 4 ✓ (all except nums[1])
  result[2] = 8  = 1 * 2 * 4 ✓ (all except nums[2])
  result[3] = 6  = 1 * 2 * 3 ✓ (all except nums[3])

───────────────────────────────────────────────────────────

DRY RUN 2: nums = [2, 3, 4]

PASS 1: Prefix products (left to right)
  i=0: result[0] = 1, prefix = 2
  i=1: result[1] = 2, prefix = 6
  i=2: result[2] = 6, prefix = 24
  
  After Pass 1: result = [1, 2, 6]

PASS 2: Suffix products (right to left)
  i=2: result[2] = 6 * 1 = 6, suffix = 4
  i=1: result[1] = 2 * 4 = 8, suffix = 12
  i=0: result[0] = 1 * 12 = 12, suffix = 24
  
  Final: result = [12, 8, 6]

VERIFICATION:
  result[0] = 12 = 3 * 4 ✓
  result[1] = 8  = 2 * 4 ✓
  result[2] = 6  = 2 * 3 ✓

KEY OBSERVATION:
The two-pass approach cleverly builds the final answer:
- Pass 1 stores "product of everything on the left"
- Pass 2 multiplies by "product of everything on the right"
- Together they give "product of everything except current element"
"""
