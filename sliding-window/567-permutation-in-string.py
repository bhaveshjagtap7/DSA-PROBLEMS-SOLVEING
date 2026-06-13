"""
LeetCode 567 - Permutation in String

Problem Statement:
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is a substring of s2.

Constraints:
- 1 <= s1.length, s2.length <= 10^4
- s1 and s2 consist of lowercase English letters.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

"""
Initial Brute Force Idea:
1. Generate all permutations of s1 (O(n!))
2. Check each permutation to see if it exists as a substring of s2 (O(m * n))
Total time: O(n! * m * n) — this is way too slow for n >= 10, let alone 10^4!
So we definitely need a smarter approach!
"""

"""
Frequency Map Explanation:
Since two strings are permutations of each other if and only if they have exactly the same character frequencies,
we don't need to generate permutations at all! Instead, we can count the frequency of each character in s1,
and then check if any window of length len(s1) in s2 has the exact same frequency counts!
"""

"""
Sliding Window Intuition:
- We need to check all windows of length len(s1) in s2
- Instead of recalculating frequency map for each window from scratch,
  we can maintain a sliding frequency map that adds the new character entering the window
  and removes the character that's leaving the window (as we slide the window)
- When the sliding window's frequency matches s1's frequency, return True!
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        
        # If s1 is longer than s2, impossible to have permutation
        if len_s1 > len_s2:
            return False
        
        # Step 1: Initialize frequency maps
        s1_freq = [0] * 26
        window_freq = [0] * 26
        for i in range(len_s1):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            window_freq[ord(s2[i]) - ord('a')] += 1
        
        # Step 2: Calculate initial number of matching frequencies
        matches = 0
        for i in range(26):
            if s1_freq[i] == window_freq[i]:
                matches += 1
        
        # Check if initial window is a match
        if matches == 26:
            return True
        
        # Step 3: Slide the window
        for right in range(len_s1, len_s2):
            # Process right character (add to window)
            r_idx = ord(s2[right]) - ord('a')
            # If before adding, frequencies matched, we lose a match
            if window_freq[r_idx] == s1_freq[r_idx]:
                matches -= 1
            window_freq[r_idx] += 1
            # If now they match again, gain a match
            if window_freq[r_idx] == s1_freq[r_idx]:
                matches += 1
            
            # Process left character (remove from window)
            left = right - len_s1
            l_idx = ord(s2[left]) - ord('a')
            # If before removing, frequencies matched, lose a match
            if window_freq[l_idx] == s1_freq[l_idx]:
                matches -= 1
            window_freq[l_idx] -= 1
            # If now they match again, gain a match
            if window_freq[l_idx] == s1_freq[l_idx]:
                matches += 1
            
            # If all 26 characters match, return True immediately
            if matches == 26:
                return True
        
        return False


"""
Time Complexity:
- Brute force: O(n! * n * m), which is way too slow
- Optimized sliding window (current): O(n + m), since we process each character in s1 and s2 exactly once, and the frequency map operations are O(26) → which is O(1) constant time
Space Complexity:
- O(1), since we use fixed-size arrays of size 26, regardless of input size

Edge Cases:
1. s1 length > s2 length → return False immediately
2. s1 exactly matches entire s2 → return True
3. s1 length = 1 (check if s2 contains that single character
4. All characters same (e.g., s1 = "aaa", s2 = "aaabaaa")
5. s2 contains permutation at the very start of s2
6. s2 contains permutation at the very end of s2

Dry Run Example:
s1 = "ab" (freq: a:1, b:1), s2 = "eidbaooo"
- Initial window = "ei" (freq e:1, i:1, matches with s1? a:0, b:0 → matches: 24 not 26 → no)
- Slide to right: "id" → same as above
- Next: "db" → d:1, b:1 → matches 24
- Next: "ba" → b:1, a:1 → matches 26! → return True!

Interview Insights:
- Always check edge cases first! (like s1 longer than s2)
- Frequency map is a common pattern for permutation/anagram problems
- Optimizing the comparison using "matches" counter is a key optimization to avoid O(26) checks every time (though even O(26) is acceptable, but matches makes it cleaner and faster in practice
- Using arrays for frequency maps (since lowercase letters are fixed at 26) are more efficient than hash maps in this problem
"""
