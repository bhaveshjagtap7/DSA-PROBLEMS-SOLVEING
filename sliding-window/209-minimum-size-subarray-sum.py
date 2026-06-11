"""
LeetCode 209 - Minimum Size Subarray Sum

Problem Statement:
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Constraints:
- 1 <= target <= 10^9
- 1 <= nums[i] <= 10^4
- 1 <= nums.length <= 10^5

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
"""

def minSubArrayLenBruteForce(target: int, nums: list[int]) -> int:
    """
    Brute Force Approach:
    Iterate through all possible subarrays, calculate their sums, and check if they are >= target.
    Since we want the minimal length, we track the minimum length found.
    """
    n = len(nums)
    min_len = float('inf')
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum >= target:
                min_len = min(min_len, j - i + 1)
                break
                
    return 0 if min_len == float('inf') else min_len

"""
Sliding Window Intuition:
Rather than checking all subarrays from scratch, we can use a sliding window (two pointers, left and right) 
to find the minimal subarray length in O(n) time.
1. We expand the window by moving the `right` pointer to the right and adding `nums[right]` to our running sum.
2. As soon as the running sum is greater than or equal to `target`, we try to shrink the window from the left 
   by moving the `left` pointer to the right. 
3. Shrinking the window helps us find the smallest valid subarray ending at the current `right` pointer that satisfies the condition. 
4. We record the minimum window size at each step where the sum >= target.
5. This works because all elements in `nums` are positive, which means the subarray sum increases monotonically 
   as the window expands, and decreases monotonically as the window shrinks.
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """
        Optimized sliding window approach to find minimal length subarray with sum >= target.
        """
        left = 0
        current_sum = 0
        min_length = float('inf')
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink the window from left as much as possible while maintaining sum >= target
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        return 0 if min_length == float('inf') else min_length


"""
Time Complexity:
- Brute Force: O(n^2) - Two nested loops
- Sliding Window: O(n) - Each element is processed at most twice (once by right pointer, once by left pointer)

Space Complexity:
- Both approaches use O(1) additional space (excluding input storage)

Interview Insights:
- Always start with brute force, then optimize
- The sliding window only works when elements are positive (monotonic sum property)
- Ask clarifying questions about constraints, edge cases, etc.
"""

"""
Edge Cases:
1. Single element equal to target: nums=[5], target=5 → Output:1
2. Single element smaller than target: nums=[3], target=5 → Output:0
3. Entire array sum less than target: nums=[1,1,1], target=5 → Output:0
4. Target exactly matches entire array sum: nums=[2,3,1], target=6 → Output:3
5. Multiple valid windows: nums=[2,3,1,2,4,3], target=7 → Output:2
"""

