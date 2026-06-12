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
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)
        current_vowels = 0
        
        # Calculate initial window sum
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
        
        max_vowels = current_vowels
        
        # Slide the window
        for i in range(k, n):
            # Remove leftmost character of previous window
            if s[i - k] in vowels:
                current_vowels -= 1
            # Add new rightmost character of current window
            if s[i] in vowels:
                current_vowels += 1
            
            max_vowels = max(max_vowels, current_vowels)
        
        return max_vowels
