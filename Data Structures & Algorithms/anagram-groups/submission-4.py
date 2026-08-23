class Solution:
    def anagram_key(self, s):
        r = [0]*26
        for c in s:
            r[ord(c)-97]+=1
        return tuple(r)
        

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for s in strs:
            k = self.anagram_key(s)
            if k in anagram_map:
                anagram_map[k].append(s)
            else:
                anagram_map[k] = [s]
        result = []
        for r in anagram_map.values():
            result.append(r)
        return result