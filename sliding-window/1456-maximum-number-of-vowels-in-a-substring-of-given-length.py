"""
LeetCode 1456 - Maximum Number of Vowels in a Substring of Given Length

Problem Statement:
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
- 1 <= k <= s.length

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 has 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
"""

def maxVowelsBruteForce(s: str, k: int) -> int:
    """
    Brute Force Approach:
    Iterate over every possible window of size k, count the number of vowels in each window,
    and keep track of the maximum count found.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    max_count = 0
    n = len(s)
    
    for i in range(n - k + 1):
        current_count = 0
        for j in range(i, i + k):
            if s[j] in vowels:
                current_count += 1
        max_count = max(max_count, current_count)
    
    return max_count


"""
Sliding Window Intuition:
Instead of recalculating the number of vowels for every new window from scratch, 
we can optimize by using a sliding window approach of fixed size k:
1. Calculate the number of vowels in the first window (from 0 to k-1)
2. Then, for each subsequent window, subtract 1 if the element leaving the window is a vowel,
   and add 1 if the new element entering the window is a vowel.
3. Keep track of the maximum count encountered!
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        Optimized sliding window approach to find maximum number of vowels in any substring of length k.
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)
        current_vowel_count = 0
        
        # Initialize the first window
        for i in range(k):
            if s[i] in vowels:
                current_vowel_count += 1
        
        max_vowel_count = current_vowel_count
        
        # Slide the window across the string
        for right in range(k, n):
            # Remove the leftmost character from the previous window
            if s[right - k] in vowels:
                current_vowel_count -= 1
            # Add the new rightmost character to the current window
            if s[right] in vowels:
                current_vowel_count += 1
            
            # Update the maximum if current window has more vowels
            max_vowel_count = max(max_vowel_count, current_vowel_count)
        
        return max_vowel_count


"""
Time Complexity:
- Brute force: O(n*k) - For each of (n - k + 1) windows, we check k elements
- Sliding window: O(n) - We process each character exactly twice (once when adding, once when removing)

Space Complexity:
- Both approaches use O(1) additional space (only a few variables and a fixed-size vowel set)

Edge Cases:
1. k equals length of string (s = "a", k=1 → 1)
2. No vowels at all (s = "xyz", k=2 → 0)
3. All vowels (s = "aeiou", k=5 →5)
4. k=1 (max single character vowel count)

Dry Run Example:
s = "abciiidef", k=3
Initial window: "abc" → 1 vowel
Next window: "bci" → 1 vowel
Next: "cii" → 2 vowels
Next: "iii" → 3 vowels (max)
Next: "iid" →2, "ide"→2, "def"→1 → final max is 3

Interview Notes:
- Always start with brute force to show understanding, then optimize
- Sliding window is perfect for fixed-size subarray problems
- Remember to use a set for O(1) vowel lookups
"""
