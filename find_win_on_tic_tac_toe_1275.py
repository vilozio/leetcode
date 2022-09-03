from collections import defaultdict


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        moves_count = {
            "A": {
                "row": defaultdict(int),  # {1: 3} 
                "col": defaultdict(int),  # {1: 1, 2: 1}
                "main_diag": 0,           # 1
                "off_diag": 0,            # 1
            },
            "B": {
                "row": defaultdict(int),  # {2: 2}
                "col": defaultdict(int),  # {2: 1, 1: 1}
                "main_diag": 0,           # 1
                "off_diag": 0,            # 0
            },
        }
        for i, move in enumerate(moves):
            if i % 2 == 0:
                player = "A"
            else:
                player = "B"
            moves_count[player]["row"][move[0]] += 1
            if moves_count[player]["row"][move[0]] == 3:
                return player
            moves_count[player]["col"][move[1]] += 1
            if moves_count[player]["col"][move[1]] == 3:
                return player
            if move[0] == move[1]:
                moves_count[player]["main_diag"] += 1
                if moves_count[player]["main_diag"] == 3:
                    return player
            if move[0] + move[1] == 2:
                moves_count[player]["off_diag"] += 1
                if moves_count[player]["off_diag"] == 3:
                    return player
        if len(moves) != 9:
            return "Pending"
        return "Draw"


# [[1, 1], [2, 2], [1, 2], [2, 1], [1, 0]]
