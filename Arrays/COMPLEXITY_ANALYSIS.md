# Complexity Analysis - Binary Search

## Problem: Leetcode 704

### Optimized Solution Complexity

#### Time Complexity: **O(log n)**
- In each iteration, we eliminate half of the remaining elements
- For an array of size n:
  - After 1st iteration: n/2 elements remain
  - After 2nd iteration: n/4 elements remain
  - After 3rd iteration: n/8 elements remain
  - After kth iteration: n/2^k elements remain
  
- We stop when n/2^k = 1
- Therefore: 2^k = n → k = log₂(n)
- **Time Complexity = O(log n)**

#### Example:
- Array of 1,000 elements: max ~10 iterations
- Array of 1,000,000 elements: max ~20 iterations

#### Space Complexity: **O(1)**
- We only use a constant amount of extra space (left, right, mid pointers)
- No recursive calls (iterative approach)
- No additional data structures

### Comparison with Brute Force

| Approach | Time Complexity | Space Complexity | Suitable For |
|----------|-----------------|------------------|--------------|
| **Brute Force (Linear)** | O(n) | O(1) | Unsorted arrays, small datasets |
| **Binary Search** | O(log n) | O(1) | **Sorted arrays, large datasets** |

### Performance Comparison

For an array of **1,000,000 elements**:
- **Linear Search**: ~1,000,000 operations (worst case)
- **Binary Search**: ~20 operations (worst case)
- **Speedup**: 50,000x faster ⚡

### Why Use Binary Search?
1. **Dramatically faster** for large sorted datasets
2. **Same space complexity** as linear search
3. **Scales logarithmically** as data grows
4. **Predictable performance** - O(log n) guaranteed

### Key Insights
- Only works on **sorted data**
- Must choose between keeping data sorted or using linear search
- Sorting cost: O(n log n) - worth it if you'll search many times
