from time import *
import random
from tkinter import *
from tkinter import ttk

root = Tk()    
cell_x = 0
cell_y = 0
cells_x = []
cells_y = [] 
head = 0
apple = 0
snake = []
snake_coords_y = []
snake_coords_x = []
t = 1

root.title("Приложение на Tkinter")   
root.geometry("500x500")  
canvas = Canvas(root,width=500,height=500,bg="black",cursor="pencil")
canvas.pack()

def create_squares():
    cell_x = 0
    cell_y = 0
    for i in range(25):
        for i in range(25):
            cells_x.append(cell_x)
            cells_y.append(cell_y)
            cell_x = cell_x + 20
        cell_x = 0
        cell_y = cell_y + 20

create_squares()

rand_x = random.randint(0, len(cells_x) - 1)
rand_y = random.randint(0, len(cells_y) - 1)

def create_head(head_x, head_y):
    global canvas
    head = canvas.create_rectangle(head_x, head_y, head_x + 20, head_y + 20, fill="green", outline="black")
    return head

def create_apple(rand_x, rand_y):
    apple = canvas.create_rectangle(cells_x[rand_x], cells_y[rand_y], cells_x[rand_x] + 20, cells_y[rand_y] + 20, fill="red", outline="black")
    return apple

snake.append(create_head(240, 240))
apple = create_apple(rand_x, rand_y)

def move_snake(event, x, y):

    global snake
    global apple
    global rand_x
    global rand_y
    global snake_coords_x
    global snake_coords_y
    global t


    last = canvas.coords(snake[0])
    print(len(snake))
    canvas.move(snake[0], x, y)
    head_x = canvas.coords(snake[0])[0]
    head_y = canvas.coords(snake[0])[1]
    canvas.delete("all")
    
    create_squares()
    i = 1
    for i in range(0, len(snake_coords_x)):
        snake[len(snake) - 1] = (create_head(snake_coords_x[i], snake_coords_y[i]))

    apple = create_apple(rand_x, rand_y)
    snake[0] = create_head(head_x, head_y)
    # snake[1] = create_head(last[0], last[1])
    t = t + 1
    if canvas.coords(apple) == canvas.coords(snake[0]):
        canvas.delete(apple)
        rand_y = random.randint(0, len(cells_y) - 1)
        rand_x = random.randint(0, len(cells_x) - 1)
        apple = create_apple(rand_x, rand_y)
        snake_coords_x.append(last[0])
        snake_coords_y.append(last[1])
        snake.append(create_head(snake_coords_x[len(snake_coords_x)-1], snake_coords_y[len(snake_coords_y)-1]))



root.update()
canvas.bind_all("<KeyPress-Up>", lambda event: move_snake(event, 0, -20))
canvas.bind_all("<KeyPress-Down>", lambda event: move_snake(event, 0, 20))
canvas.bind_all("<KeyPress-Left>", lambda event: move_snake(event, -20, 0))
canvas.bind_all("<KeyPress-Right>", lambda event: move_snake(event, 20, 0))

root.mainloop()