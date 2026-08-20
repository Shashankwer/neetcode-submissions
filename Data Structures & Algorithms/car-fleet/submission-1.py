class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positions_sorted = sorted([(pos, index) for index, pos in enumerate(position)], reverse=True)
        #print(positions_sorted)
        time_sorted = [(target-pos[0])/speed[pos[1]] for pos in positions_sorted]
        del positions_sorted
        current_top = time_sorted[0]
        groups = 1
        #print(time_sorted)
        for i in range(1, len(time_sorted)):
            if time_sorted[i] > current_top:
                groups+= 1
                current_top = time_sorted[i]
        return groups