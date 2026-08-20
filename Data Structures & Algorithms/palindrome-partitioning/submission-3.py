class Solution:
    def isPalindrome(self, s:str) -> bool:
        if not s or len(s) == 0:
            return False
        left, right = 0,len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left = left + 1
            right = right -1
        return True

    def partition(self, s: str) -> List[List[str]]:
        subsets = []
        result = []
        len_s = len(s)
        def backtrack(index):
            if index >= len_s:
                result.append(subsets.copy())
            for j in range(index, len_s):
                if self.isPalindrome(s[index:j+1]):
                    subsets.append(s[index:j+1])
                    backtrack(j+1)
                    subsets.pop()
        backtrack(0)
        return result
            

        
        