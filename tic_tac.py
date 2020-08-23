from tkinter import *

root = Tk()
root.title("Tic-Tac Game")
root.geometry("350x450")
root.resizable(0,0)
c = 0
def main():
    y = StringVar()
    
    def check():
        if(b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X"):
            y.set("Player_1 Winner!!!")
            return
        elif(b1["text"]=="0" and b2["text"]=="0" and b3["text"]=="0"):
            y.set("Player_2 Winner!!!")
            return
        elif(b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X"):
            y.set("Player_1 Winner!!!")
            return
        elif(b4["text"]=="0" and b5["text"]=="0" and b6["text"]=="0"):
            y.set("Player_2 Winner!!!")
            return
        elif(b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X"):
            y.set("Player_1 Winner!!!")
            return
        elif(b7["text"]=="0" and b8["text"]=="0" and b9["text"]=="0"):
            y.set("Player_2 Winner!!!")
            return
        elif(b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X"):
            y.set("Player_1 Winner!!!")
            return
        elif(b1["text"]=="0" and b4["text"]=="0" and b7["text"]=="0"):
            y.set("Player_2 Winner!!!")
            return
        elif(b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X"):
            y.set("Player_1 Winner!!!")
            return
        elif(b2["text"]=="0" and b5["text"]=="0" and b8["text"]=="0"):
            y.set("Player_2 Winner!!!")
            return
        elif(b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X"):
            y.set("Player_1 Winner!!!")
            return
        elif(b3["text"]=="0" and b6["text"]=="0" and b9["text"]=="0"):
            y.set("Player_2 Winner!!!")
            return
        elif(b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X"):
            y.set("Player_1 Winner!!!")
            return
        elif(b1["text"]=="0" and b5["text"]=="0" and b9["text"]=="0"):
            y.set("Player_2 Winner!!!")
            return
        elif(b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X"):
            y.set("Player_1 Winner!!!")
            return
        elif(b3["text"]=="0" and b5["text"]=="0" and b7["text"]=="0"):
            y.set("Player_2 Winner!!!")
            return
        elif c == 9:
            y.set("Game over!!!")


    def show(b):
        global c
        c += 1
        if c%2==0:
            if b["text"] == "":
                b["text"] = "0"
            else:
                c -= 1
        else:
            if b["text"] == "":
                b["text"] = "X"
                b["bg"] = "red"
            else:
                c -= 1
        ck = check()
        

        

    b1 = Button(root,text="",width=10,height=5,font=("Arial",15),command = lambda:show(b1))
    b1.grid(row=0,column=0,sticky = W)
    b2 = Button(root,text="",width=10,height=5,font=("Arial",15),command = lambda:show(b2))
    b2.grid(row=0,column=1,sticky = W)
    b3 = Button(root,text="",width=10,height=5,font=("Arial",15),command = lambda:show(b3))
    b3.grid(row=0,column=2,sticky = W)
    b4 = Button(root,text="",width=10,height=5,font=("Arial",15),command = lambda:show(b4))
    b4.grid(row=1,column=0,sticky = W)
    b5 = Button(root,text="",width=10,height=5,font=("Arial",15),command = lambda:show(b5))
    b5.grid(row=1,column=1,sticky = W)
    b6 = Button(root,text="",width=10,height=5,font=("Arial",15),command = lambda:show(b6))
    b6.grid(row=1,column=2,sticky = W)
    b7 = Button(root,text="",width=10,height=5,font=("Arial",15),command = lambda:show(b7))
    b7.grid(row=2,column=0,sticky = W)
    b8 = Button(root,text="",width=10,height=5,font=("Arial",15),command = lambda:show(b8))
    b8.grid(row=2,column=1,sticky = W)
    b9 = Button(root,text="",width=10,height=5,font=("Arial",15),command = lambda:show(b9))
    b9.grid(row=2,column=2,sticky = W)
    b10 = Button(root,text="New Game",width=8,height=1,font=("Arial",10),command = main)
    b10.grid(row=3,column=0,columnspan=1,sticky = W)
    b11 = Button(root,text="Exit",width=8,height=1,font=("Arial",10),command = root.destroy)
    b11.grid(row=3,column=0,columnspan=18,sticky = E)
    e1 = Entry(root,font=("Arial"),textvariable = y)
    e1.grid(row=3,column = 0,columnspan =6)
    
   
main()

root.mainloop()