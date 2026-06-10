"""
LeetCode 49: Group Anagrams

Problem Statement:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

Time Complexity Analysis:
- Approach 1 (Initial / Brute Force): O(N^2 * K log K)
  Where N is the number of strings and K is the maximum length of a string.
  We compare each string against the representative of all existing groups (up to N groups).
  Each comparison does sorting of size K which takes O(K log K).
- Approach 2 (HashMap with Sorted Keys): O(N * K log K)
  We iterate through N strings. For each string of length K, we sort the characters
  in O(K log K) time and insert it into a hash map. HashMap insertions/lookups take O(K) 
  average time for string keys.
- Approach 3 (Optimized HashMap with Count Keys): O(N * K)
  We iterate through N strings. For each string of length K, we count character frequencies
  in O(K) time and insert/lookup the tuple representation of size 26 in the HashMap in O(1) 
  average time.

Space Complexity Analysis:
- Approach 1 (Initial / Brute Force): O(N * K)
  To store the resulting groups of anagrams.
- Approach 2 (HashMap with Sorted Keys): O(N * K)
  To store the hash map containing N strings partitioned by their sorted keys of length K.
- Approach 3 (Optimized HashMap with Count Keys): O(N * K)
  To store the hash map containing N strings partitioned by their count tuple keys of size 26.
"""

from collections import defaultdict

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]


# ============================================================================
# EDGE CASES TO CONSIDER
# ============================================================================
"""
1. Empty array: Input: [] -> Output: [] (Though constraints specify 1 <= strs.length)
2. Single empty string: Input: [""] -> Output: [[""]]
3. Multiple empty strings: Input: ["", ""] -> Output: [["", ""]]
4. Single character string: Input: ["a"] -> Output: [["a"]]
5. No anagrams: Input: ["abc", "def", "ghi"] -> Output: [["abc"], ["def"], ["ghi"]]
6. All anagrams: Input: ["abc", "bca", "cab"] -> Output: [["abc", "bca", "cab"]]
7. Identical strings: Input: ["a", "a", "a"] -> Output: [["a", "a", "a"]]
8. Different length strings: Input: ["a", "ab", "abc"] -> Output: [["a"], ["ab"], ["abc"]]
"""


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def is_anagram(str1: str, str2: str) -> bool:
    """
    Checks if two strings are anagrams of each other.
    Two strings are anagrams if their sorted representations are identical.
    """
    return sorted(str1) == sorted(str2)


# ============================================================================
# APPROACH 1: INITIAL/BRUTE FORCE GROUPING
# ============================================================================

def groupAnagrams_initial(strs):
    """
    Initial grouping approach.
    We iterate through the input strings. For each string, we try to place it
    into an existing group of anagrams. We determine if a string belongs to a group
    by comparing its sorted character list with the sorted version of the first
    string in the group.
    
    If it fits in an existing group, we append it. Otherwise, we create a new group.
    """
    groups = []
    
    for s in strs:
        found_group = False
        for group in groups:
            # Check if current string is an anagram of the group representative
            if is_anagram(s, group[0]):
                group.append(s)
                found_group = True
                break
        
        # If no matching group is found, create a new group
        if not found_group:
            groups.append([s])
            
    return groups


# ============================================================================
# APPROACH 2: HASHMAP OPTIMIZATION (Sorted String Key)
# ============================================================================

def groupAnagrams_hashmap(strs):
    """
    HashMap-based approach.
    Key insight: All anagrams will yield the exact same string when sorted.
    By using the sorted string as a key in a hash map, we can group all anagrams
    together in O(N * K log K) time, where N is the number of strings and K is the
    maximum length of a string.
    """
    anagram_map = defaultdict(list)
    
    for s in strs:
        # Sort the characters of s and join them back into a string key
        sorted_key = "".join(sorted(s))
        # Group s under this unique sorted key
        anagram_map[sorted_key].append(s)
        
    return list(anagram_map.values())


# ============================================================================
# APPROACH 3: OPTIMIZED HASHMAP (Character Count Key)
# ============================================================================

def groupAnagrams_optimized(strs):
    """
    Optimized HashMap-based approach.
    Instead of sorting each string (which takes O(K log K) time), we compute the
    frequency of each character (a-z) in O(K) time.
    We use a tuple of size 26 containing these frequencies as the key in our map.
    This runs in O(N * K) time.
    """
    anagram_map = defaultdict(list)
    
    for s in strs:
        # Create a frequency count array of size 26 for lowercase English letters
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
            
        # Convert list to tuple to make it hashable and use it as key
        anagram_map[tuple(count)].append(s)
        
    return list(anagram_map.values())


# ============================================================================
# TEST CASES
# ============================================================================

if __name__ == "__main__":
    test_cases = [
        # (input_list, expected_output, description)
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
            "Standard multi-anagram mix"
        ),
        (
            [""],
            [[""]],
            "Single empty string"
        ),
        (
            ["a"],
            [["a"]],
            "Single character string"
        ),
        (
            ["", ""],
            [["", ""]],
            "Multiple empty strings"
        ),
        (
            ["abc", "def", "ghi"],
            [["abc"], ["def"], ["ghi"]],
            "No anagrams present"
        ),
        (
            ["abc", "bca", "cab"],
            [["abc", "bca", "cab"]],
            "All strings are anagrams"
        ),
        (
            ["a", "a", "a"],
            [["a", "a", "a"]],
            "Identical strings"
        ),
        (
            ["a", "ab", "abc"],
            [["a"], ["ab"], ["abc"]],
            "Different length strings"
        ),
        (
            [],
            [],
            "Empty list (Extreme edge case)"
        )
    ]
    
    def normalize(groups):
        """Helper to sort groups and their elements for comparison."""
        return sorted([sorted(g) for g in groups])
        
    print("=" * 80)
    print("LeetCode 49: Group Anagrams - Test Suite")
    print("=" * 80)
    
    all_success = True
    for i, (strs, expected, desc) in enumerate(test_cases, 1):
        # Run all three implementations
        res_initial = groupAnagrams_initial(strs[:])
        res_hashmap = groupAnagrams_hashmap(strs[:])
        res_optimized = groupAnagrams_optimized(strs[:])
        
        # Normalize outputs to ignore order
        norm_expected = normalize(expected)
        norm_initial = normalize(res_initial)
        norm_hashmap = normalize(res_hashmap)
        norm_optimized = normalize(res_optimized)
        
        match_initial = norm_initial == norm_expected
        match_hashmap = norm_hashmap == norm_expected
        match_optimized = norm_optimized == norm_expected
        
        passed = match_initial and match_hashmap and match_optimized
        if not passed:
            all_success = False
            
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"\nTest {i}: {desc} -> {status}")
        print(f"  Input:    {strs}")
        print(f"  Expected: {expected}")
        print(f"  Initial:  {res_initial} (Match: {match_initial})")
        print(f"  HashMap:  {res_hashmap} (Match: {match_hashmap})")
        print(f"  Opt Count:{res_optimized} (Match: {match_optimized})")
        
    print("\n" + "=" * 80)
    if all_success:
        print("SUMMARY: All test cases passed successfully!")
    else:
        print("SUMMARY: Some test cases failed.")
    print("=" * 80)
