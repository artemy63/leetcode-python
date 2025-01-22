# 443. String Compression

from typing import List


# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
# Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.
#
# You must write an algorithm that uses only constant extra space.

# Example 1:
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

# Example 2:
# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.

# Example 3:
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

class Solution:
    def compress(self, chars: List[str]) -> int:
        # pointer to slot in source array in order to write number of chars or next char
        idx_to_write = 1
        # initial count of certain char
        curr_char_count = 1
        # cause first char will not change start form 1 idx of source array
        for i in range(1, len(chars)):
            # if current char equals to previous we need to increase number of entries but there are some corner cases
            if chars[i] == chars[i - 1]:
                curr_char_count += 1

                # if it is last element of array we need to record number of entries for given char
                # but it is necessary to consider that '12' should be written as separate '1' and '2'
                if i == len(chars) - 1:
                    # so transform number of entries into str and after that split by chars via list
                    curr_char_count_str_arr = list(str(curr_char_count))
                    # and write it char by char, increasing idx_to_write
                    for j in range(0, len(curr_char_count_str_arr)):
                        chars[idx_to_write] = curr_char_count_str_arr[j]
                        idx_to_write += 1
            else:
                # if sequence of entries are broken it's necessary to write that number
                if curr_char_count > 1:
                    curr_char_count_str_arr = list(str(curr_char_count))
                    for j in range(0, len(curr_char_count_str_arr)):
                        chars[idx_to_write] = curr_char_count_str_arr[j]
                        idx_to_write += 1
                    curr_char_count = 1

                chars[idx_to_write] = chars[i]
                idx_to_write += 1

        print(chars[:idx_to_write])
        return len(chars[:idx_to_write])


# test
if __name__ == '__main__':
    print(Solution().compress(["a", "a", "b", "b", "c", "c", "c"]) == 6)
    print(Solution().compress(["a"]) == 1)
    print(Solution().compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) == 4)
