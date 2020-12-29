from tkinter import *
from time import sleep


#примечание для разработчиков - если в пункте TODO в конце написано "checked" пункт выполнен
root = Tk()
root.title('Capricorn: The First Chapter - January')


canvas = Canvas(root, width=600, height=600, bg='LightSkyBlue3')
canvas.pack()
root.resizable(0, 0)


# canvas.create_line(0, 0, 600, 600)

# canvas.create_rectangle(10, 10, 50, 50, fill='greenyellow')


# canvas.create_rectangle(10, 10, 70, 70)
# canvas.create_rectangle(30, 30, 90, 90)
# canvas.create_line(10, 10, 30, 30)
# canvas.create_line(70, 10, 90, 30)
# canvas.create_line(10, 70, 30, 90)
# canvas.create_line(70, 70, 90, 90)

# canvas.create_oval(500, 500, 700, 700)
# canvas.create_text(200, 200, text='La casa de papel', fill='red', activefill='yellow', font='Arial 40')

# from time import sleep
# # circle_1 = canvas.create_oval(10, 10, 50, 50, fill='red')
# # circle_2 = canvas.create_oval(10, 10, 50, 50)


# # for i in range(100):
# # canvas.move(circle_1, 1, 1)
# # root.update()
# # sleep(0.05)


# ghost = canvas.create_polygon(10, 10, 10, 60, 50, 35, fill='red')

# def move_triangle(event):
# if event.keysym == 'Up':
# canvas.move(ghost, 0, -3)
# elif event.keysym == 'Down':
# canvas.move(ghost, 0, 3)
# elif event.keysym == 'Left':
# canvas.move(ghost, -3, 0)
# elif event.keysym == 'Right':
# canvas.move(ghost, 3, 0)

# canvas.bind_all('<KeyPress>', move_triangle)

class Circle:
    '''
    Create a circle
    '''
    def __init__(self):
        self.x = 100
        self.y = 100
        self.size = 115
        self.speed_x = 5
        self.speed_y = 3
        self.canvas_size = 600
        self.object = canvas.create_oval(self.x, self.y, self.size, self.size, fill='gainsboro', outline='gainsboro')

    def move(self):
        '''
        result - a Circle have move
        '''
        canvas.move(self.object, self.speed_x, self.speed_y)
        self.check_collision()
        self.check_collision_with_platform()

    def check_collision(self):
        '''
        functional - check collision with walls
        '''
        #TODO: сделать проверку столкновения с платформой
        pos = canvas.coords(self.object)
        if pos[0] <= 0:
            self.speed_x *= -1
        if pos[1] <= 0:
            self.speed_y *= -1
        if pos[2] >= self.canvas_size:
            self.speed_x *= -1
        if pos[3] >= self.canvas_size:
            self.speed_y *= -1

    def check_collision_with_platform(self):
        pos_platform = p1.getter_coords()
        pos_circle = canvas.coords(self.object)

        if pos_circle[3] >= pos_platform[1] and pos_circle[2] >= pos_platform[0] and pos_circle[0] <= pos_platform[2] and pos_circle[1] <= pos_platform[3]:      #if circle have collision witn platform up - he is got around
            self.speed_y *= -1
        if pos_circle[3] <= pos_platform[3] and pos_circle[1] >= pos_platform[1] and pos_circle[0] >= pos_platform[2]:
            self.speed_x *= -1

    def getter_status(self):
        pos_circle = canvas.coords(self.object)

        if pos_circle[3] >= self.canvas_size:
            canvas.delete(ALL)
            canvas.create_text(300, 300, text="You lose \n thanks for play", justify=CENTER,  font="Helvetica 20")
            return False
        else:
            return True

class Platform():
    def __init__(self):
        self.x = 225
        self.y = 500
        self.size = 15
        self.canvas_size = 600
        self.object = canvas.create_rectangle(self.x, self.y, self.x + self.size*10, self.y + self.size, fill='Salmon4', outline='Salmon4')
        self.canvas = canvas
        self.canvas.bind_all('<KeyPress>', self.move)

    def move(self, event):
        if event.keysym == 'Left':
            canvas.move(self.object, -8, 0)
        elif event.keysym == 'Right':
            canvas.move(self.object, 8, 0)

        self.check_collision()
    
    def check_collision(self):
        #TODO: сделать проверку столкновения платформы со стеной (checked)
        posp = canvas.coords(self.object)            #pos = position, p = platform

        if posp[0] <= 0:
            canvas.move(self.object, 8, 0)
        elif posp[2] >= self.canvas_size:
            canvas.move(self.object, -8, 0)
    
    def getter_coords(self):
        posp = canvas.coords(self.object)
        return posp


class Cubes():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 20
        self.x2 = self.size
        self.y2 = self.size
        self.canvas_size = 600
        self.ratio = self.canvas_size // self.size
        self.canvas = canvas

    def create_cubes(self):
        for c in range(3):
            for r in range(self.ratio):
                self.canvas.create_rectangle(self.x, self.y, self.x2, self.y2, fill='steelblue')
                self.x += self.size
                self.x2 += self.size
            self.x = 0
            self.x2 = self.size
            self.y += self.size
            self.y2 += self.size
                
c1 = Circle()
p1 = Platform()
cube = Cubes()
cube.create_cubes()
while c1.getter_status(): 
    c1.move()
    root.update()
    sleep(0.03)
root.mainloop()