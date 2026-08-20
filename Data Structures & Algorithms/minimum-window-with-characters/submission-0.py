class Solution:
    def compareSubstrings(self,s:str)->str:
        s_dict = dict(Counter(s))
        print(self.target_dict, s)
        for key, value in self.target_dict.items():
            if s_dict.get(key, 0)<value:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        self.target_dict = dict(Counter(t))
        if not self.compareSubstrings(s):
            return ""
        left = 0
        right = len(s)
        while self.compareSubstrings(s[left:]):
            left+=1
        left-=1
        while self.compareSubstrings(s[left:right]):
            right-=1
        right+=1
        return s[left:right]

