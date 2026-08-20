import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = 0
        upper = len(s)-1
        bound = string.ascii_letters + string.digits
        while lower < upper:
            while s[lower] not in bound and lower < upper:
                lower += 1
            while s[upper] not in bound and lower< upper :
                upper-=1
            if lower >= upper:
                break
            if s[lower].lower() == s[upper].lower():
                upper -= 1
                lower += 1
            else:
                return False
        return True