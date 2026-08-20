class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = {}
        for c in s:
            if c in char_map:
                char_map[c] +=1
            else:
                char_map[c] = 1
        for c in t:
            if c in char_map:
                char_map[c] -=1
                if char_map[c] == 0:
                    char_map.pop(c)
            else:
                return False
        if len(char_map)==0:
            return True
        else:
            return False