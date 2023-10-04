from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
# root.config(bg = "cadet blue",cursor = "dotbox")
# root.geometry("303x305")
root.resizable(FALSE, FALSE)
bclick = True
def ttt(buttons) :
    global bclick
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        
    elif(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
        button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
        button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or  
        button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or  
        button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
        button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
        button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
        messagebox.showinfo("Winner Is X", "Player X wins")
        root.destroy()
        import tic_tac_toe
    elif(button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
        button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
        button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or  
        button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or  
        button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
        button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
        button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
        button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
        messagebox.showinfo("Winner Is O", "Player O wins") 
        root.destroy()
        import tic_tac_toe 
    else:
        messagebox.showinfo("Draw", "The Game is Draw 👏") 
        root.destroy()
        import tic_tac_toe     

buttons = StringVar()
button1 = Button(root, text = " ", bg = "cadet blue",cursor = "dotbox",fg = "white",font = ("Rockwell", 10, "bold"),command = lambda: ttt(button1),width = 13,height = 6, relief = GROOVE)
button1.grid(row = 1, column = 0, sticky = S+N+E+W)
button2 = Button(root, text = " ", bg = "cadet blue",cursor = "dotbox",fg = "white",font = ("Rockwell", 10, "bold"),command = lambda: ttt(button2),width = 13,height = 6, relief = GROOVE)
button2.grid(row = 1, column = 1, sticky = S+N+E+W)
button3 = Button(root, text = " ", bg = "cadet blue",cursor = "dotbox",fg = "white",font = ("Rockwell", 10, "bold"),command = lambda: ttt(button3),width = 13,height = 6, relief = GROOVE)
button3.grid(row = 1, column = 2, sticky = S+N+E+W)
button4 = Button(root, text = " ", bg = "cadet blue",cursor = "dotbox",fg = "white",font = ("Rockwell", 10, "bold"),command = lambda: ttt(button4),width = 13,height = 6, relief = GROOVE)
button4.grid(row = 2, column = 0, sticky = S+N+E+W)
button5 = Button(root, text = " ", bg = "cadet blue",cursor = "dotbox",fg = "white",font = ("Rockwell", 10, "bold"),command = lambda: ttt(button5),width = 13,height = 6, relief = GROOVE)
button5.grid(row = 2, column = 1, sticky = S+N+E+W)
button6 = Button(root, text = " ", bg = "cadet blue",cursor = "dotbox",fg = "white",font = ("Rockwell", 10, "bold"),command = lambda: ttt(button6),width = 13,height = 6, relief = GROOVE)
button6.grid(row = 2, column = 2, sticky = S+N+E+W)
button7 = Button(root, text = " ", bg = "cadet blue",cursor = "dotbox",fg = "white",font = ("Rockwell", 10, "bold"),command = lambda: ttt(button7),width = 13,height = 6, relief = GROOVE)
button7.grid(row = 3, column = 0, sticky = S+N+E+W)
button8 = Button(root, text = " ", bg = "cadet blue",cursor = "dotbox",fg = "white",font = ("Rockwell", 10, "bold"),command = lambda: ttt(button8),width = 13,height = 6, relief = GROOVE)
button8.grid(row = 3, column = 1, sticky = S+N+E+W)
button9 = Button(root, text = " ", bg = "cadet blue",cursor = "dotbox",fg = "white",font = ("Rockwell", 10, "bold"),command = lambda: ttt(button9),width = 13,height = 6, relief = GROOVE)
button9.grid(row = 3, column = 2, sticky = S+N+E+W)
root.mainloop()
