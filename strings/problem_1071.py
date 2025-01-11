# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t
# (i.e., t is concatenated with itself one or more times).
#
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
# Example 1:
#
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:
#
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:
#
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
#
#
# Constraints:
#
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.

# class Solution:
def gcd_of_strings(str1: str, str2: str) -> str:
    str1_prefixes = []
    for i in range(len(str1), 0, -1):
        str1_prefixes.append(str1[:i])

    str2_prefixes = []
    for i in range(len(str2), 0, -1):
        str2_prefixes.append(str2[:i])

    result = ''
    for str1_prefix in str1_prefixes:
        if (str1_prefix in str2_prefixes
                and (len(str1_prefix) == len(str1) or str1_prefix*str1.count(str1_prefix) == str1)
                and (len(str1_prefix) == len(str2) or str1_prefix*str2.count(str1_prefix) == str2)
        ):
            result = str1_prefix
            break

    return result

def gcd_of_strings_2(self, str1: str, str2: str) -> str:
    len1, len2 = len(str1), len(str2)

    def valid(k):
        if len1 % k or len2 % k:
            return False
        n1, n2 = len1 // k, len2 // k
        base = str1[:k]
        return str1 == n1 * base and str2 == n2 * base

    for i in range(min(len1, len2), 0, -1):
        if valid(i):
            return str1[:i]
    return ""

# test
if __name__ == '__main__':
    print(gcd_of_strings(str1='ABCABC', str2='ABC') == 'ABC')
    print(gcd_of_strings(str1='ABABAB', str2='ABAB') == 'AB')
    print(gcd_of_strings(str1='ABAB', str2='ABABAB') == 'AB')
    print(gcd_of_strings(str1='LEET', str2='CODE') == '')
    print(gcd_of_strings(str1='TAUXXTAUXXTAUXXTAUXXTAUXX', str2='TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX') == 'TAUXX')
    print(gcd_of_strings(str1='AA', str2='A') == 'A')
