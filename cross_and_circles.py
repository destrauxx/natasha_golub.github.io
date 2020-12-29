from tkinter import *
# TODO change import method, to from tkinter import module


# Constants
CANVAS_SIZE = 600
FIGURE_SIZE = CANVAS_SIZE / 3
RATIO = CANVAS_SIZE // FIGURE_SIZE
BG_COLOR = 'black'
EMPTY = None

# Player setup
X = 'player 1'
O = 'player 2'
FIRST_PLAYER = X

class Board(Tk):
    def __init__(self, start_player):
        super().__init__()
        self.canvas = Canvas(height=CANVAS_SIZE, width=CANVAS_SIZE)
        self.canvas.pack()
        self.figure_size = FIGURE_SIZE
        self.current_player = start_player
        self.canvas.bind('<Button-1>', self.click_event)
        self.game_status = True
        self.board = [[EMPTY, EMPTY, EMPTY,],
            [EMPTY, EMPTY, EMPTY,],
            [EMPTY, EMPTY, EMPTY,]]

    def build_grid(self, grid_color):
        '''
        Render on canvas lines - grid
        input: color of grid(str)

        '''
        x = CANVAS_SIZE // RATIO
        y1 = 0
        y2 = CANVAS_SIZE
        for _ in range(2):
            self.canvas.create_line(x, y1, x, y2, fill=grid_color)
            self.canvas.create_line(y1, x, y2, x, fill=grid_color)
            x += CANVAS_SIZE // RATIO


    def render_cross(self, posX, posY):
        '''
        Render cross(X) on grid by coords - posX and posY
        input: posX(int), posY(int) - coords of cross on pole
        '''
        f_size = self.figure_size
        self.canvas.create_line(posX, posY, posX + f_size, posY + f_size, fill='red', width=5)
        self.canvas.create_line(posX + f_size, posY, posX, posY + f_size, fill='red', width=5)

    def render_circle(self, posX, posY):

        '''
        Render circle(O) on grid by coords - posX and posY
        input: posX, posY - coords of circle on pole
        Magic number: 5, its a gap between edges and figure
        '''
        f_size = self.figure_size - 5
        self.canvas.create_oval(posX + 5, posY + 5, posX + f_size, posY + f_size, outline='green', width=5)

    def winner(self, player=None):
        '''Display end game text, depends on player attribute
        and shutdown the game
        input: player(str) who won
        '''
        self.game_status = False
        center = CANVAS_SIZE // 2
        if player:
            text = f'Winner: {player}'
        else:
            text = 'Draw'
        
        self.canvas.create_text(center, center, text=text, fill='white', font='Arial 50')
        self.canvas.unbind('<Button-1>')

    def click_event(self, event):
        '''
        click tracking, launch make_move
        '''
        x_coord = int(event.x // FIGURE_SIZE)
        y_coord = int(event.y // FIGURE_SIZE)
        self.make_move(x_coord, y_coord)

        if self.game_status:
            self.ai_best_move()
    def make_move(self, x, y):
        '''
        If there was a click, render the figure depending on the player at the x y coordinates
        input: x(int) and y(int) coords of click
        '''
        position = {0: 0, 1: 200, 2: 400}

        if self.board[x][y] == EMPTY:
            self.update_board(x, y)
            if self.current_player == X:
                self.render_cross(position[x], position[y])
            elif self.current_player == O:
                self.render_circle(position[x], position[y])
            self.change_player()

    def update_board(self, x, y):
        '''
        If make_move has occurred and there is no figure on the cell - update the grid list
        input: x(int), y(int)
        '''
        c_player = self.current_player
        self.board[x][y] = c_player
        if self.check_win(self.board, c_player):
            self.winner(c_player)
        elif self.check_draw(self.board):
            self.winner()

    def check_win(self, board, player):
        '''
        Check win of player =)
        input: board(list with lists), player(str)
        output: result - win player or not
        '''
        for row in board:
            if row == [player, player, player]:
                return True
            
        for col in range(len(board)):
            if board[0][col]==board[1][col]==board[2][col] == player:
                return True
        
        if board[0][0]==board[1][1]==board[2][2]==player:
            return True

        if board[0][2]==board[1][1]==board[2][0]==player:
            return True
        
        return False
        
    def check_draw(self, board):
        for row in board:
            if EMPTY in row:
                return False
            
        return True

    def change_player(self):
        if self.current_player == X:
            self.current_player = O
        else:
            self.current_player = X
    
    def minimax(self, board, isMax):
        board_len = range(len(self.board))

        if self.check_win(board, O):
            return 1
        elif self.check_win(board, X):
            return -1
        elif self.check_draw(board):
            return 0

        if isMax:
            best_score = float('-inf')
            for i in board_len:
                for j in board_len:
                    if board[i][j] == EMPTY:
                        board[i][j] = O
                        score = self.minimax(board, False)
                        board[i][j] = EMPTY
                        best_score = max(score, best_score)
        else:
            best_score = float('inf')
            for i in board_len:
                for j in board_len:
                    if board[i][j] == EMPTY:
                        board[i][j] = X
                        score = self.minimax(board, True)
                        board[i][j] = EMPTY
                        best_score = min(score, best_score)
        return best_score

    def ai_best_move(self):
        best_score = float('-inf')
        board_len = range(len(self.board))
        board = self.board[:]
        for i in board_len:
            for j in board_len:
                if board[i][j] == EMPTY:
                    board[i][j] = O
                    score = self.minimax(board, False)
                    board[i][j] = EMPTY
                    if score > best_score:
                        best_score = score
                        move = i, j

        self.make_move(move[0], move[1])
# Initialize game object and execute require methods
game_v1 = Board(start_player=FIRST_PLAYER)
game_v1.build_grid(BG_COLOR)

# Testing
# game_v1.winner('Test')

# Run the game
game_v1.mainloop()