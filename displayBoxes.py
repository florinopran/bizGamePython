from tkinter import Label

def initializeBoxes(self):

    # LABELS FOR: NEWS, INCOME, SPENDINGS, BALANCE, ADVISER
    self.lnews=Label(text="News:\n", width=34, height=10, background="white", 
                        anchor="nw", justify="left", font=("Segoe UI", 8))
    self.lnews.place(x=20,y=540)
    self.lrevenue=Label(text="Revenue:\n", width=34, height=10, background="white", 
                        foreground="darkgreen",
                        anchor="nw", justify="left", font=("Segoe UI", 8))
    self.lrevenue.place(x=340,y=540)
    self.lexpenditure=Label(text="Expenditure:\n", width=34, height=10, background="white",
                            foreground="red", 
                            anchor="nw", justify="left", font=("Segoe UI", 8))
    self.lexpenditure.place(x=660,y=540)
    self.lbalance=Label(text="Balance:\n", width=63, height=1, 
                        background="darkgreen", foreground="white",
                            anchor="nw", justify="left", font=("Segoe UI", 8, "bold"))
    self.lbalance.place(x=340,y=760)
    self.lAdviserBox=Label(text="", width=42, height=10, 
                        background="white", foreground="darkgreen",
                        highlightbackground="darkgreen",highlightthickness=2,
                            anchor="nw", justify="left", font=("Segoe UI", 8, "bold"))
    self.lAdviserBox.place(x=20,y=310)