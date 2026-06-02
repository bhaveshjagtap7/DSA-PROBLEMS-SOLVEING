# Two Sum - Complexity Analysis

## Approach Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (Nested Loops) | O(n²) | O(1) | Simple but slow |
| Hash Map (Optimal) | O(n) | O(n) | Best for interviews |
| Two Pointers (Sorted) | O(n log n) | O(1) | Modifies array |

## Detailed Analysis

### 1. Brute Force
```python
Time: O(n²)
- Outer loop: n iterations
- Inner loop: (n-1) + (n-2) + ... + 1 = n(n-1)/2 ≈ n²/2
- Total: O(n²)

Space: O(1)
- Only storing indices i and j
```

### 2. Hash Map (Recommended)
```python
Time: O(n)
- Single pass through array: n iterations
- Hash map lookup: O(1) average
- Hash map insert: O(1) average
- Total: O(n)

Space: O(n)
- Worst case: store all n elements in hash map
- Best case: store 1 element (early match)
```

### 3. Two Pointers (Requires Sorted Array)
```python
Time: O(n log n)
- Sort array: O(n log n)
- Two pointer scan: O(n)
- Total: O(n log n)

Space: O(1)
- Only two pointers
- NOTE: Modifies original array order
- Loses original indices (need index mapping)
```

## Why Hash Map is Best for Interviews

✓ **Optimal time complexity:** O(n)  
✓ **Single pass through array**  
✓ **Preserves original indices**  
✓ **No sorting required**  
✓ **Handles duplicates correctly**  
✓ **Works with negative numbers**  

Trade-off: Uses O(n) extra space, but it's worth it!

## Real-World Performance

For n = 10,000 elements:

| Approach | Operations | Time (approx) |
|----------|-----------|---------------|
| Brute Force | ~50,000,000 | 500ms |
| Hash Map | ~10,000 | 0.1ms |
| **Speedup** | **5000x faster!** | |

## Interview Tips

1. **Always mention brute force first** (shows you understand the problem)
2. **Then optimize to hash map** (shows problem-solving skills)
3. **Discuss trade-offs** (time vs space)
4. **Consider edge cases** (duplicates, negatives, empty array)

## Space-Time Trade-off

```
Brute Force:  [Low Space, High Time]  ← Not scalable
Hash Map:     [Medium Space, Low Time] ← Best balance ✓
```

The extra O(n) space is **acceptable** because:
- Modern systems have plenty of memory
- Time complexity matters more for scalability
- O(n) space is linear, not exponential
