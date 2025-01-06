from display import *
from engine import *
from tkinter import messagebox, simpledialog
from displayOptBox import *
import random


def do_bstart(game, engine):
    game.lAdviser.config(image=game.imgBizAdviser)
    bool = True # only the first reason to deny will be displayed.   
    message="Business Adviser: \n"
    if game.biz > 0:
        bool = False
        message+="You already have a business going!"
    if game.deposit < 7000 and bool==True:        
        bool = False
        message+=("You don't have enough money in the bank \n" 
        "to start a business! ($7000 needed)")
    if game.con < 1 and bool==True:
        bool == False
        message+=("You need at least one connection\n" 
                  "in order to start a business! \n"
                    "You should be more social.")        
    if bool==False:    
        game.lAdviserBox.config(text=message)                
    else:        
        game.changeStats("deposit", -7000)
        game.changeStats("biz", 1)
        game.changeStats("energy", -35)
        game.changeStats("job",-game.job)
        game.lAdviserBox.config(text="Business Adviser:\n"
                                "You started a business! Congratulation! 🎉")        
    game.displayStats()  # refresh la scor


def do_bexpand(game, engine):
    game.lAdviser.config(image=game.imgBizAdviser)
    expandon = True
    messageSuccess="Business Adviser:"
    success=0
    messageDeny="Business Adviser:"
    deny=0
    messageInfo="Business Adviser:"
    info=0
    messageAlready12="Business Adviser:"
    already12=0

    levelup = game.biz + 1 # the level you want to reach
    print("levelup=",levelup)

    if game.deposit >= engine.biz_invest(levelup) and expandon == True:
        info=1
        messageInfo+=(
                f"\nYou have ${game.deposit}.\n"
                f"That's enough to upgrade your business."
                )
    else:
        expandon = False
        deny=1
        messageDeny+=(f"\nInsufficient funds!\n"                    
                    f"You need to have a bank account of at least ${engine.biz_invest(levelup)}!")

    if game.con >= game.biz * 10 + 1 and expandon == True:
        info=1
        messageInfo+=(
                f"\nYou have enough connections to upgrade your business.")
    else:
        expandon = False
        deny=1
        messageDeny+=(f"\nInsufficient connections!\n"                
                f"You need {game.biz * 10 + 1} connexions to upgrade.")    

    if levelup <= 12 and expandon == True:
        success=1
        messageSuccess+=(f"\nYou made it! You now own a level {levelup} business.")        
    elif levelup>12:
        expandon = False 
        already12=1
        messageAlready12+=(f"Business Adviser: \n" 
                           "You have a level 12 business. You can't go any higher!\n"
                        f"Maybe you should think about making a big exit!")        

    if already12==1: 
        game.lAdviserBox.config(text=messageAlready12)
        
    else:    
        if deny==1: #first inform, and then deny
            game.lAdviserBox.config(text=messageInfo)
            game.lAdviserBox.config(text=messageDeny)

    
    if expandon == True: #after all the testing, you succeed upgrading
        success=1
        messageSuccess+=(
                    f"\nYou had enough resources ({engine.biz_invest(levelup)}) \n"
                    f"and connections ({game.biz * 10 + 1}) \n"
                    )
        game.changeStats("biz", 1)
        game.changeStats("energy", -20)
        game.changeStats("deposit", -engine.biz_invest(levelup))
        game.lAdviserBox.config(text=messageSuccess)
    game.displayStats()  # refresh la scor

def do_bboost(game,engine):
    hideYesNoEntry(game)
    game.lAdviser.config(image=game.imgBizAdviser)    
    game.lAdviserBox.config(text=("Business Adviser: \n"
                                  "What level do you want to boost your business at?\n "
                                  "Keep in mind that it will be 30% more expensive!\n"))
    def actionBoost(game,level):
        hideYesNoEntry(game)
        showResult=False   # will be True after the result will be displayed     
        boostToLevel=int(level)
        cost_boost_money = 0
        cost_boost_con = 0
        for i in range(game.biz + 1, boostToLevel + 1):
            cost_boost_money += engine.biz_invest(i) * 1.0
            # print(i,"...",cost_boost_money)
        cost_boost_con += boostToLevel * 10 * 1.3

        message=f"Business Adviser:\n"

        if (game.biz+1>=boostToLevel or game.biz>=11 or boostToLevel>12) and showResult==False:
            message+=(f"You can not boost your level from {game.biz} to {boostToLevel}.")
            showResult=True #show the result and stop

        if cost_boost_con>game.con and showResult==False:
            message+=(f"Failed!\n"
                      f"You need {cost_boost_con} partners and ${cost_boost_money} in deposits\n"
                      f"You only have {game.con} partners and ${game.deposit} in deposits.\n")
            showResult=True #show the result and stop
        
        if game.deposit<cost_boost_money and showResult==False:
            message+=(f"Failed!\n"
                      f"You need {cost_boost_con} partners and ${cost_boost_money} in deposits\n"
                      f"You only have {game.con} partners and ${game.deposit} in deposits.\n")    
            showResult=True   
        
        if showResult==False: #have money & connections. 
            message+=(f"You boosted your business level from {game.biz} to {boostToLevel}")
            showResult=True            
            game.changeStats("biz", boostToLevel - game.biz)
            game.changeStats("deposit", -cost_boost_money)
            game.changeStats("energy", -20)
            game.displayStats()  # refresh la scor

        game.lAdviserBox.config(text=message)
    activateEntry(game,actionBoost)

def do_bscam(game,engine):
    hideYesNoEntry(game)
    game.lAdviser.config(image=game.imgScamAdviser)
    message=("Con Artist: \n"
             "You're a shark surrounded by minnows, my friend. \n"
             "Let me show you how sharks thrive.\n"
             "They're coasting on your hard work. But you and me? \n"
             "We’re cut from the same cloth—smart, bold. \n"
             "One little nudge, and you’ll be swimming in profits. \n"
             "Who’s gonna know?\n"
             "Trust me, I see opportunity where others see risk.")
    game.lAdviserBox.config(text=message)

    def actionScam(game,opt):
        hideYesNoEntry(game)
        showResult=False
        message="Con Artist:\n"
        if opt=="no":
            message+=("Pff, suit yourself, you gutless little... kretznarg!\n"
                    "Enjoy your scraps, genius.")
            showResult=True
        if opt=="yes" and showResult==False:
            scamon = True
            conscam = random.randint(0, game.con)  # parteneri inselati
            litigiu = int(0.03 * conscam * engine.biz_val(game))  # castigi 3% din valoarea af/partener inselat
            if game.con >= 3 and scamon == True:  # poti face un scam daca ai macar 3 parteneri
                game.changeStats("energy", -20)
            else:
                scamon = False
                message += "\n You don't have enough partners to scam."

            if conscam >= 1 and scamon == True:  # pacalesti macar 1 partener
                message += f"\nYou stole ${litigiu} from {conscam} partners."
                game.changeStats("deposit", litigiu)
            else:
                scamon = False
                message += "You fooled no one but yourself! You lost one of your partners."
                game.changeStats("con", -1)

            conangry = random.randint(0, conscam)  # parteneri suparati
            if conangry > 0 and scamon == True:  # parteneri suparati
                message += f"\nYou've upset {conangry} parteners, {int(conangry / 3)} of which left you!"
                game.changeStats("con", -int(conangry / 3))
            else:
                scamon = False

            complainers = random.randint(0, int(conangry / 5))
            despagubiri = int(0.03 * engine.biz_val(game) * complainers * random.randint(1, 20))
            if random.randint(1, 4) and complainers > 0 and scamon == True:  # ai fost dat in judecata
                message += f"\nYou've been sued by {complainers} ex partners!"
                message += f"\nYou had to pay them ${despagubiri} in compensations."
                game.changeStats("credit", despagubiri)
            else:
                scamon = False
                message += "\nYou got away with it! Congratulation!"

            if random.randint(1, 5) and scamon == True:  # fines and detention
                message += f"\nAuthorities conducted an investigation against you." \
                            f"\nThey found you guilty. They fined you with ${int(0.1 * litigiu)}" \
                            f"\nYou also have to serve 2 weeks in isolation."
                game.changeStats("time", 2)
                game.changeStats("credit", int(0.1 * litigiu))
            game.lAdviserBox.config(text=message)
            showResult=True
            game.displayStats()  # refresh la scor
    if game.biz>0:
        activateYesNo(game, actionScam)
    else:
        game.lAdviserBox.config(text="Split fool! You don't even run a business!")

# -------------------------------------------
# ----------- EXIT BUSINESS -----------------
# -------------------------------------------

def do_bexit(game,engine):    
    hideYesNoEntry(game)
    soldBusiness=0 # keeps the value of transaction. if 0, there is no transaction
    game.lAdviser.config(image=game.imgBizAdviser)    
    
    game.changeStats("energy", -20) # Losing energy 

    def updateBusiness(soldBusiness): # sell adjustments
        print("(after if) before updates:",soldBusiness)
        #update stats
        if soldBusiness>0: 
            print("here it's being used:",soldBusiness)       
            game.changeStats("biz",-game.biz)
            # priority: reduce credits and put the extra in deposit.
            if soldBusiness<=game.credit: 
                game.changeStats("credit",-soldBusiness)
            else:
                game.changeStats("credit",-game.credit)
                game.changeStats("deposit",soldBusiness-game.credit)
            game.displayStats() # update stats
    
    if game.biz==0:
        game.lAdviserBox.config(text="Business Adviser:\n"\
                                "You don't run a business."
                                )  
        
    elif game.biz==1 and game.randant==0: # level 1 biz, with no randant (probably just started business)
        offer=3500 + random.randint(0,3500) # sell for less than you invested
        game.lAdviserBox.config(text="Business Adviser:\n"\
                                    f"Selling a business is a way to reduce credits!\n"\
                                    f"You have a ${offer} offer\n"\
                                    "Will you accept?")
        def actionAcceptSmallOffer(game,opt):            
            nonlocal soldBusiness #need this outside of the function
            hideYesNoEntry(game)
            if opt=="yes":
                soldBusiness=offer            
                game.lAdviserBox.config(text="Business Adviser:\n"\
                                    f"You sold your business for ${soldBusiness}."
                                    )
                print("modified successfuly:",soldBusiness)
                updateBusiness(soldBusiness)
        activateYesNo(game,actionAcceptSmallOffer)
        
    elif game.biz>=1 and game.randant>=0: # level 1 biz and randant>0 (profitable business)       
        x = int(engine.biz_val(game))
        offer=random.randint(int(x/3),int(x*1.3)) # willing to pay
        offerReveal=random.randint(int(offer*0.5),offer) # what you know about the offer
        game.lAdviserBox.config(text="Business Adviser:\n"
                                    "Selling a business is a way to reduce credits!\n"
                                    f"One of your partners is interested.\n"
                                    f"He would probably pay more than ${offerReveal}\n"
                                    f"Value of your business is ${engine.biz_val(game)}\n"
                                    f"Set your final price!")
        def actionSetPrice(game, price):
            nonlocal soldBusiness
            hideYesNoEntry(game)
            price=int(price)
            if price>offer: #not sold
                game.lAdviserBox.config(text="Business Adviser:\n"
                                        f"He was willing to pay no more than {offer}\n"
                                        f"The deal is off.")
            else: #sold for price
                game.lAdviserBox.config(text="Business Adviser:\n"
                                        f"You sold your business for {price}.\n"
                                        f"By the way: He was willing to pay no more than {offer}\n"
                                        )
                soldBusiness=price
                updateBusiness(soldBusiness)
        activateEntry(game,actionSetPrice)

    elif game.biz>=1 and game.randant<0: # unprofitable business
        game.lAdviserBox.config(text="Business Adviser:\n"
                                "No one is interested by an unprofitable business.")
    else:
        game.lAdviserBox.config(text="Business Adviser:\n"
                                "Uncharted situation. Not sure what to say.")
    


# -------------------------------------------
# ----------- TRAIN IN BUSINESS -------------
# -------------------------------------------

def do_btrain(game,engine):    
    hideYesNoEntry(game)
    game.lAdviser.config(image=game.imgBizAdviser) 
    #training cost
    cost=100+(game.bizSkill**2)*100

    game.lAdviserBox.config(text="Business Adviser:\n"\
                                "Do you want to follow an intensive Business Training?\n"
                                f"It will cost you: {cost}\n\n"
                                "Each skill level will add 1pp to your profits!\n"
                                "(for both: legit profits and scamming operations)"
                                )  
    
    def actionTrain(game,opt):  
        hideYesNoEntry(game)
        if opt=="yes":
            bizSkillGain=random.randint(0,2)
            scamSkillGain=random.randint(0,2)
            conGain=random.randint(-1,bizSkillGain+scamSkillGain)
            message="Business Adviser:\n"
            if bizSkillGain>0:
                message+=f"You actually learned something! (+{bizSkillGain} bizz skills)\n"
            elif bizSkillGain==0:
                message+=f"You didn't gain any knowledge! (+{bizSkillGain} biz skills)\n"
            message+=f"You learned to manipulate people (+{scamSkillGain} scam skills)\n"
            message+=f"(new connections:{conGain})"
            game.lAdviserBox.config(text=message)
            game.bizSkill+=bizSkillGain
            game.scamSkill+=scamSkillGain
            game.con+=conGain
            game.energy-=30
            game.credit+=cost            
            game.displayStats() # display updated stats
            
    activateYesNo(game,actionTrain)
        


















