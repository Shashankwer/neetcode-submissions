class Solution:
    def check_match_window(self, l1, l2) -> bool:
        print(l1, l2)
        return dict(Counter(l1)) == dict(Counter(l2))
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        window_size = len(s1)
        left = 0
        result_size= len(s2)
        while (left+window_size)<=len(s2):
            r = self.check_match_window(s1, s2[left:left+window_size])
            if r:
                return True
            else:
                left+=1
        return False
