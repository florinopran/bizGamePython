from engine import *
from display import *
from tkinter import messagebox, simpledialog
from displayOptBox import *
import constants
import random, os


def do_brest(game, engine):
    hideYesNoEntry(game)
    game.canvasContainer.itemconfig(game.adviserC, image=game.oldManAdviser)
    game.canvasContainer.itemconfig(game.environmentC, image=game.bedroomEnvironment)    
    game.lAdviserBox.config(text="")  #reset dialog box
    hideYesNoEntry(game) #eliminate dialog box's options (yes/no/entry)
    engine.timeline(game)
    game.displayStats()
    if game.gameOn==1:  

        def adviserHere():    
            game.canvasContainer.itemconfig(game.adviserC, image=game.callAdviser)
            game.lAdviserBox.config(text="Need help? \nMaybe you should call an advisor...")
            def actionCallAdviser(game,response):
                hideYesNoEntry(game)
                if response=="yes":
                    game.canvasContainer.itemconfig(game.adviserC, image=game.oldManAdviser)
                    message="Adviser: "
                    if game.time<10 and game.job==0:
                        message+="You should get a job (you'll lose energy)."
                    if game.job==0 and game.biz==0:
                        message+="\nAlert: You have no job and own no business."
                    if game.cash<100:
                        message+="\nAlert: You're dangerously low on cash."

                    randomAdvice=random.randint(0,7)
                    message+="\n\nLet me give you a tip:"
                    
                    message+=constants.ADVISER_PEDIA["randomAdvice"][randomAdvice]   

                    message+="\n\n💡If you need specific details, just type \"help\""

                    game.lAdviserBox.config(text=message)

                    def distroybNormalize():
                        if hasattr(game, 'bNormalize') and game.bNormalize:
                            game.bNormalize.destroy()
                            game.bNormalize = None
                    def normalizeWindow():
                        game.lAdviserBox.config(width=42,height=10)
                        game.lAdviserBox.place(x=20,y=310)
                        game.bentry.place(x=460, y=428)
                        game.submit_bentry.place(x=460, y=468)
                        distroybNormalize()
                        hideYesNoEntry(game)
                        

                    def actionPedia(game,response):                    
                        if response in constants.ADVISER_PEDIA:
                            # extend dialog box
                            game.lAdviserBox.tkraise()
                            game.lAdviserBox.config(width=52, height=16)
                            game.lAdviserBox.place(x=20,y=170)
                            game.bentry.place(x=680, y=428)
                            game.submit_bentry.place(x=680, y=468)
                            message=constants.ADVISER_PEDIA[response]
                            message+="\nIf I'm boring you, feel free to say bye."
                            game.lAdviserBox.config(text=message)
                            distroybNormalize()
                            game.bNormalize = Button(image=game.xMark, borderwidth=0, highlightthickness=0,
                                command=lambda: normalizeWindow())
                            game.bNormalize.place(x=520, y=175)
                        elif response == "bye":
                            normalizeWindow()
                            game.lAdviserBox.config(text="Business Adviser:\n Good luck!")
                        
                        else:  # Handle unrecognized response
                            normalizeWindow()
                            game.lAdviserBox.config(text="Adviser: Sorry! I do not understand.")                   
                    activateEntry(game,actionPedia)  
                else:
                    game.lAdviserBox.config(text="As you wish...\n You can call your adviser tomorrow.")
            activateYesNo(game,actionCallAdviser)

        def girlfriendHere(): 
            # set the message
            if game.datingStatusLevel==4:
                message=random.choice(
                                    constants.RELATION_SOFT_DILEMA
                                    )
            elif game.datingStatusLevel==3:
                message=random.choice(
                                    constants.RELATION_SELF_DILEMA+
                                    constants.RELATION_COMMITTED_DILEMA
                                    )
            elif game.datingStatusLevel==2:
                message=random.choice(
                                    constants.RELATION_SELF_DILEMA+
                                    constants.RELATION_COMMITTED_DILEMA+
                                    constants.RELATION_HEAVY_DILEMA
                                    )
            elif game.datingStatusLevel==1:
                message=random.choice(
                                    constants.RELATION_HEAVY_DILEMA
                                    )
            # set the image
            if message in constants.RELATION_SELF_DILEMA:
                theImage=game.imgGirlfriend5
            else:
                theImage=random.choice([
                                    game.imgGirlfriend1,
                                    game.imgGirlfriend2,
                                    game.imgGirlfriend3,
                                    game.imgGirlfriend4
                                    ]) 
            # show image
            game.canvasContainer.itemconfig(game.adviserC, image=theImage)    
            # show message                    
            game.lAdviserBox.config(text=message)
            def actionGirlfriendDilema(game,response):  #response doesn't matter                       
                hideYesNoEntry(game)  

                message=random.choice(constants.RELATION_EVENTS) # "Let's to something"

                game.lAdviserBox.config(text=message)
                def actionGirlEvent(game,response):
                    hideYesNoEntry(game)
                    if response=="no" and random.randint(1,3)==1: # might be bad for you
                        game.lAdviserBox.config(text="Ohh! Maybe we should just break up!")
                        def actionBreakup(game,response):
                            hideYesNoEntry(game)
                            if response=="yes":
                                hideYesNoEntry(game)
                                game.changeStats("datingStatusLevel",-game.datingStatusLevel) #single
                                game.lAdviserBox.config(text="You broke up!"
                                        f"Now you're {game.STATUS_OPTIONS[game.datingStatusLevel]}") 
                            else:
                                increment=-3 # change in relationScore (she's still upset)
                                game.changeStats("relationScore",increment)                            
                                game.girlfriendName=""
                                game.lAdviserBox.config(text="Still hanging on..."\
                                            f"Relation score is {game.relationScore}({increment})")                                                      
                        activateYesNo(game,actionBreakup)
                    elif response=="yes": # yes to the event
                        increment=2
                        game.changeStats("relationScore",increment)
                        message=f"Sweeet! Love you baby!\n"\
                            f"\nRelation score is {game.relationScore}({increment})"                    
                        game.lAdviserBox.config(text=message)                    
                        if (game.relationScore>(game.datingStatusLevel+2)*10 and
                            random.randint(1,game.datingStatusLevel)==1 and
                            game.datingStatusLevel<4):                    
                            # she might want to go the the next level if:
                            #   reached a certain relation score
                            #   a random chance (less chance with higher level)
                            #   not married yet.
                            hideYesNoEntry(game)
                            game.lAdviserBox.config(text="Maybe we should make the next step\n in our relationship...")
                            def actionAdvanceRelation(game,response):
                                hideYesNoEntry(game)                            
                                if response=="yes":
                                    game.changeStats("datingStatusLevel",1)
                                    increment=5
                                    game.changeStats("relationScore",increment)
                                    message="You made the next step:"\
                                            f"\nNow you're {game.STATUS_OPTIONS[game.datingStatusLevel]}"                                        
                                else: # you don't want to make the next step.
                                    increment=-7
                                    game.changeStats("relationScore",increment)  
                                    message="\nYou're not ready to make the next step."   
                                message+=f"\nRelation Score is {game.relationScore} ({increment})"  
                                game.lAdviserBox.config(text=message)                                                 
                            activateYesNo(game,actionAdvanceRelation)
                activateYesNo(game,actionGirlEvent)
            activateEntry(game,actionGirlfriendDilema)

        randomChance=random.randint(1,2)
        print(randomChance)
        if game.datingStatusLevel>0 and game.datingStatusLevel<4 and randomChance==1:
            print(f"-girlfriend")
            girlfriendHere()
        elif random.randint(1,2)==1:
            adviserHere()



def do_bgamble(game, engine):
    hideYesNoEntry(game)
    game.canvasContainer.itemconfig(game.adviserC, image=game.dealerAdviser)
    game.canvasContainer.itemconfig(game.environmentC, image=game.casinoEnvironment)    
    game.lAdviserBox.config(text="Club Adviser:\n"
                                "Welcome to the club, mate!\n"
                                "How much money do you want to bring to the table?")
    cashflow=0

    def actionCashFlow(game, cashInTheGame):
        nonlocal cashflow
        cashflow = int(cashInTheGame)
        if cashflow > game.cash:
            game.lAdviserBox.config(text="Club Adviser:\n"
                                        "You don't have enough money.\n"
                                        "Come back when you do.")
        else:
            game.changeStats("cash", -cashflow)
            game.displayStats()
            game.lAdviserBox.config(text=f"Dealer:\n"
                                    f"You have ${cashflow} to gamble.\n"
                                    ) 
            def actionTakeNoticeGamble(game,response):
                gamble()
            activateOk(game,actionTakeNoticeGamble)

    def gamble():  # valid cashflow  
        game.lAdviserBox.config(text=f"Dealer:\n"
                                    f"You have ${cashflow}.\n"
                                    "How much do you want to bet on RED?")  
        
        def actionBet(game, betx):
            nonlocal cashflow
            bet = int(betx) 
            validBet=True           
            if bet > cashflow:                                
                print(f"bet is {bet}. cashflow is: {cashflow}")
                game.lAdviserBox.config(text=f"Dealer:\n"
                                             f"Impossible!"
                                             f"You only have ${cashflow} in your pocket.\n"
                                            f"You can't bet ${bet}.")
                def actionInvalidBet(game,response):
                    print("invalid bet")
                    nonlocal validBet                    
                    validBet=False  
                    print (validBet,response,"function called")
                    gamble()                
                activateOk(game,actionInvalidBet)
            else: 
                # if validBet:
                game.changeStats("energy", -5) 
                game.displayStats()
                
                result = random.randint(1, 37)  # Simulates roulette
                if 1 <= result <= 18:  # RED => WIN
                    cashflow += bet   
                    message=(f"Dealer:\n"
                            f"You bet ${bet} on RED.\n"
                            "😃😃😃 It's RED! You won!💰💰💰\n"
                            f"You now have ${cashflow}.\n\n"
                            "Do you want to continue?")  
                else:        # BLACK => LOSE
                    cashflow -= bet                
                    message=(f"Dealer:\n"
                            f"You bet {bet} on RED.\n"
                            "😢 It's BLACK! You LOST!\n"
                            f"You now have {cashflow}.\n\n"
                            "Do you want to continue?")
                game.lAdviserBox.config(text=message)
                def actionBetResult(game, response):
                    if response == "yes" and cashflow>0:
                        gamble()
                    else:
                        endGambling()             
                activateYesNo(game, actionBetResult)
        activateEntry(game, actionBet)
    def endGambling():
        winnings = cashflow * 0.9  # Club keeps 10%
        game.lAdviserBox.config(text=f"Club Adviser:\n"
                                     f"Club keeps 10% of your money.\n"
                                     f"You're leaving the club with {winnings}.")
        game.changeStats("cash", winnings)
        game.displayStats()
        hideYesNoEntry(game)
    activateEntry(game, actionCashFlow)
    
    

def do_bclub(game):  
    # in the club:
    # you party (and get connections)
    # you have a chance to play poker for money
    # you have a chance to meet a girl
    hideYesNoEntry(game)
    game.canvasContainer.itemconfig(game.adviserC, image=game.dealerAdviser)
    game.canvasContainer.itemconfig(game.environmentC, image=game.clubEnvironment)  

    def poker():           
        game.lAdviserBox.config(text="Club Adviser: \n"
                                "We gathered some friends for a poker game.\n"
                                "Wanna\'join?")    
        # this one is kept in a loop (until user click on NO)        
        def actionPokerOpportunity(game,response):
            if response=="no":
                hideYesNoEntry(game)
                game.lAdviserBox.config(text="Club Adviser: \nCool. Maybe next time!")
                return
            # if yes:
            game.lAdviserBox.config(text=f"Minimum bet is ${baseTicket:.2f}."                                    
                                    "\nHow much do you want to bet?"
                                    )
            def actionPlayPoker(game,betx):                
                bet=int(betx)
                if bet<baseTicket or bet>game.netWorth:
                    hideYesNoEntry(game)
                    game.lAdviserBox.config(text="Club Adviser: Not with this money. Maybe next time!")
                else:                    
                    pokerOdds=random.randint(0,150) # take 0% (lose all) to 150% (earn 50%)
                    pokerOdds+=5*game.scamSkill # 1 scamSkill => 5% eg. 10(scamSkill)=>+50%
                    cashResult=bet*(pokerOdds/100) #includes bet. 0=lost all.
                    if game.con<=40:
                        newFriends=random.randint(-1,3)
                    else:
                        newFriends=0
                    game.changeStats("con", newFriends)
                    if cashResult>=bet:
                        game.changeStats("cash", cashResult-bet)
                    else:
                        game.changeStats("credit",-cashResult+bet)
                    game.changeStats("energy", -10)
                    game.displayStats()
                    game.lAdviserBox.config(text=
                                            f"Club Adviser\n"
                                            f"Cool game!\n" 
                                            f"> You put on the table:    ${bet:.2f}.\n"
                                            f"> You take from the table: ${cashResult:.2f}.\n"
                                            f"> Friends={newFriends}.\n\n"
                                            "Play again?")   
                    def actionFinalResult(game,response):    
                        if response=="yes":
                            actionPokerOpportunity(game,"yes")
                        else:
                            hideYesNoEntry(game)
                            game.lAdviserBox.config(text=
                                            f"Cool game! See you later!")      
                    activateYesNo(game,actionFinalResult)                        
            activateEntry(game,actionPlayPoker)  
        activateYesNo(game,actionPokerOpportunity)
    # end of poker() function
    

    def meetGirl():         
            # GET A GIRL IN THE CLUB
        # self.STATUSOPTIONS :
        #     "single", "dating a college girl", "dating a lady",
        #     "engaged", "married", "divorced"    
        # self.status = self.STATUSOPTIONS[self.datingStatusLevel]
        if random.randint(1,2)==1 and game.socialSkill>=5 and game.datingStatusLevel<=1:                        
            #u're single (0) or dating a college girl (1) => upgrade possible ( to a lady (2) )
            game.canvasContainer.itemconfig(game.adviserC, image=game.imgGirlfriend1)
            game.canvasContainer.itemconfig(game.environmentC, image=game.clubEnvironment) 
            game.lAdviserBox.config(text=(
                "Dating Adviser: "
                "\nSee that beautiful girl in the corner?"
                "\nGo and talk to her!"
                "\nYou should probably buy her a drink."            
                ))
            def actionGetGirl(game,response):
                hideYesNoEntry(game)
                if response=="yes":  
                    chancesWithTheGirl =  random.randint(0,game.socialSkill)           
                    print (chancesWithTheGirl)
                    if chancesWithTheGirl>game.datingStatusLevel*30+20 and random.randint(1,2)==1:                        
                        game.lAdviserBox.config(text="Dating Adviser:\nYou got the girl!")                            
                        #upgrade to next level
                        def actionUpgradeStatus(game,response):
                            hideYesNoEntry(game)
                            game.changeStats("datingStatusLevel",1) # change status and the rest 
                            game.changeStats("credit",100) 
                            game.canvasContainer.itemconfig(game.personaC, image=game.personaCouple)  
                            game.lAdviserBox.config(text=(
                                "Dating Adviser:"
                                "\nYou got the girl!"
                                f"\nStatus level changed: you're now {game.status}"
                                f"\nAlso, you have more connections now: {game.con},"
                                f"\nand have higher monthly costs."
                            ))
                            game.displayStats()
                        # single/divorced => might get into a relation
                        if game.datingStatusLevel==0 or game.datingStatusLevel==5: 
                            activateOk(game,actionUpgradeStatus)
                        else: 
                            effectOnRelation=random.randint(1,7)
                            if effectOnRelation in [1,2,3,4]: # relationScore decreased
                                game.lAdviserBox.config(text=
                                            f"You slept with her, but {game.girlfriendName} suspects something."
                                            f"\nRelation score decreased to {game.relationScore}(-3)"
                                            f"\n Your social skill improved to {game.socialSkill}(+3)"
                                                    )
                                game.changeStats("relationScore",-3)
                                game.changeStats("socialSkill",3)
                            elif effectOnRelation==5: # relationScore decreased
                                game.lAdviserBox.config(text=
                                            f"You slept with her, but {game.girlfriendName} found out."
                                            f"\nThere was a big fight, but she forgave you!"
                                            f"\nRelation score decreased to {game.relationScore}(-7)"
                                            f"\n Your social skill improved to {game.socialSkill}(+3)"
                                                    )
                                game.changeStats("relationScore",-7)
                                game.changeStats("socialSkill",3)
                            elif effectOnRelation==6 and game.datingStatusLevel<4: # relationScore decreased
                                game.lAdviserBox.config(text=
                                            f"You slept with her, but returned to your unsuspicious partner.."
                                            f"\nRelation score decreased to {game.relationScore}(-1)"                                        
                                            f"\n Your social skill improved to {game.socialSkill}(+3)"                            
                                                    )
                                game.changeStats("relationScore",-1)
                                game.changeStats("socialSkill",3)
                            elif effectOnRelation==7 and game.datingStatusLevel<4:   # become single
                                game.lAdviserBox.config(text=
                                            "You slept with her."
                                            f"\n{game.girlfriendName} knows! She dumped your ass!" 
                                            f"\nStill... your social skill increased to {game.socialSkill}(+3)"
                                                        )
                                game.changeStats("datingStatusLevel",-game.datingStatusLevel)
                                game.changeStats("socialSkill",3)                                
                            elif effectOnRelation==7 and game.datingStatusLevel==4:
                                game.lAdviserBox.config(text=                                            
                                            f"\n{game.girlfriendName} divorced you!" 
                                            f"\nStill... your social skill increased to {game.socialSkill}(+3)"
                                                        )
                                game.changeStats("datingStatusLevel",-game.datingStatusLevel)
                                game.changeStats("socialSkill",3) 


                    else:
                        game.lAdviserBox.config(text="Dating Adviser:\n Ouch! Harsh rejection!😒")
                else:
                    game.lAdviserBox.config(text=(
                        "Dating Adviser:" 
                        "\nIt takes guts to approach such a beautiful woman."
                        "\nBut you chickened out. Not cool, man!"
                        ))
            activateYesNo(game,actionGetGirl)
    # end of meetGirl function
                                
    if game.deposit<100:
        baseTicket=100
    else:
        baseTicket=100+int(0.005*game.netWorth) # 0.5% of your net worth
    
    game.lAdviserBox.config(text=f"Club Adviser: \n"
                            f"Will you pay the ${baseTicket} entry fee?")
    # MAIN CLUB FUNCTION (ACTIVATED IN THE END)
    def actionClubbing(game,response):
        game.lAdviserBox.config(text="")
        hideYesNoEntry(game)
        if response=="no":
            game.lAdviserBox.config(text="Ok. Come back when you want to party!")
            return
        #if response == yes, do that:
        newFriends=random.randint(-1,3) # new partners
        game.lAdviserBox.config (text=f"Club Adviser:\n"
                                 "You've spent time in the club: \n"
                                f"> new friends: {newFriends}.\n"
                                f"> cash flow: ${baseTicket}\n"
                                f"> energy spent: -10")        
        if game.deposit>baseTicket:
            game.changeStats("deposit", -baseTicket)
        else:
            game.changeStats("credit",baseTicket)
        game.changeStats("energy", -10)
        game.changeStats("con",newFriends)
        game.displayStats()   

         
        # play poker?
        if (random.randint(1,2)==1) and (game.energy>25): # 50% chances 
            poker()  # 50% chances
        else:
            #meet girl
            meetGirl() # 50% chances
            
            
    

    activateYesNo(game,actionClubbing)



def do_bcharity(game):
    hideYesNoEntry(game)
    game.canvasContainer.itemconfig(game.adviserC, image=game.charityLadyAdviser)
    game.canvasContainer.itemconfig(game.environmentC, image=game.charityEnvironment)      
    castig_con=0   
    charityOn=True
    message="Charity Adviser:\n"     

    if game.netWorth<10000 or game.con<30:
        charityOn=False
        message+=("You're not wealthy enough to attend tu such events!\n"
                  "You need money ($10.000) and connections (30).")
    else:
        message+="Welcome!\nYou met the requirement for this event.\n"

    game.lAdviserBox.config(text=message)
    
    def actionEnterEvent(game,response):
        nonlocal charityOn
        if charityOn==False:
            hideYesNoEntry(game)
            
        else:
            game.changeStats("energy", -20)
            game.displayStats()
            charityFactor = random.randint(10, 50) / 1000  # intre 1% si 5%
            minDonation = int(game.netWorth * charityFactor)
            game.lAdviserBox.config(text=f"Charity Adviser: "
                                    f"Your networth is {game.netWorth})\n"
                                    f"How much will you give to charity?")
            def actionDonation(game,donation):
                hideYesNoEntry(game)
                donation=int(donation)
                game.changeStats("credit", donation)
                
                if donation<=minDonation:
                    castig_con=-random.randint(0,int(game.con*0.15)) 
                    game.lAdviserBox.config(text="Charity Advisor:\n"
                                     f"Your donation was below other donations(${minDonation})\n"
                                        "That made you look cheap. \n"
                                        "You actually lost some connections."
                                        f"({castig_con})"
                                     )                    
                else:
                    castig_con = random.randint(0, int(donation / (0.02 * game.netWorth)));
                    # castigul maxim de parteneri = donatia / 2% networth
                    if (castig_con > 0):
                       game.lAdviserBox.config(text="Charity Adviser:\n"
                                        "You gain new connections!"
                                            f"(+{castig_con})")
                
                game.changeStats("con",castig_con)
                game.displayStats()

            activateEntry(game,actionDonation)
    
    activateOk(game,actionEnterEvent)
    game.displayStats()  # refresh la scor


def do_bcocaine(game):
    hideYesNoEntry(game)
    game.canvasContainer.itemconfig(game.adviserC, image=game.drugDealerAdviser)
    game.canvasContainer.itemconfig(game.environmentC, image=game.backstreetEnvironment)
    #cost of cocaine is game.cocaineMin, but not less then % of your cash money
    # % is determined by game.cocainePP * cash
    # both game.cocaineMin and game.cocainePP are growing 

    cocaineCost=max(game.cocaineMin,game.cocainePP*game.cash)    
    
    message=("Heinous Dealer:\n"
            "Hei mate! Want some cocaine?\n")  
    if game.cash<cocaineCost:   
        #not enough money. It all stops here.       
        message+=(f"Come back when you have at least ${cocaineCost}!")  
        game.lAdviserBox.config(text=message) 

    else: 
        # you have money to buy cocaine
        message+=(f"One dose would cost you ${cocaineCost}, \n"
                                       "but will boost your energy \n"
                                       "with 50%! Will you do it?"
                                       ) 
        game.lAdviserBox.config(text=message) # Question: YES or NO?
        def buyCocaine(game,opt): # After you say YES or NO
            hideYesNoEntry(game)            
            if opt=="yes":
                game.lAdviserBox.config(text=("Heinous Dealer:\n"
                                               "Enjoy It!\n"
                                               "By the way..."
                                               "Next time, the price might be higher!"))                
                game.changeStats("energy",50)
                game.changeStats("cash",-500)
                game.cocainePP+=3
                game.displayStats()  # refresh la scor
                if game.cocainePP>0.75:
                    game.cocainePP=0.50 # it will be capped between 50% and 75%
                game.cocaineMin=game.cocaineMin*1.25
            elif opt=="no":
                game.lAdviserBox.config(text=("Heinous Dealer:\n"
                                               "Don't waste my time, mate!\n"
                                               "You don't want to see me angry!"))
                
            if opt=="yes" and random.randint(1,5)==1: # daca te-ai drogat, ai 20% sanse sa dai de punks
                game.lAdviserBox.config(text=("Punks:\n"
                                               "Gimme' all your cash!")) # Question: YES or NO?
                def punks(game, opt2):    
                    hideYesNoEntry(game)                    
                    if opt2=="yes":
                        game.changeStats("cash", -game.cash)
                        game.lAdviserBox.config(text=("Punks:\n"
                                               "Thanks fool! You can go.\n\n"
                                               "(You are safe)"))
                        game.displayStats()  # refresh la scor
                    elif random.randint(1,5)==1: # 20% sa iei bataie
                        game.lAdviserBox.config(text=("Facts:\n"
                                               "They've beaten you.\n\n"
                                               "(Your energy is almost depleted)") )  
                        game.changeStats("cash",-game.cash)
                        game.changeStats("energy",5-game.energy)
                        game.displayStats()  # refresh la scor
                    else: # risti si iese bine
                        message=("Punks:\n"
                                "We were joking, man! You can go.\n\n"
                                )
                        if random.randint(1, 2) == 1:  # 50% chances to meet potential partners
                            message+="You're cool. We should be friends."
                            game.lAdviserBox.config(text=message)
                            def cocaineFriends(game, opt3):
                                hideYesNoEntry(game)
                                if opt3=="OK":
                                    print("cocaine friends")                   
                                    partners=random.randint(1,2)
                                    game.changeStats("con",partners)
                                    game.lAdviserBox.config(text=("Personal Adviser:\n"
                                                            f"You met some new connections (+{partners} partner(s))."))
                                    game.displayStats()  # refresh la scor
                            activateOk(game, cocaineFriends)
                        else:
                            game.lAdviserBox.config(text=message)
                activateYesNo(game, punks)                       
        activateYesNo (game, buyCocaine)


def do_btrain(game, engine): #socialize
    # game.lAdviser.config(image=game.imgAdvYoungGirl)
    hideYesNoEntry(game)
    game.canvasContainer.itemconfig(game.adviserC, image=game.youngGirlAdviser)
    game.canvasContainer.itemconfig(game.environmentC, image=game.socializeEnvironment)
    game.lAdviserBox.config(text="Personal Adviser Kate:"
                                "\nReady to flex your brain, booze your confidence, "
                                "\nand sprint like it’s no tomorrow?"
                                )   
    def actionTrain(game, opt):
        hideYesNoEntry(game)
        if opt=="yes":
            socializeCost=random.randint(5,25)+int(0.005*game.netWorth) #0,5%
            socializeEnergy=random.randint(7,15)                                  
            skillGain=min(random.randint(-1,3),2) # possibilities -1/0/1/2/2
            conGain=random.randint(-1,1)
            trainPlace=random.choice(["bar","club","dance club","park","mall","football field"])
            trainActivity=random.choice(["socialized","trained","walked"])
            trainMood=random.choice(["joked","fooled around","goofed around","played pranks"])
            trainPeople=random.choice(["a cute girls","a potential partner","a training partner",
                                    "a puppy","an idiot","a drunk fellow"])
            message=(f"Personal Adviser Kate:"
                     f"\nYou've been in the {trainPlace}."
                     f"\nYou {trainActivity} and {trainMood} with {trainPeople}."
                     f"\nYou paid ${socializeCost}. Effect on energy: -{socializeEnergy}"
                     )
            game.changeStats("socialSkill",skillGain)
            game.changeStats("con",conGain)
            game.changeStats("energy",-socializeEnergy)
            game.changeStats("cash",-socializeCost)
            if skillGain==-1:
                message+=f"\n\nYour social skill decreased to {game.socialSkill} ({skillGain})"
            if skillGain==0:
                message+=f"\n\nYour social skill is unchanged: {game.socialSkill}."
            if skillGain>0:
                message+=f"\n\nYour social skill improved to {game.socialSkill} (+{skillGain})"
            message+=f"\nPartners: {conGain}"        
            # display message
            game.lAdviserBox.config(text=message)  
            # update stats
            game.displayStats()   
        elif opt=="no":
            game.lAdviserBox.config(text=("Personal Adviser Kate:"
                                     "\n\nYou'll never meet new people if you just stay home..."))
    activateYesNo (game, actionTrain)


# GAME OPTIONS (RETIRE / VACATION)
def do_bretire(game, engine):
    hideYesNoEntry(game)
    game.canvasContainer.itemconfig(game.adviserC, image=game.oldManAdviser)
    game.canvasContainer.itemconfig(game.environmentC, image=game.businessAdviser)
    game.lAdviserBox.config(text=(
                        "Personal Adviser?\n"
                        "Are you sure you want to retire?"))
    def actionRetire(game,response):
        hideYesNoEntry(game)
        if response=="yes":            
            game.lAdviserBox.config(text=(
                    "Personal Adviser?\n"
                    "So be it!"))        
            game.changeStats("gameon",-1)
            game.changeStats("energy",-100)
            game.displayStats()  # refresh la scor
            game.lbalance.config(text="G A M E   O V E R")
        else:
            game.lAdviserBox.config(text=("Personal Adviser\n"
                                            "Cool. Let's get back to business!"))
    activateYesNo(game,actionRetire)

def do_bvacation(game, engine):
    hideYesNoEntry(game)
    game.canvasContainer.itemconfig(game.adviserC, image=game.oldManAdviser)
    game.canvasContainer.itemconfig(game.environmentC, image=game.businessAdviser)
    game.lAdviserBox.config(text=(
                        "Personal Adviser?\n"
                        "Need a 2 week vacation?"))
    def actionVacation(game,response):
        hideYesNoEntry(game)
        if response=="yes":            
            game.lAdviserBox.config(text=(
                    "Personal Adviser?\n"
                    "You just let two weeks pass away, you lazy ass!"))                
            game.changeStats("energy",100)
            game.changeStats("time",2)
            game.displayStats()  # refresh la scor                
        else:
            game.lAdviserBox.config(text=("Personal Adviser\n"
                                            "Cool. Let's stay focused!"))
    activateYesNo(game,actionVacation)


def do_bsave(game,engine):
    # copy data from original file
    file1=open(os.path.join(os.path.join(os.path.dirname(__file__), "data.csv")),"r")
    file1Data=[]
    i=0
    for line in file1:
        file1Data.append(line)     
    file1.close() 
    # paste data in data_saved_v01.csv
    file2=open(os.path.join(os.path.join(os.path.dirname(__file__), "data_saved_01.csv")),"w") 
    for r in file1Data:
        if " = " in r:
            r=r.strip()
            par,parValue=r.split(" = ")
            r= par + " = " + str(getattr(game,par))+"\n"
        file2.write(r) # write each line
    file2.close()

def do_bload(game,engine):
        # copy data from saved file
    file1=open(os.path.join(os.path.join(os.path.dirname(__file__), "data_saved_01.csv")),"r")
    for line in file1:
        line=line.strip()
        if " = " in line:
            par,parValue=line.split(" = ")
            if "." in parValue: # float
                parValue = float(parValue)
            elif parValue.isdigit(): # int
                parValue=int(parValue)
            elif parValue=="None": # None
                parValue=None
            else:   # string
                parValue = parValue
            print(f"Saved {par} is {parValue}")
            setattr(game,par,parValue)
            game.displayStats()
    file1.close() 

