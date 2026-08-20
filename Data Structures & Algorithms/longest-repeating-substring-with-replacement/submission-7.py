class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        l = 0
        window_size = 0
        maxf = 0
        maxc = ''
        for c in s:
            freq_map[c] = freq_map.get(c,0)+1 
            if freq_map[c] > maxf:
                maxf = freq_map[c]
                maxc = c
            window_size+=1
            if window_size - maxf > k:
                window_size-=1
                freq_map[s[l]]-=1
                l+=1
        print(freq_map)
        return window_size