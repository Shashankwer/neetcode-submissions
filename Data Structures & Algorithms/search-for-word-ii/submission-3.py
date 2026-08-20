class TrieNode:
    def __init__(self):
        self.children = {}
        self.ref = 0
        self.index = -1
    
    def addWord(self, word, i):
        curr = self
        curr.ref += 1
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.ref += 1
        curr.index = i

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        res = []
        for index, word in enumerate(words):
            root.addWord(word, index)
        ROWS, COLS = len(board), len(board[0])
        def search(r, c, node):
            # Search for the trie node here
            # Base case
            if r < 0 or c< 0 or r >= ROWS or c >= COLS or board[r][c] == '*' or node is None:
                return
            tmp = board[r][c]
            if node.children.get(tmp, None) is None:
                return
            board[r][c] = '*'
            prev = node
            node = node.children.get(tmp)
            if node.index != -1:
                res.append(words[node.index])
                node.index = -1
                node.ref -= 1
                if not node.ref:
                    prev.children.pop(tmp)
                    node = None
                    board[r][c] = tmp
                    return
            search(r+1, c, node)
            search(r-1, c, node)
            search(r, c+1, node)
            search(r , c-1, node)
            board[r][c] = tmp
        for r in range(ROWS):
            for c in range(COLS):
                search(r,c, root)
        return res


        