# 392. Is Subsequence

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
# of the characters without disturbing the relative positions of the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        if len(t) == 0:
            return False

        s_pointer = 0
        t_pointer = 0

        # перебирараю всю строку t, проверяя, есть ли в ней следующий символ "подстроки" s
        while s_pointer < len(s) and t_pointer < len(t):
            for i in range(t_pointer, len(t)):
                if t[i] == s[s_pointer]:
                    t_pointer += 1
                    s_pointer += 1
                    break
                else:
                    t_pointer += 1

        if s_pointer == len(s):
            return True
        else:
            return False


# test
if __name__ == '__main__':
    print(Solution().isSubsequence('abc', 'ahbgdc') == True)
    print(Solution().isSubsequence('axc', 'ahbgdc') == False)
    print(Solution().isSubsequence('abc', 'abcabcabcabcabcabc') == True)
