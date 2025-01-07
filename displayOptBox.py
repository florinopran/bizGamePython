from tkinter import *
# from optBox import *


def initializeOptBox(self):
    # Not yet activated. It's activated from optBox
    self.boptYes = Button(text="Yes", width=8, font=("Segoe UI", 8))
    self.boptYes.place_forget()
    # self.boptYes.place(x=460, y=428)
    
    # Not yet activated. It's activated from optBox
    self.boptNo = Button(text="No", width=8, font=("Segoe UI", 8))
    self.boptNo.place_forget()
    # self.boptNo.place(x=460, y=468)


    # ENTRY DATA as an ANSWEAR TO ADVISERS
    # Create an Entry widget for user input
    self.bentry = Entry(width=8, font=("Segoe UI", 8), text="")
    self.bentry.place_forget()
    # self.bentry.place(x=460, y=428)

    # Create a Button to submit data
    self.submit_bentry = Button(text="Submit", command=submit_data)
    self.submit_bentry.place_forget()
    # self.submit_bentry.place(x=460, y=468)

# def activateYesNo(self, action):
#     hideYesNoEntry(self)
#     # self.opt=None
#     # action is the function from personal.py / biz.py eg.
#     self.boptYes.config(command=lambda: action(self,"yes")) 
#     self.boptNo.config(command=lambda: action(self,"no"))
#     self.boptYes.place(x=460, y=428)
#     self.boptNo.place(x=460, y=468)

# def activateOk(self, action):
#     hideYesNoEntry(self)
#     # self.opt=None
#     # action is the function from personal.py / biz.py eg.
#     self.boptYes.config(text="OK", command=lambda: action(self, "ok")) 
#     # self.boptNo.config(command=lambda: action(self,"no"))
#     self.boptYes.place(x=460, y=428)
#     # self.boptNo.place(x=460, y=468)



# def activateEntry (self, action):
#     hideYesNoEntry(self)
#     # Make the Entry widget visible
#     self.bentry.place(x=460, y=428)
    
#     # Bind the <Return> key to trigger the action
#     self.bentry.bind("<Return>", lambda event: action(self, self.bentry.get()))
    
#     # Configure the Submit button to trigger the action
#     self.submit_bentry.config(command=lambda: action(self, self.bentry.get()))
#     self.submit_bentry.place(x=460, y=468)
    


# def hideYesNoEntry(self):
#     self.boptYes.place_forget()
#     self.boptNo.place_forget()
#     self.bentry.place_forget()
#     self.submit_bentry.place_forget()



def submit_data(self):
    self.opt=self.bentry.get()
    print(self.opt)



def activateYesNo(game, action):
    hideYesNoEntry(game)
    # game.opt=None
    # action is the function from personal.py / biz.py eg.
    game.boptYes.config(command=lambda: action(game,"yes")) 
    game.boptNo.config(command=lambda: action(game,"no"))
    game.boptYes.place(x=460, y=428)
    game.boptNo.place(x=460, y=468)

def activateOk(game, action):
    hideYesNoEntry(game)
    # game.opt=None
    # action is the function from personal.py / biz.py eg.
    game.boptYes.config(text="OK", command=lambda: action(game, "ok")) 
    # game.boptNo.config(command=lambda: action(game,"no"))
    game.boptYes.place(x=460, y=428)    
    # game.boptNo.place(x=460, y=468)



def activateEntry (game, action):
    hideYesNoEntry(game)
    # Make the Entry widget visible
    game.bentry.place(x=460, y=428)
    
    # Bind the <Return> key to trigger the action
    game.bentry.bind("<Return>", lambda event: action(game, game.bentry.get()))
    
    # Configure the Submit button to trigger the action
    game.submit_bentry.config(command=lambda: action(game, game.bentry.get()))
    game.submit_bentry.place(x=460, y=468)
    


def hideYesNoEntry(game):
    game.boptYes.place_forget()
    game.boptNo.place_forget()
    game.bentry.place_forget()
    game.submit_bentry.place_forget()
    game.bentry.delete(0, END)


def submit_data(game):
    game.opt=game.bentry.get()
    print(game.opt)





