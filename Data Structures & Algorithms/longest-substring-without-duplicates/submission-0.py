class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_char = 0
        current_substring = ''
        for c in s:
            if c not in current_substring:
                current_substring+=c
                if max_char < len(current_substring):
                    max_char = len(current_substring)
            else:
                current_substring = current_substring[current_substring.index(c)+1:] + c
        return max_char

