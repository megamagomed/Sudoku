
from tkinter import*
from ast import Lambda
import random


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
        self.cell_coordinates = []
        self.yellow_square = []
        self.click_cell = []
        self.changed_task_fields_for_check_in_square = [[],[],[],[],[],[],[],[],[]]
        self.wrong_number = []

    def change_task_field(self):
        for i in range(len(self.task)):
            for j in range(len(self.task)):
                if j <=2 and i<=2:
                    self.changed_task_fields_for_check_in_square[0].append(self.task[i][j])
                if  3<=j<=5 and i<=2:
                    self.changed_task_fields_for_check_in_square[1].append(self.task[i][j])
                if  6<=j<=8 and i<=2:
                    self.changed_task_fields_for_check_in_square[2].append(self.task[i][j]) 
                if j <=2 and 3<=i<=5:
                    self.changed_task_fields_for_check_in_square[3].append(self.task[i][j])  
                if 3<=j<=5 and 3<=i<=5:
                    self.changed_task_fields_for_check_in_square[4].append(self.task[i][j])
                if 6<=j<=8 and 3<=i<=5:
                    self.changed_task_fields_for_check_in_square[5].append(self.task[i][j])
                if j <=2 and 6<=i<=8:
                    self.changed_task_fields_for_check_in_square[6].append(self.task[i][j])
                if 3<=j<=5 and 6<=i<=8:
                    self.changed_task_fields_for_check_in_square[7].append(self.task[i][j]) 
                if 6<=j<=8 and 6<=i<=8:
                    self.changed_task_fields_for_check_in_square[8].append(self.task[i][j])          
                
    def made_field(self):
        self.change_task_field()
        width_of_lines = 1
        summ = 0
        for i in range(10):
            if i==0 or i==3 or i ==6 or i==9:
                width_of_lines = 5
            else:
                width_of_lines = 1
            canvas.create_line(50, self.cell_size*(i+1)+50, self.field_size + 50, self.cell_size*(i+1)+50, fill='blue', width=width_of_lines)
            canvas.create_line(50+self.cell_size*(i), 100, 50+self.cell_size*(i), self.field_size + 100, fill='blue', width=width_of_lines)
        for i in self.task:
            summ +=sum(i)
        if summ == 0:
            canvas.delete("del")
        else:
            for i in range(len(self.task)):
                for j in range(len(self.task)):
                    if self.task[i][j] !=0:
                        text_in_cell = self.task[i][j]
                        canvas.create_text(self.cell_size/2+ self.cell_size*j+50, self.cell_size/2+self.cell_size*i+100, text=text_in_cell, font='Verdana 20', fill = 'green', tag = "del" )        
                    

    def click_event_field(self, event):
        canvas.create_rectangle(50, 100, 500, 550, width = 1, fill = 'white')
        if len(self.wrong_number)>=1:
            canvas.delete(self.wrong_number[0])
            self.wrong_number.pop(0)
        self.cell_coordinates.append(self.change_coords(event.x, event.y))
        cell_coordinates = self.cell_coordinates[len(self.cell_coordinates)-1]
        if 8>=cell_coordinates[0]>=0 and 8>=cell_coordinates[1]>=0:
            self.draw_yellow_square()
            self.vertical_rectangle.append(canvas.create_rectangle(50+self.cell_size*cell_coordinates[1],100,100+self.cell_size*cell_coordinates[1], 550, width = 1, fill = 'yellow'))
            self.horizontal_rectangle.append(canvas.create_rectangle(50, 100+self.cell_size*cell_coordinates[0],500, 150+self.cell_size*cell_coordinates[0], width = 1, fill = 'yellow'))
            self.click_cell.append(canvas.create_rectangle(50+self.cell_size*cell_coordinates[1],100+self.cell_size*cell_coordinates[0],100+self.cell_size*cell_coordinates[1],150+self.cell_size*cell_coordinates[0], width = 1, fill = 'gray'))
            if len(self.vertical_rectangle)>1:
                canvas.delete(self.vertical_rectangle[0])
                self.vertical_rectangle.pop(0)
                canvas.delete(self.horizontal_rectangle[0])
                self.horizontal_rectangle.pop(0)
                canvas.delete(self.yellow_square[0])
                self.yellow_square.pop(0)
                canvas.delete(self.click_cell[0])
                self.click_cell.pop(0)
        self.made_field()    
    
    def draw_yellow_square(self):
        
        cell_coordinates = self.cell_coordinates[len(self.cell_coordinates)-1]
        if cell_coordinates[0] <=2 and cell_coordinates[1]<=2:
            self.yellow_square.append(canvas.create_rectangle(50,100,200, 250, width = 1, fill = 'yellow'))
        if cell_coordinates[0] <=2 and 3<=cell_coordinates[1]<=5:
            self.yellow_square.append(canvas.create_rectangle(200,100,350, 250, width = 1, fill = 'yellow'))
        if cell_coordinates[0] <=2 and cell_coordinates[1] >=6:
            self.yellow_square.append(canvas.create_rectangle(350,100,500, 250, width = 1, fill = 'yellow'))
        if 3<=cell_coordinates[0] <=5 and cell_coordinates[1]<=2:
            self.yellow_square.append(canvas.create_rectangle(50,250,200, 400, width = 1, fill = 'yellow'))
        if 3<=cell_coordinates[0] <=5 and 3<=cell_coordinates[1]<=5:
            self.yellow_square.append(canvas.create_rectangle(200,250,350, 400, width = 1, fill = 'yellow'))       
        if 3<=cell_coordinates[0] <=5 and cell_coordinates[1]>=6:
            self.yellow_square.append(canvas.create_rectangle(350,250,500, 400, width = 1, fill = 'yellow'))
        if cell_coordinates[0] >=6 and cell_coordinates[1]<=2:
            self.yellow_square.append(canvas.create_rectangle(50,400,200, 550, width = 1, fill = 'yellow'))  
        if cell_coordinates[0] >=6 and 3<=cell_coordinates[1]<=5:
            self.yellow_square.append(canvas.create_rectangle(200,400,350, 550, width = 1, fill = 'yellow'))
        if cell_coordinates[0] >=6 and cell_coordinates[1]>=6:
            self.yellow_square.append(canvas.create_rectangle(350,400,500, 550, width = 1, fill = 'yellow'))

    def change_coords(self,x,y):
        row = (y-100)//self.cell_size
        column = (x-50)//self.cell_size
        return row,column
    
    def write_number_in_cell(self, num):
        cell_coordinates = self.cell_coordinates[len(self.cell_coordinates)-1]
        check_value = self.check_entered_value(num)
        if check_value:
            canvas.create_text(self.cell_size/2+ self.cell_size*cell_coordinates[1]+50, self.cell_size/2+self.cell_size*cell_coordinates[0]+100, text=num, font='Verdana 20', fill = 'green', tag = "del" )
            self.task[cell_coordinates[0]][cell_coordinates[1]] = num
            self.change_task_field()
    
    def check_entered_value(self, num):
        self.error_flag =0 
        cell_coordinates = self.cell_coordinates[len(self.cell_coordinates)-1]
        if self.task[cell_coordinates[0]][cell_coordinates[1]] != 0:
            return False
        if num in self.task[cell_coordinates[0]]:
            self.error_flag =1
            canvas.create_rectangle(self.cell_size*(self.task[cell_coordinates[0]]).index(num)+51, self.cell_size*cell_coordinates[0]+101, self.cell_size*(self.task[cell_coordinates[0]]).index(num)+99,self.cell_size*cell_coordinates[0]+149, fill = 'green')
            canvas.create_text(self.cell_size/2+ self.cell_size*(self.task[cell_coordinates[0]]).index(num)+50, self.cell_size/2+self.cell_size*cell_coordinates[0]+100, text=num, font='Verdana 25', fill = 'red', tag = "del" )
            canvas.create_text(self.cell_size/2+ self.cell_size*cell_coordinates[1]+50, self.cell_size/2+self.cell_size*cell_coordinates[0]+100, text=num, font='Verdana 25', fill = 'blue', tag = "del" )
            canvas.create_line(53+self.cell_size*cell_coordinates[1],103+self.cell_size*cell_coordinates[0],99+self.cell_size*cell_coordinates[1],149+self.cell_size*cell_coordinates[0], width = 2, fill = 'red')
            canvas.create_line(53+self.cell_size*cell_coordinates[1],147+self.cell_size*cell_coordinates[0],99+self.cell_size*cell_coordinates[1],101+self.cell_size*cell_coordinates[0], width = 2, fill = 'red')

        for i in range(len(self.task)):
            if self.task[i][cell_coordinates[1]]==num:
                self.error_flag =1
                canvas.create_rectangle(self.cell_size*cell_coordinates[1]+51, self.cell_size*i+101, self.cell_size*cell_coordinates[1]+99,self.cell_size*i+149, fill = 'green')
                self.draw_wrong_number(num, i)
        
        if cell_coordinates[0] <=2 and cell_coordinates[1]<=2 and num in self.changed_task_fields_for_check_in_square[0]:
            self.error_flag =1
            for i in range(3):
                if num in self.task[i] and self.task[i].index(num)<3:
                    canvas.create_rectangle(self.cell_size*self.task[i].index(num)+51, self.cell_size*i+101, self.cell_size*self.task[i].index(num)+99,self.cell_size*i+149, fill = 'green')
                    self.draw_wrong_number(num, i)
                
        if cell_coordinates[0] <=2 and 3<=cell_coordinates[1]<=5 and num in self.changed_task_fields_for_check_in_square[1]:
            self.error_flag =1
            for i in range(3):
                if num in self.task[i] and 5>=self.task[i].index(num)>=3:
                    print("fgsdfgdf")
                    canvas.create_rectangle(self.cell_size*self.task[i].index(num)+51, self.cell_size*i+101, self.cell_size*self.task[i].index(num)+99,self.cell_size*i+149, fill = 'green')
                    self.draw_wrong_number(num, i)

        if cell_coordinates[0] <=2 and cell_coordinates[1] >=6 and num in self.changed_task_fields_for_check_in_square[2]:
            self.error_flag =1
        if 3<=cell_coordinates[0] <=5 and cell_coordinates[1]<=2 and num in self.changed_task_fields_for_check_in_square[3]:
            self.error_flag =1
        if 3<=cell_coordinates[0] <=5 and 3<=cell_coordinates[1]<=5 and num in self.changed_task_fields_for_check_in_square[4]:
            self.error_flag =1    
        if 3<=cell_coordinates[0] <=5 and cell_coordinates[1]>=6 and num in self.changed_task_fields_for_check_in_square[5]:
            self.error_flag =1
        if cell_coordinates[0] >=6 and cell_coordinates[1]<=2 and num in self.changed_task_fields_for_check_in_square[6]:
            self.error_flag =1  
        if cell_coordinates[0] >=6 and 3<=cell_coordinates[1]<=5 and num in self.changed_task_fields_for_check_in_square[7]:
            self.error_flag =1
        if cell_coordinates[0] >=6 and cell_coordinates[1]>=6 and num in self.changed_task_fields_for_check_in_square[8]:
            self.error_flag =1

        if self.error_flag ==1:
            self.wrong_number.append(canvas.create_text(300, 50, text="WRONG NUMBER!!!", font='Verdana 20', fill = 'red', tag = "del" ))
            return False

        return True

    def draw_wrong_number(self, num, i):
        cell_coordinates = self.cell_coordinates[len(self.cell_coordinates)-1]
        canvas.create_text(self.cell_size/2+ self.cell_size*self.task[i].index(num)+50, self.cell_size/2+self.cell_size*i+100, text=num, font='Verdana 25', fill = 'red', tag = "del" )
        canvas.create_text(self.cell_size/2+ self.cell_size*cell_coordinates[1]+50, self.cell_size/2+self.cell_size*cell_coordinates[0]+100, text=num, font='Verdana 25', fill = 'blue', tag = "del" )
        canvas.create_line(53+self.cell_size*cell_coordinates[1],103+self.cell_size*cell_coordinates[0],99+self.cell_size*cell_coordinates[1],149+self.cell_size*cell_coordinates[0], width = 2, fill = 'red')
        canvas.create_line(53+self.cell_size*cell_coordinates[1],147+self.cell_size*cell_coordinates[0],99+self.cell_size*cell_coordinates[1],101+self.cell_size*cell_coordinates[0], width = 2, fill = 'red')

class Click:
    def __init__(self):
        self.clear_flag = 0
        self.field = Field()
    def click_handler(self, event):
            random_arg = 0
            clear_field = Field(spisok_empty)
            if event == "new game":
                clear_field.made_field()
                random_arg = random.randint(0, len(spisok)-1)
                self.field =  Field((spisok[random_arg]))
                self.field.made_field()
                self.clear_flag = 1

            if event == "clear" and self.clear_flag ==1:
                clear_field.made_field()
                self.field.made_field()
            
            if type(event) == int:
                self.field.write_number_in_cell(event)
            
            canvas.bind('<Button-1>', self.field.click_event_field)    

spisok = [[[1,0,0,0,0,0,0,0,3], 
          [0,0,7,2,6,0,4,8,0], 
          [4,0,0,9,3,5,0,0,6],
          [0,3,0,4,8,0,2,0,0],      
          [0,4,1,6,0,9,3,0,0],
          [0,0,6,0,0,0,8,9,0],
          [5,7,8,0,4,0,0,0,2],
          [0,0,0,3,0,0,0,7,0],
          [2,0,0,0,0,0,0,0,5]],
          [[0,9,0,0,0,5,1,0,0], 
          [0,0,5,0,8,7,3,0,4], 
          [4,0,0,1,0,0,5,0,6],
          [0,0,0,0,0,0,0,6,0],      
          [0,0,4,5,0,2,7,0,0],
          [0,3,0,0,0,0,0,0,0],
          [7,0,9,0,0,4,0,0,1],
          [3,0,2,9,5,0,6,0,0],
          [0,0,1,7,0,0,0,2,0]],
          [[1,0,0,0,0,6,0,5,0], 
          [0,0,0,0,0,2,0,0,0], 
          [0,0,0,0,0,0,3,0,2],
          [0,0,0,0,5,1,0,0,0],      
          [6,0,7,2,0,0,0,0,0],
          [0,0,0,0,7,0,0,3,8],
          [8,0,0,1,0,0,0,0,0],
          [0,2,0,8,0,4,9,0,7],
          [3,0,0,0,0,0,0,4,6]],
          [[0,0,0,9,0,0,0,0,1], 
          [0,5,0,0,0,0,6,0,0], 
          [4,0,0,3,0,0,0,0,7],
          [0,8,0,0,0,5,0,0,0],      
          [0,0,1,0,0,0,2,0,0],
          [0,0,0,4,0,0,0,9,0],
          [7,0,0,0,0,1,0,0,8],
          [0,0,9,0,0,0,0,3,0],
          [2,0,0,0,0,7,0,0,0]],
          [[7,0,0,9,0,0,3,4,0], 
          [0,5,0,8,0,6,0,0,0], 
          [0,0,0,0,1,0,0,0,0],
          [0,6,0,0,0,0,0,8,0],      
          [1,0,0,0,3,0,0,0,5],
          [0,0,0,4,0,0,2,0,0],
          [0,0,0,0,2,0,0,9,0],
          [0,0,0,0,0,0,7,0,2],
          [9,0,0,0,7,5,4,0,8]]]

spisok_empty = [[0,0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0,0], 
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],      
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]]

click = Click()
btn_new_game = Button(text="New game", background="#2a7098", foreground="white", font=("Arial", 23, "bold"), command=lambda: click.click_handler("new game"))
btn_new_game.place(x=700, y=100,  height=50, width=450, bordermode=INSIDE)
btn_cancel = Button(text="Cancel", background="#2a7098", foreground="white", font=("Arial", 23, "bold"), command=lambda: click.click_handler("cancel"))
btn_cancel.place(x=700, y=170,  height=50, width=200, bordermode=INSIDE)
btn_clear = Button(text="Clear", background="#2a7098", foreground="white", font=("Arial", 23, "bold"), command=lambda: click.click_handler("clear"))
btn_clear.place(x=950, y=170,  height=50, width=200, bordermode=INSIDE)
btn_1 = Button(text="1", background="#20a3df", foreground="white", font=("Arial", 23, "bold"), command=lambda: click.click_handler(1))
btn_1.place(x=700, y=240,  height=90, width=137, bordermode=INSIDE)
btn_2 = Button(text="2", background="#20a3df", foreground="white", font=("Arial", 23, "bold"), command=lambda: click.click_handler(2))
btn_2.place(x=857, y=240,  height=90, width=137, bordermode=INSIDE)
btn_3 = Button(text="3", background="#20a3df", foreground="white", font=("Arial", 23, "bold"), command=lambda: click.click_handler(3))
btn_3.place(x=1014, y=240,  height=90, width=137, bordermode=INSIDE)
btn_4 = Button(text="4", background="#20a3df", foreground="white", font=("Arial", 23, "bold"), command=lambda: click.click_handler(4))
btn_4.place(x=700, y=350,  height=90, width=137, bordermode=INSIDE)
btn_5 = Button(text="5", background="#20a3df", foreground="white", font=("Arial", 23, "bold"), command=lambda: click.click_handler(5))
btn_5.place(x=857, y=350,  height=90, width=137, bordermode=INSIDE)
btn_6 = Button(text="6", background="#20a3df", foreground="white", font=("Arial", 23, "bold"), command=lambda: click.click_handler(6))
btn_6.place(x=1014, y=350,  height=90, width=137, bordermode=INSIDE)
btn_7 = Button(text="7", background="#20a3df", foreground="white", font=("Arial", 23, "bold"), command=lambda: click.click_handler(7))
btn_7.place(x=700, y=460,  height=90, width=137, bordermode=INSIDE)
btn_8 = Button(text="8", background="#20a3df", foreground="white", font=("Arial", 23, "bold"), command=lambda: click.click_handler(8))
btn_8.place(x=857, y=460,  height=90, width=137, bordermode=INSIDE)
btn_9 = Button(text="9", background="#20a3df", foreground="white", font=("Arial", 23, "bold"), command=lambda: click.click_handler(9))
btn_9.place(x=1014, y=460,  height=90, width=137, bordermode=INSIDE)

root.mainloop()