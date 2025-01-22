# 1456. Maximum Number of Vowels in a Substring of Given Length

# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
## Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

# Example 2:
# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.

# Example 3:
# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.

# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= s.length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        # define vowel letters
        vowel_letters = ['a', 'e', 'i', 'o', 'u']

        result = 0

        # init step, take first k elements and calculate number of vowels
        for i in range(0, k):
            if s[i] in vowel_letters:
                result += 1

        # slide window and take into account s[i] and s[i-k]
        local_res = result
        for i in range(k, len(s)):
            # we already reach possible max, no need to iterate though whole string
            if result == k:
                break
            if s[i] in vowel_letters:
                local_res += 1
            if s[i - k] in vowel_letters:
                local_res -= 1

            if local_res > result:
                result = local_res

        return result

# test
if __name__ == '__main__':
    print(Solution().maxVowels('abciiidef', 3) == 3)
    print(Solution().maxVowels('aeiou', 2) == 2)
    print(Solution().maxVowels('leetcode', 3) == 2)
    print(Solution().maxVowels('a', 1) == 1)
    print(Solution().maxVowels('s', 1) == 0)
    print(Solution().maxVowels('tryhard', 4) == 1)