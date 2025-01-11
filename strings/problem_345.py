
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
#
# Example 1:
# Input: s = "IceCreAm"
#
# Output: "AceCreIm"
# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
#
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_letters = ['a', 'e', 'i', 'o', 'u']
        reversed_string = list(s)
        left_idx = 0
        right_idx = len(s) - 1

        while left_idx <= right_idx:
            left_, right_ = None, None
            # find first vowel letter from beginning
            for i in range(left_idx, right_idx):
                left_idx = i
                if reversed_string[i].lower() in vowel_letters:
                    left_ = s[i]
                    break

            # find last vowel letter from the end
            for i in range(right_idx, left_idx, -1):
                right_idx = i
                if reversed_string[right_idx].lower() in vowel_letters:
                    right_ = s[i]
                    break

            if left_ and right_:
                reversed_string[left_idx] = right_
                reversed_string[right_idx] = left_
                left_idx += 1
                right_idx -= 1
            else:
                break

        return ''.join(reversed_string)


# test
if __name__ == '__main__':
    print(Solution().reverseVowels('IceCreAm') == 'AceCreIm')
    print(Solution().reverseVowels('leetcode') == 'leotcede')