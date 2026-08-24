class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for operation in operations:
            match operation:
                case "+":
                    if len(result) >= 2:
                        r = result[-1]+result[-2]
                        result.append(r)
                case "C":
                    result.pop(-1)
                case "D":
                    r = 2*result[-1]
                    result.append(r)
                case _:
                    result.append(int(operation))
        return sum(result)