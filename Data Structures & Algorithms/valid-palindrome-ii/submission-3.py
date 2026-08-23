class Solution:
    def isPalindrome(self, s:str, edit:int = 1):
        left, right = 0,len(s)-1
        while left < right:
            if edit == 0 and s[left]!=s[right]:
                return False
            elif s[left]!=s[right]:
                palindrome = self.isPalindrome(s[left+1:right+1], 0) | self.isPalindrome(s[left:right],0)
                return palindrome
            else:
                left+=1
                right-=1
        return True
            
    def validPalindrome(self, s: str) -> bool:
        return self.isPalindrome(s)