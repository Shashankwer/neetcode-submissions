class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {len(s): True}
        def recurseSearch(index):
            if index in cache:
                return cache[index]
            for w in wordDict:
                if (index+len(w)) <= len(s) and s[index:index+len(w)] == w:
                    if recurseSearch(index+len(w)):
                        cache[index] = True
                        return True
            cache[index] = False
            return False
        return recurseSearch(0)