from tkinter import*
from ast import Lambda

root =Tk()
root.title('SUDOKU')
canv_size = 600
canvas = Canvas(root, width=canv_size*2, height=canv_size)
canvas.pack()
canvas.create_line(canv_size,5, canv_size, canv_size-5, fill = '#3f8023', width=5)
canvas.create_rectangle(5,5, canv_size*2-5, canv_size-5,outline="#3f8023", width=5)



class Field:
    def __init__(self, task=None):
        self.task = task
        self.field_size = 450
        self.cell_size = 50
        self.vertical_rectangle =[]
        self.horizontal_rectangle = []
    def made_field(self):
        width_of_lines = 1
        
        for i in range(10):
            if i==0 or i==3 or i ==6 or i==9:
                width_of_lines = 5
            else:
                width_of_lines = 1
            canvas.create_line(50, self.cell_size*(i+1)+50, self.field_size + 50, self.cell_size*(i+1)+50, fill='blue', width=width_of_lines)
            canvas.create_line(50+self.cell_size*(i), 100, 50+self.cell_size*(i), self.field_size + 100, fill='blue', width=width_of_lines)
        
        for i in range(len(self.task)):
            for j in range(len(self.task)):
                if self.task[i][j] !=0:
                    canvas.create_text(self.cell_size/2+ self.cell_size*j+50, self.cell_size/2+self.cell_size*i+100, text=self.task[i][j], font='Verdana 20', fill = 'green')

    def click_event_field(self, event):
        cell_coordinates = self.change_coords(event.x, event.y)
        self.vertical_rectangle.append(canvas.create_rectangle(50+self.cell_size*cell_coordinates[1],100,100+self.cell_size*cell_coordinates[1], 550, outline = 'red', width = 2))
        self.horizontal_rectangle.append(canvas.create_rectangle(50, 100+self.cell_size*cell_coordinates[0],500, 150+self.cell_size*cell_coordinates[0], outline = 'red',width = 2))
        if len(self.vertical_rectangle)>1:
            canvas.delete(self.vertical_rectangle[0])
            self.vertical_rectangle.pop(0)
            canvas.delete(self.horizontal_rectangle[0])
            self.horizontal_rectangle.pop(0)
        print(self.vertical_rectangle)
        print(cell_coordinates)
    
    def change_coords(self,x,y):
        row = (y-100)//self.cell_size
        column = (x-50)//self.cell_size
        return row,column


spisok = [[1,0,0,0,0,0,0,0,3], 
          [0,0,7,2,6,0,4,8,0], 
          [4,0,0,9,3,5,0,0,6],
          [0,3,0,4,8,0,2,0,0],      
          [0,4,1,6,0,9,3,0,0],
          [0,0,6,0,0,0,8,9,0],
          [5,7,8,0,4,0,0,0,2],
          [0,0,0,3,0,0,0,7,0],
          [2,0,0,0,0,0,0,0,5]]

field = Field(spisok)
field.made_field()
canvas.bind('<Button-1>', field.click_event_field)


# if len(spisok) !=9:
#     print('rukogop')
# for i in range(len(spisok)):
#     if len(spisok[i]) != 9:
#         print('rukogop')

# def check_digit(spisok, row, column, arg):
#     square_row = row // 3
#     square_column = column // 3
#     for i in range(square_row*3, square_row*3+3):
#         for j in range(square_column*3, square_column*3+3):
#             if arg == spisok[i][j]:
#                 return False
    
#     if arg in spisok[row]:
#         return False

#     for i in range(len(spisok)):
#         if spisok[i][column]==arg:
#             return False
    



# print(check_digit(spisok, 5, 0, 2))

# check_digit(spisok, 0, 8, 1)
# check_digit(spisok, 6, 2, 1)



btn_new_game = Button(text="New game", background="#2a7098", foreground="white", font=("Arial", 23, "bold"))
btn_new_game.place(x=700, y=100,  height=50, width=450, bordermode=INSIDE)
btn_cancel = Button(text="Cancel", background="#2a7098", foreground="white", font=("Arial", 23, "bold"))
btn_cancel.place(x=700, y=170,  height=50, width=200, bordermode=INSIDE)
btn_clear = Button(text="Clear", background="#2a7098", foreground="white", font=("Arial", 23, "bold"))
btn_clear.place(x=950, y=170,  height=50, width=200, bordermode=INSIDE)
btn_1 = Button(text="1", background="#20a3df", foreground="white", font=("Arial", 23, "bold"))
btn_1.place(x=700, y=240,  height=90, width=137, bordermode=INSIDE)
btn_2 = Button(text="2", background="#20a3df", foreground="white", font=("Arial", 23, "bold"))
btn_2.place(x=857, y=240,  height=90, width=137, bordermode=INSIDE)
btn_3 = Button(text="3", background="#20a3df", foreground="white", font=("Arial", 23, "bold"))
btn_3.place(x=1014, y=240,  height=90, width=137, bordermode=INSIDE)
btn_4 = Button(text="4", background="#20a3df", foreground="white", font=("Arial", 23, "bold"))
btn_4.place(x=700, y=350,  height=90, width=137, bordermode=INSIDE)
btn_5 = Button(text="5", background="#20a3df", foreground="white", font=("Arial", 23, "bold"))
btn_5.place(x=857, y=350,  height=90, width=137, bordermode=INSIDE)
btn_6 = Button(text="6", background="#20a3df", foreground="white", font=("Arial", 23, "bold"))
btn_6.place(x=1014, y=350,  height=90, width=137, bordermode=INSIDE)
btn_7 = Button(text="7", background="#20a3df", foreground="white", font=("Arial", 23, "bold"))
btn_7.place(x=700, y=460,  height=90, width=137, bordermode=INSIDE)
btn_8 = Button(text="8", background="#20a3df", foreground="white", font=("Arial", 23, "bold"))
btn_8.place(x=857, y=460,  height=90, width=137, bordermode=INSIDE)
btn_9 = Button(text="9", background="#20a3df", foreground="white", font=("Arial", 23, "bold"))
btn_9.place(x=1014, y=460,  height=90, width=137, bordermode=INSIDE)

root.mainloop()