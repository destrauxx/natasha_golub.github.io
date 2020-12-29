from tkinter import *
# TODO change import method, to from tkinter import module


# Constants
CANVAS_SIZE = 600
FIGURE_SIZE = CANVAS_SIZE / 3
RATIO = CANVAS_SIZE // FIGURE_SIZE
BG_COLOR = 'black'
EMPTY = None

# Player setup
x = 'player 1'
o = 'player 2'
FIRST_PLAYER = x

class Board(Tk):
    def __init__(self, start_player):
        super().__init__()
        self.canvas = Canvas(height=CANVAS_SIZE, width=CANVAS_SIZE)
        self.canvas.pack()
        self.figure_size = FIGURE_SIZE
        self.current_player = start_player
        self.canvas.bind('<Button-1>', self.click_event)
        self.board = [[EMPTY, EMPTY, EMPTY,],
            [EMPTY, EMPTY, EMPTY,],
            [EMPTY, EMPTY, EMPTY,]]

    def build_grid(self, grid_color):
        x = CANVAS_SIZE // RATIO
        y1 = 0
        y2 = CANVAS_SIZE
        for _ in range(2):
            self.canvas.create_line(x, y1, x, y2, fill=grid_color)
            self.canvas.create_line(y1, x, y2, x, fill=grid_color)
            x += CANVAS_SIZE // RATIO


    def render_cross(self, posX, posY):
        f_size = self.figure_size
        self.canvas.create_line(posX, posY, posX + f_size, posY + f_size, fill='red', width=5)
        self.canvas.create_line(posX + f_size, posX, posY, posY + f_size, fill='red', width=5)

    def render_circle(self, posX, posY):
        '''Magic number: 5, its a gap between edges and figure
        Render o on field
        '''
        f_size = self.figure_size - 5
        self.canvas.create_oval(posX + 5, posY + 5, posX + f_size, posY + f_size, outline='green', width=5)

    def winner(self, player=None):
        '''Display end game text, depends on player attribute
        and shutdown the game
        '''
        center = CANVAS_SIZE // 2
        if player:
            text = f'Winner: {player}'
        else:
            text = 'Draw'
        
        self.canvas.create_text(center, center, text=text, fill='white', font='Arial 50')
        self.canvas.unbind('<Button-1>')

    def click_event(self, event):
        x_coord = int(event.x // FIGURE_SIZE)
        y_coord = int(event.y // FIGURE_SIZE)
        self.make_move(x_coord, y_coord)
    def make_move(self, x, y):
        position = {0: 0, 1: 200, 2: 400}

        if self.board[x][y] == EMPTY:
            self.update_board(y, x)

    def update_board(self, x, y):
        c_player = self.current_player
        self.board[x][y] = c_player
        if self.check_win(self.board, c_player):
            self.winner(c_player)
        elif self.check_draw(self.board):
            self.winner()

    def check_win(self, board, player):
        
        for row in board:
            if row == [player, player, player]:
                return True
            
        for col in range(len(board)):
            if board[0][col]==board[1][col]==board[2][col] == player:
                return True
        
        if board[0][0]==board[1][1]==board[2][2]==player:
            return True

        # if board[0][2]==board[1][1]==board[2][0]==player:
        
        print(board)
        
    def check_draw(self, board):
        pass
# Initialize game object and execute require methods
game_v1 = Board(start_player=FIRST_PLAYER)
game_v1.build_grid(BG_COLOR)

# Testing
# game_v1.winner('Test')

# Run the game
game_v1.mainloop()