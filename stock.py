from display import *
from tkinter import messagebox, simpledialog
from displayOptBox import *


# INVEST (STOCK)
def do_binvest(game):
    game.lAdviser.config(image=game.imgBroker)
    game.lAdviserBox.config(text="Warren Broker:\n"\
                                f"\nIndex value = {game.stockIndexMV:.2f}"
                                f"\nReal value (estimated by experts) = {game.stockIndexRV:.2f}"
                                f"\nHow many shares do you want to buy?"
                                    ) 
    def actionInvest(game, shares):
        shares=int(shares)
        hideYesNoEntry(game)
        value=int(shares*game.stockIndexMV)     
        if value>0:
            game.changeStats("energy", -10)               
            if (game.deposit >= value and shares>0):
                game.changeStats("stock", shares)
                game.changeStats("deposit", -value)
                game.stockTotalInvestment+=value
                message=("Warren Broker:"
                         f"\nYou invested ${value:.2f} for {shares} shares.")          
            else:
                message=("Warren Broker: Failed to buy"
                         f"\nYou only have ${game.deposit:.2f} in your bank account.")     
            game.lAdviserBox.config(text=message)     
            game.displayStats()  # refresh la scor
    activateEntry(game, actionInvest)

# SELL (STOCK)
def do_bsell(game):
    game.lAdviser.config(image=game.imgBroker)
    game.lAdviserBox.config(text=("Warren Broker:\n"
                                    "\nHow many shares do you want to sell?.\n ")) 
    def actionSell(game, shares):
        shares=int(shares)
        hideYesNoEntry(game)
        value=int(shares*game.stockIndexMV)        
        game.changeStats("energy", -10)        
        if (game.stock >= shares and shares>0): # you have shares to sell
            game.stockTotalInvestment=(game.stockTotalInvestment/game.stock)*(game.stock-shares)
            game.changeStats("stock", -shares)
            game.changeStats("deposit", value)            
            message=("Warren Broker:"
                     f"\nYou liquidated ${value:.2f} worth of stocks.\n"
                     f"\nYour total portofolio is now ${game.stock*game.stockIndexMV:.2f}")
        else:
            message=("Warren Broker: Failed to sell."
                     f"\nYo only have {game.stock} shares.")
        game.lAdviserBox.config(text=message)
        game.displayStats()  # refresh la scor
    activateEntry(game,actionSell)


