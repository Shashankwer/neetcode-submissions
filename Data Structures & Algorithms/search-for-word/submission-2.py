class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r,c = len(board),len(board[0])
        word_len = len(word)
        def searchWord(index, x,y):
            if index == word_len:
                return True
            elif x < 0 or y < 0 or x >= r or y >= c:
                return False
            elif board[x][y] != word[index]:
                return False
            else:
                t = board[x][y]
                board[x][y] = "~"
                res = searchWord(index+1, x, y-1) or searchWord(index+1, x-1, y) or searchWord(index+1, x+1, y) or searchWord(index+1, x, y+1)
                board[x][y] = t
                return res
        for row in range(r):
            for col in range(c):
                if searchWord(0,row, col):
                    return True
        return False