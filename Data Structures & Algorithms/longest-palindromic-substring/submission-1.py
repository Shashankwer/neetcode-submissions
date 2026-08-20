class Solution:
    def longestPalindrome(self, s: str=None) -> str:
        if not s:
            return ""
        self.s = s
        self.len_s = len(s)
        len_s = len(s)
        max_len = -1
        res = ""
        for index in range(len_s):
            left, right = index-1, index+1
            len_palin, left, right = self.findPalindrome(left, right)
            if len_palin >= max_len:
                max_len = len_palin
                res = self.s[left:right + 1]
            left, right = index, index + 1
            len_palin, left, right = self.findPalindrome(left, right)
            if len_palin >= max_len:
                max_len = len_palin
                res = self.s[left:right + 1]
        return res

    def findPalindrome(self, left, right):
        if left < 0 or right >= self.len_s or self.s[left] != self.s[right] :
            return -1, left, right
        while (left -1) >= 0 and right+1 < self.len_s:
            if self.s[left-1] == self.s[right+1]:
                left -= 1
                right += 1
            else:
                break
        return right - left + 1, left, right