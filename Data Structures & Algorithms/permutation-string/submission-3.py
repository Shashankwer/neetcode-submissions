class Solution:
    def checkMatch(self, l2) -> bool:
        return self.freq_match == dict(Counter(l2))

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        self.freq_match = dict(Counter(s1))
        window_size = len(s1)
        left = 0
        result_size = len(s2)
        while (left+window_size)<=result_size:
            r = self.checkMatch(s2[left:left+window_size])
            if r:
                return True
            else:
                left+=1
        return False