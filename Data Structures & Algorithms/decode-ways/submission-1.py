class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}

        def decodeRecurse(index):
            if index in dp:
                return dp[index]
            if s[index] == "0":
                return 0
            
            res = decodeRecurse(index+1)

            if index + 1 < len(s) and (
                s[index] == "1" or s[index] == "2" and
                s[index + 1] in "0123456"
            ):
                res += decodeRecurse(index+2)
            dp[index] = res
            return res
        return decodeRecurse(0)
        