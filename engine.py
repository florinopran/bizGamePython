# engine asigura actualizarea valorilor in timp
# (unitatea de timp = saptamana)
import random
from display import *
from decimal import Decimal, ROUND_HALF_UP # pentru a putea rotunji la doua zecimale
from tkinter import messagebox, simpledialog
import pyautogui

# I need a class because there are several complex functions which are calling each other
class Engine():
    def __init__(self):
        pass

    def timeline(self,game):
        # trece timpul
        game.changeStats("time", 1)
        game.changeStats("energy",75) #adds 70pp to energy (capped at 100pp)
        cashOut=0
        cashIn=0
        #make sure the number of connections is at least 0
        if game.con<0:
            game.con=0
        # incasare salariu
        if game.job>0: 
            cashIn+=game.job
            game.jobSeniority+=1
            game.changeStats("energy",-game.jobEnergy)
        # incasare dobanda pt depozitele preexistente
        if game.deposit>0:
            income_deposit=game.deposit*game.interest
            game.changeStats("deposit", income_deposit)
        else:
            income_deposit=0

        # STOCK MARKET
        messageStockMarket=""
        # shows if you dont't own anything
        game.lnews.config(text=f"Stock Market Index = ${game.stockIndexMV:.2f}"\
                          f"\nExperts estimate a real value of ${game.stockIndexRV:.2f}") 
        # stock market trends
        # real value of assets (2 digits) => variation between 1.00% and 5.00%
        realTrend=1+random.randint(100,int(game.stockNormalPerformance*10000))/10000 
        game.stockIndexRV=game.stockIndexRV*realTrend
        print (f"Real Trend= {realTrend}")
        eventChance=random.randint(1,18)
        if eventChance==13: # Crash
            crashValue=(random.randint(11,55))/100 # max 55%
            game.stockIndexMV=game.stockIndexMV*(1-crashValue)
            performance=crashValue
            messageStockMarket+=f"Huge crash on the market ({-performance*100:.2f}%)" #Event            
        elif eventChance==7: # Spike
            spikeValue=(random.randint(11,55))/100 # max 55%
            game.stockIndexMV=game.stockIndexMV*(1+spikeValue)
            performance=spikeValue
            messageStockMarket+=f"Huge Hype on the market ({performance*100:.2f}%)" #Event            
        else: # Normal evolution (no crash. no spike)
            if game.stockIndexMV>game.stockIndexRV:
                # 5% + half of the gap
                lowest=-game.stockNormalPerformance/2-((game.stockIndexMV/game.stockIndexRV)*100-100)/200  
                lowest=int(lowest*1000)
                # 2.5% (can still go higher)
                highest=game.stockNormalPerformance/2
                highest=int(highest*1000)                             
                randomPerformance=random.randint(lowest , highest)/1000 # pressure to go lower towards real value
                performance=max(randomPerformance,-0.11) # ex. -2.75% (capped at -11%)
                print(f"Trend down: {performance} is between {lowest/1000} and {highest/1000}") 
            else:
                # 5% + half of the gap
                highest=game.stockNormalPerformance/2+((game.stockIndexRV/game.stockIndexMV)*100-100)/200  
                highest=int(highest*1000)
                # -2.5% (can still go lower)
                lowest=-game.stockNormalPerformance/2 
                lowest=int(lowest*1000)                
                randomPerformance=random.randint(lowest, highest)/1000  # pressure to go higher towards real value
                performance=min(randomPerformance,0.11) # ex. +2.75%   (capped at +11%) 
                print(f"Trend up: {performance} is between {lowest/1000} and {highest/1000}")             
            game.stockIndexMV=game.stockIndexMV *(1+performance) # eg. * 1.0275
            messageStockMarket+=f"Market is calm ({performance*100:.2f}%)" #No event

        messageStockMarket+=f"\nIndex value is now {game.stockIndexMV:.2f} ({performance*100:.2f}%)"\
                            f"\nEstimated real value by experts is: {game.stockIndexRV:.2f}"
        
        messageStockMarket+=f"\nYou have {game.stock} shares in your portofolio"
        messageStockMarket+=f"\nthat worth ${game.stock*game.stockIndexMV:.2f}"
        messageStockMarket+=f"\nTotal investment = {game.stockTotalInvestment:.2f}"

            #dividends
        dividendsYield=random.randint(1,15) # procentul de dividende (se aplica la game.stock*game.stockIndexMV)
        if game.time%12==0: #anually
            dividendsValue=1+dividendsYield/100 * game.stock * game.stockIndexMV
            game.changeStats("deposit",dividendsValue)            
            messageStockMarket+=(f"\n\n You received dividends ({dividendsYield:.2f}%)!"
                                f"\n{dividendsValue:.2f}$ has been transferred to \nyour account." )

        if game.stock>0:
            game.lnews.config(text=f"{messageStockMarket}")

        # calcul profit afacere
        if game.biz > 0:
            game.bizval=int(self.biz_val(game)) # calculez valoarea afacerii si o salvez in game
            rand_con=self.rand_con(game)
            rand_con=Decimal(str(rand_con)).quantize(Decimal('0.0000'), rounding=ROUND_HALF_UP)
            rand_biz=self.rand_biz(game)
            rand_biz=Decimal(str(rand_biz)).quantize(Decimal('0.0000'), rounding=ROUND_HALF_UP)
            profit_con=int(rand_con*game.bizval) # already applied 2% for each bizSkill
            profit_biz=int(rand_biz*game.bizval) #already applied 2% for each bizSkill            
            profit_total=profit_con+profit_biz
            game.changeStats("randant",rand_con+rand_biz)
            cashIn+=profit_total
        else:
            profit_total=0
            rand_biz=0
            rand_con=0
            profit_biz=0
            profit_con=0


        #calcul income
        # cashIn = profit_total + game.job (deposits do not count)

        # calcul rata credit
        if game.credit>200:
            plata_credit=0.07*game.credit +0.03*game.credit # calcul rata de plata
            game.changeStats("credit", -0.03*game.credit) # scadere din principal
        elif game.credit==0:
            plata_credit=0
        else:
            plata_credit=game.credit
            game.changeStats("credit",-game.credit) # plata integrala
        plata_credit=int(plata_credit)
        # weekly payments
        cashOut=(game.EXP_MAINTENANCE[game.datingStatusLevel]
                +game.EXP_NETWORKING[game.datingStatusLevel]
                +game.EXP_MEDICAL[game.datingStatusLevel]
                +plata_credit)

        #net worth
        #for stocks: total investment matters (not unrealised profit).
        #when you sell stocks for a profit, your networth increases.
        game.netWorth=game.cash+game.stockTotalInvestment+game.deposit+game.bizval-game.credit

        # balance
        balance=cashIn-cashOut
        game.changeStats("cash",balance)
        game.displayStats()

        # afisare EXPENDITURE (jos-dreapta)
        game.lexpenditure.config(text=f"Expenditure\n"
                        f"${cashOut} paid in the last week.\n"
                        f"> Maintenance:    ${game.EXP_MAINTENANCE[game.datingStatusLevel]}\n"
                        f"> Networking:     ${game.EXP_NETWORKING[game.datingStatusLevel]}\n"
                        f"> Medical bills:  ${game.EXP_MEDICAL[game.datingStatusLevel]}\n"
                        f"> Credits:        ${plata_credit}\n" 
                        f"(7% interest and 3% principal)", anchor="nw")
       
        #afisare REVENURE (jos-centru)
        game.lrevenue.config(text=f"Revenue\n"
                             f"${cashIn} received in the last week.\n"
                             f"> Job:    ${game.job}\n"
                             f"> Total profit:    ${profit_total} ({(rand_biz+rand_con)*100}%)\n"
                                     f"  ${profit_biz}({rand_biz*100}%) from business \n"
                                     f"  ${profit_con}({rand_con*100}%) from partners \n"
                                     f"Estimated value of business is {game.bizval}\n"
                                     f"...............................................\n"
                             f"Capitalized interest: ${int(income_deposit)}\n"
                               f"(3% interest from deposits)", anchor="nw")

        # afisare balance (jos-dreapta)
        game.lbalance.config(text=f"Balance: {balance}")
    
        if game.cash<0:
            game.warning+=1
            messagebox.showinfo("Personal Adviser:", f"Cash warning no.{game.warning}/3.\n"
                                "Balance your finance, or you're going bankrupt.")
        else:
            game.warning=0

        if game.energy<1 or game.warning==3:
            # nu poate sa functioneze, pentru ca vine dupa rest (deci energy=min 70)
            game.changeStats("gameon",-1)
            messagebox.showinfo ("General Adviser:",f"You lost the game!\n"
                                            f"Your energy level is {game.energy}."
                                            f"You cash warning is: {game.warning}/3."
                                            f"What were you thinking?")
            game.lbalance.config(text="G A M E   O V E R")

    def rand_biz(self,game): # randamentul afacerii
        # (1) Randamentul din afacere (variaza aleator intre -2.5% si +10%)
        min=-25
        max=100
        value=(random.randint(min,max+2*game.biz))/1000
        value = value * (1+game.bizSkill/50) #2% for each bizSkill
        return value # returneaza procent
        # intre -0,025 si +0,1 (adica intre -2.5% si +10%)
        # nivelul afacerii creste intervalele (ex. pt level 1 randamentul este intre -2,5% si 10,2%)


    def rand_con(self,game): # randamentul din conexiuni
        # (2) Randamentul din conexiuni (plafonat la 7%)
        # maxim 0,03 pe partener (adica 0,2% pe partener)
        rand_con=(random.randint(0,2*game.con))/1000
        if rand_con>1.5:
            rand_con=1.5
        rand_con = rand_con * (1+game.bizSkill/50) #2% for each bizSkill
        return rand_con

    # (4) investitia pentru a ajunge la un anumit nivel
    # exemplu: biz_invest(3) = investitia pt a ajunge la nivelul 3
    def biz_invest(self,nextlevel):
        # returneaza valoarea investitiei necesare pt upgrade next level
        return (nextlevel ** 2) * 7000

    # (5) biz_totalinvest = valoarea cumlata a investitiilor
    def biz_totalinvest(self, level):
        vci=7000
        if level>1:
            # ultima iteratie din range este cu level
            for i in range (2,level+1):
                vci += self.biz_invest(i-1)
                # print (f"vci pt level {i}={vci}")
        return vci

    # calculeaza valoarea afacerii (in cazul vanzarii)
    def biz_val (self, game):
        # factor randament = influenta randamentului anterior asupra valorii actuale
        # variaza intre 0,97 si 1,07 (am facut modificari. plaja de variatie e mai mare)
        if (game.randant < 0):
            factorRandAnt=(random.randint( (1+game.randant)*1000, 1000))/1000
        elif (game.randant > 0):
            factorRandAnt=(random.randint(1000, (1+game.randant)*1000))/1000
        else:
            factorRandAnt = 1
        # print (f"factor randament = {factorRandAnt}")

        #factorCon = influenta conexiunilor asupra valorii actuale
        # variaza intre 0,5 si 2
        # variatia este mai redusa la un numar mai redus de conexiuni
        parteneri=game.con
        if parteneri>500:
            parteneri=500
        if parteneri==0:
            factorCon=1
        elif parteneri<10:
            factorCon = 1 + random.randint((-15 + int(parteneri / 5)), (15 + int(parteneri / 10))) / 100;
        elif parteneri<25:
            factorCon = 1 + random.randint((-30 + int(parteneri / 5)), (30 + int(parteneri / 10))) / 100;
        elif parteneri<40:
            factorCon = 1 + random.randint((-40 + int(parteneri / 5)), (40 + int(parteneri / 10))) / 100;
        else:
            factorCon = 1 + random.randint((-50 + int(parteneri / 5)), (50 + int(parteneri / 10))) / 100;

        # print(f"factor conexiuni = {factorCon}")
        return self.biz_totalinvest(game.biz) * factorRandAnt * factorCon;

# print("Invest for next level=",biz_invest(2))
# print("Total invest=",biz_totalinvest(3))
# print ("Current value=",biz_val())


