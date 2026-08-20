class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return ""
        self.s = s
        self.len_s = len(s)
        res = set()
        for index in range(self.len_s):
            res.add((index, index))
            left, right = index, index
            palin = self.findPalindrome(left, right)
            res = res.union(palin)
            left, right = index, index + 1
            palin = self.findPalindrome(left, right)
            res = res.union(palin)
        return len(res)

    def findPalindrome(self, left, right):
        res = set()
        if left < 0 or right >= self.len_s or self.s[left] != self.s[right]:
            return res
        while left >= 0 and right < self.len_s:
            if self.s[left] == self.s[right]:
                res.add((left, right))
                left -= 1
                right += 1
            else:
                break
        return res