#TODO bug = banca iti poate da in mod repetat credit la maximul admis
from display import *
from tkinter import messagebox, simpledialog
from displayOptBox import *


# CREDIT (BANK)
def do_bcredit(game):
    game.lAdviser.config(image=game.imgBankAdviser)    
    maxim=max(3 * (game.netWorth),100)
    message=("Finance Adviser:\n"
            f"Bank will grant you a max credit of ${maxim:.2f}.\n"
            f"How much do you need from the bank?")      
    game.lAdviserBox.config(text=message)  
    def actionCredit(game,value):
        hideYesNoEntry(game)
        value=int(value)
        game.changeStats("energy", -25)
        if (value <= maxim):
            game.changeStats("credit", value)
            game.changeStats("deposit", value)
            message= ("Finance Adviser:\n"
                      f"You received a credit of ${value:.2f}.\n"
                      f"You now owe the bank ${game.credit:.2f}")        
        else:
            message("Finance Adviser:\n"
                    f"Loan declined due to inadequate guarantees from cashflow analysis!")
        game.lAdviserBox.config(text=message)
        game.displayStats()  # refresh la scor
    activateEntry(game,actionCredit)

# DEPOSIT (BANK)
def do_bdeposit(game):
    game.lAdviser.config(image=game.imgBankAdviser) 
    message=("Financial Adviser:\n"
             "How much money do you want to deposit?")
    game.lAdviserBox.config(text=message)
    def actionDeposit(game,value):
        game.changeStats("energy", -5)
        hideYesNoEntry(game)        
        value = int(value)
        if (game.cash >= value):
            game.changeStats("deposit", value)
            game.changeStats("cash", -value)
            message=("Finance Adviser:"
                    f"You deposited ${value}.\n"
                    f"Your total bank deposit is {game.deposit:.2f}!")
        else:
            message=("Finance Adviser:\n"
                     f"Failed! You don't have that kind of money!")
        game.lAdviserBox.config(text=message)
        game.displayStats()  # refresh la scor
    activateEntry(game,actionDeposit)

# WITHDRAW (BANK)
def do_bwithdraw(game):
    game.lAdviser.config(image=game.imgBankAdviser) 
    message=("Financial Adviser:\n"
            "How much money do you want to withdraw?")
    game.lAdviserBox.config(text=message)
    def actionWithdraw(game,value):
        hideYesNoEntry(game)        
        game.changeStats("energy", -5)
        value=int(value)
        if (game.deposit >= value):
            game.changeStats("cash", value)
            game.changeStats("deposit", -value)
            message=("Financial Adviser:\n"
                     f"You withdrew ${value}.\n"
                     f"You have ${game.deposit} left in your deposit.")
        else:
            message=("Financial Adviser:\n"
                     f"Failed! Insufficient funds.")
        game.lAdviserBox.config(text=message)
        game.displayStats()  # refresh la scor
    activateEntry(game,actionWithdraw)


