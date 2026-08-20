class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {i:0 for i in range(26)}
        if len(s) != len(t):
            return False
        for char in s:
            hashmap[ord(char) - 97] += 1
            # char_sum += 1
        for char in t:
            if hashmap[ord(char)-97] < 1:
                return False
            hashmap[ord(char)-97] -= 1
            # char_sum -= 1
        return True