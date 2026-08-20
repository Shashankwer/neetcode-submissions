class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = {}
        def is_anagram(w1,w2):
            return Counter(w1) == Counter(w2)
        for s in strs:
            l = len(s)
            matched = False
            if l in anagram_list:
                for index, al in enumerate(anagram_list[l]):
                    if is_anagram(s, al[0]):
                        anagram_list[l][index].append(s)
                        matched = True
                        break
                if not matched:
                    anagram_list[l].append([s])
            else:
                anagram_list[l] = [[s]]
        results = []
        for key, value in anagram_list.items():
            results.extend(value)
        return results



