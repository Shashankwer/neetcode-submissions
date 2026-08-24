class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0,1
        if len(s) in [0,1]:
            return len(s)
        result = 1
        while right < len(s):
            if s[right] not in s[left:right]:
                right+=1
                result = max(len(s[left:right]),result)
            else:
                while s[right] in s[left:right]:
                    left+=1
                right+=1
                result = max(len(s[left:right]),result)
        return result