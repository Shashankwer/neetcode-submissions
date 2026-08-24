class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for ast in asteroids:
            if result:
                if result[-1] > 0 and ast>0:
                    result.append(ast)
                elif (result[-1] > 0 and ast >0) or (result[-1] < 0 and ast <0) :
                    result.append(ast)
                elif ast < 0:
                    #print(result)
                    curr = result[-1]
                    while result and curr*ast < 0:
                        if abs(curr) > abs(ast):
                            break
                        elif abs(curr) == abs(ast):
                            result.pop()
                            ast = 0
                            break
                        else:
                            result.pop()
                            if result:
                                curr = result[-1]
                    if abs(ast) > 0 and (not result or curr*ast>0):
                        result.append(ast)
                else:
                    result.append(ast)
            else:
                result.append(ast)
        return result


                    