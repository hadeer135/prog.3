import tkinter as tk
import threading 
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root=tk.Tk()                                   
        self.root.title("TicTacToe")
        self.current_player="X"
        self.board=[[" " for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                button=tk.Button(self.root ," ", width=10,height=5,command=lambda i=i,j=j:self.make_move(i,j))
                button.grid(row=i,column=j)

                self.lock=threading.Lock()

    def make_move(self,i,j):
        with self.lock:
            if self.board[i][j]==" " :
                self.board[i][j]=self.current_player
                if self.check_winner():
                    messagebox.showinfo("Winner is : " f" player {self.current_player}")
                    self.reset_board()

                else:
                    if all(all(cell != " " for cell in row ) for row in self.board):
                        messagebox.showinfo(" it is a draw ")
                        self.reset_board() 
                    else:
                        self.current_player="O" if self.current_player=="X" else "X"

    def check_winner(self):
        for row in self.board:
            if all( cell==row[0] and cell !=" " for cell in row):
                return True
            
        for j in range(3):
            if all(self.board[i][j] == self.board[0][j] and self.board !=" " for i in range(3)):
                return True
            
        if all(self.board[i][j]==self.board[0][0] and self.board[i][j] != " " for i in range(3)):
            return True
        if all(self.board[i][2-i]==self.board[0][2] and self.board[i][2-i] != " " for i in range(3)):
            return True
        return False
    
    def reset_board(self):
        with self.lock:
            for i in range(3):
                for j in range(3):
                    button=tk.Button(self.root, text=" ", width=10,height=5,command=lambda i=i,j=j:threading.Thread(target=self.make_move,args=(i,j).start()))
                    button.grid(row=i,column=j)

            self.current_player="X"
            self.board=[[" " for _ in range(3) for _ in range (3)]]

    def run(self):
        threading.Thread(target=self.board.mainloop().start())


if __name__ =="__main__":
    game=TicTacToe()
    game.run()

                

