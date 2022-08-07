
class GameState():
    def __init__(self):
        self.dim1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.dim2 = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.board = []
        for i in self.dim2:
            for t in self.dim1:
                print(t+i)
                self.board.append(i+t)


state = GameState()

print(state.board[0])

print(next(x for x in state.board if x == 'A1'))

