class TrieNode:
    def __init__(self):
        self.child = {}
        self.word = False

class TrieSearch:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        currNode = self.root
        for c in word:
            if c in currNode.child:
                currNode = currNode.child[c]
            else:
                currNode.child[c] = TrieNode()
                currNode = currNode.child[c]
        currNode.word = True
    
    def search(self, word):
        def dfs(index, root):
            # for each word try to get dfs:
            curr = root
            for i in range(index, len(word)):
                c = word[i]
                if c == "*":
                    for node in curr.child.values():
                        if dfs(i+1, node):
                            return True
                    return False
                else:
                    if c in curr.child:
                        curr = curr.child[c]
                    else:
                        return False
            return curr.word
        return dfs(0, self.root)

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordDict = TrieSearch()
        wordDict.add(beginWord)
        res = 1
        visited = []
        numCandidates = 1
        def wordSearch(word):
            w = list(word)
            for index in range(len(w)):
                t = w[index]
                w[index] = "*"
                if wordDict.search("".join(w)):
                    return True
                w[index] = t
            return False

        while numCandidates:
            tempList = []
            for word in wordList:
                if word not in visited and wordSearch(word):
                    if word == endWord:
                        return res+1
                    else:
                        numCandidates += 1
                        tempList.append(word)
                        visited.append(word)
            numCandidates = len(tempList)
            for word in tempList:
                wordDict.add(word)
            res+=1      
        return 0
        


