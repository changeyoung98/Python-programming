#interface.py

from grid import*
from tkMessageBox import*

class Interface:
    #the interface of Sudoku game,
    #and you can choose the difficulty-simple, normal, hard.
    def __init__(self):
        "The initial interface"
        self.tk = Tk(className = "sudoku")
        self.c = Canvas(self.tk, width = 460, height = 400)
        self._c = Canvas(self.tk, width = 460, height = 400)
        self.grid = Grid(self.tk, self._c)

        helpText = """To fill the 9x9 grid with digits so that
each column, each row, and each of
the nine 3x3 sub-grids that compose
the grid contains all of the digits
from 1 to 9.
At the beginning, you can choose the
difficulty.
In the game, you can click 'restart' to
start a new game, or you can click
'return' to return the start interface.
When you fill all the grid, you can click
'check' to check if the Answer is right.
Or you can click 'answer' to show the
answer."""
        self.text = Label(self.tk, text = helpText, anchor = W, justify = LEFT, font = "arial 14")
        
        self.start = Button(self.tk, bd = 5, cursor = 'hand2', text = "start", font = "arial 18", command = self.startGame)
        self.help = Button(self.tk, bd = 5, cursor = 'hand2', text = "Help", font = "arial 18", command = self.showHelp)
        self.exit = Button(self.tk, bd = 5, cursor = 'hand2', text = "Exit", font = "arial 18", command = self._exit)

        self.restart = Button(self.tk, bd = 5, cursor = 'hand2', font = "arial 18", text = "Restart")
        self.restart.bind("<Button-1>", self.showGame)
        self._return = Button(self.tk, bd = 5, cursor = 'hand2', font = "arial 18", text = "Return", command = self._returnB)
        
        self.simple = Button(self.tk, bd = 5, cursor = 'hand2', font = "arial 18", text = "simple")
        self.normal = Button(self.tk, bd = 5, cursor = 'hand2', font = "arial 18", text = "normal")
        self.hard = Button(self.tk, bd = 5, cursor = 'hand2', font = "arial 18", text = "hard")
        self.simple.bind("<Button-1>", self.showGame)
        self.normal.bind("<Button-1>", self.showGame)
        self.hard.bind("<Button-1>", self.showGame)
        
        self.check = Button(self.tk, bd = 5, cursor = 'hand2', font = "arial 18", text = "Check", command = self.checkAnswer)
        self.answer = Button(self.tk, bd = 5, cursor = 'hand2', font = "arial 18", text = "Answer", command = self.showAnswer)

        self.c.pack()
        self.start.place(width = 100, height = 50, x = 175, y = 75)
        self.help.place(width = 100, height = 50, x = 175, y = 175)
        self.exit.place(width = 100, height = 50, x = 175, y = 275)
        self.tk.mainloop()

    def startGame(self):
        "show the difficluties for user to choose"
        self.start.place_forget()
        self.help.place_forget()
        self.exit.place_forget()
        self._return.place(width = 100, height = 50, x = 15, y = 250)
        self.simple.place(width = 100, height = 50, x = 175, y = 75)
        self.normal.place(width = 100, height = 50, x = 175, y = 175)
        self.hard.place(width = 100, height = 50, x = 175, y = 275)

    def showHelp(self):
        "show the help text"
        self.start.place_forget()
        self.help.place_forget()
        self.exit.place_forget()
        self._return.place(width = 100, height = 50, x = 15, y = 250)
        self.text.place(width = 325, height = 300, x = 125, y = 50)

    def _exit(self):
        "exit the game"
        self.tk.destroy()

    def _returnB(self):
        "return to the initial interface"
        self.start.place(width = 100, height = 50, x = 175, y = 75)
        self.help.place(width = 100, height = 50, x = 175, y = 175)
        self.exit.place(width = 100, height = 50, x = 175, y = 275)
        self.c.pack()
        self.simple.place_forget()
        self.normal.place_forget()
        self.hard.place_forget()
        self.text.place_forget()
        self._return.place_forget()
        self.grid.pack_forget()
        self.check.place_forget()
        self.restart.place_forget()
        self.answer.place_forget()
        self.check['state'] = 'normal'

    def showGame(self, event):
        "start a game"
        t = event.widget["text"]
        if t == "simple":
            self.grid.setDifficulty(1)
        elif t == "normal":
            self.grid.setDifficulty(2)
        elif t == "hard":
            self.grid.setDifficulty(3)
        self._return.place(width = 100, height = 50, x = 15, y = 250)
        self.restart.place(width = 100, height = 50, x = 15, y = 150)
        self.simple.place_forget()
        self.normal.place_forget()
        self.hard.place_forget()
        self.c.pack_forget()
        self.grid.pack_forget()
        self.grid.showGame()
        self.check.place(width = 100, height = 50, x = 175, y = 325)
        self.answer.place(width = 100, height = 50, x = 300, y = 325)
        self.check['state'] = 'normal'

    def checkAnswer(self):
        "check if the answer is right"
        if self.grid.checkAnswer():
            showinfo("Congratulations!", "Congratulations!")
            self._returnB()
        else:
            showinfo("Sorry!", "It's wrong!")

    def showAnswer(self):
        "show the answer"
        self.grid.showAnswer()
        self.check['state'] = 'disabled'
                         
i = Interface()
