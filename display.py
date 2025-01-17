from tkinter import *
from PIL import Image, ImageTk
import job, stock, bank, biz, personal
import constants
from engine import Engine
import random

# import os
# from optBox import *
# import optBox
#TODO should change name for DisplayStats(also have a function with same name)
from displayStats import DisplayStats 
import displayAnimations
import displayBoxes
import displayMenu
import displayOptBox

# optBox=OptBox()
engine=Engine() #initialize a unique instance of Engine() class


class Playground(DisplayStats):    
    def __init__(self):
        super().__init__()  # Initialize all atributes from inherited classes (ex. DisplayStats)
        # DisplayStats.__init__(self)       

        self.testare=1 # doar pentru test
        # initialize tkinter module        
        self.playground=Tk()        
        self.playground.geometry("1000x800")
        self.playground.config(bg="lightgrey")
        self.playground.title("BizAdviser Beta V03.8.2") 

        self.testVar=1
        # STATS         
        # displayStats.initializeStats(self)    
        displayAnimations.initializeAnimations(self)
        displayBoxes.initializeBoxes(self)
        displayMenu.initializeMenu(self, bank, biz, job, personal, stock, engine)        
        displayOptBox.initializeOptBox(self)



        # ----- SKILL LABELS
        self.labelskills=Label(text=f"💰Biz  Skill={self.bizSkill}\n" 
                                    f"🥷Scam Skill={self.scamSkill}\n" 
                                    f"🎭Soc  Skill={self.socialSkill}\n"
                                    f"💘Status={self.status}\n"
                                    f"{self.girlfriendName} {self.girlfriendFeelings}", 
                               width=26, height=6, font=("Segoe UI", 7), anchor="nw", justify="left",
                               background="white", foreground="darkgreen")
        self.labelskills.place(x=780, y=40)
        
       

        # self.write(f"STATS: FULL Energy, $1000 cash and 162 weeks",\
        #            font=("arial", 10, "normal"))
        self.playground.mainloop()


    def displayStats(self):        
        
        self.lenergy.config(text=f"ENERGY:{self.energy}")
        self.lcash.config(text=f"CASH:${self.cash:.0f}") 
        self.lnetworth.config(text=f"Net worth:${self.netWorth:.0f}")       
        self.ltime.config(text=f"Year {(self.time-1)//12+1}. Month {(self.time-1)%12+1}")
        self.ljob.config(text=f"Job:${self.job:.0f}")
        self.lstock.config(text=f"Stocks:{self.stock}")
        self.lcredit.config(text=f"Credits:${self.credit:.0f}")
        self.ldeposit.config(text=f"Deposits:${self.deposit:.0f}")
        self.lbiz.config(text=f"LEVEL:{self.biz}")
        self.lcon.config(text=f"Connexions:{self.con}")
        self.labelskills.config(text=f"💰Biz  Skill={self.bizSkill}\n" 
                                    f"🥷Scam Skill={self.scamSkill}\n" 
                                    f"🎭Soc  Skill={self.socialSkill}\n"
                                    f"💘Status={self.status} ({self.relationScore})\n"
                                    f"{self.girlfriendName} {self.girlfriendFeelings}")


    def adjustGirlfriendFeelings(self): # based on relationScore
        theKey=max([key for key in self.RELATION_BENCHMARKS if key <= self.relationScore]) 
        self.girlfriendFeelings=self.RELATION_BENCHMARKS[theKey]   

    #TODO aceasta este noua functie de schimbare a valorilor
    def changeStats(self, stat, value):
        value=int(value)

        if stat=="gameOn":
            self.gameOn=value
        
        if self.gameOn==0:
            value=0 # no more updates

        if stat=="time":
            self.time+=value
            
        if stat=="energy":
            self.energy+=value
            if self.energy>100:
                self.energy=100
            if self.energy<=0:
                print("No more energy. Try cocaine!")
                self.energy=0
                

        if stat == "cash":
            self.cash += value
        if stat == "job":
            self.job+=value
        if stat == "jobSeniority":
            self.jobSeniority+=value
        if stat == "jobLastOffer":
            self.jobLastOffer+=value
        if stat == "jobSalaryLevel":
            self.jobSalaryLevel+=value
        if stat == "jobEnergy":
            self.jobEnergy+=value
        
        if stat == "stock":
            self.stock += value
        if stat == "credit":
            self.credit += value
        if stat == "deposit":
            self.deposit += value
        if stat == "biz":
            self.biz += value
        if stat == "con":
            self.con += value

        if stat=="socialSkill":
            self.socialSkill+=value
        if stat=="bizSkill":
            self.bizSkill+=value
        if stat=="scamSkill":
            self.scamSkill+=value

        if stat=="girlfriendName":
            self.girlfriendName=random.choice(constants.GIRLFRIEND_NAMES)

        if stat=="relationScore":
            self.relationScore+=value   
            self.adjustGirlfriendFeelings()  
                                   
        
        if stat=="datingStatusLevel":            
            if self.datingStatusLevel==0 and value==1: # new girlfriend
                self.girlfriendName=random.choice(constants.GIRLFRIEND_NAMES)
                self.relationScore=11
                self.girlfriendFeelings=self.RELATION_BENCHMARKS[10]
            #make the change                
            self.datingStatusLevel+=value #change dating status level            
            self.status=self.STATUS_OPTIONS[self.datingStatusLevel] #change status
            if value>0: #increase connections due to relation
                self.con=int(self.con*self.IMPACT_NETWORKING[self.datingStatusLevel])
            else: #decrease connections due to breakup
                self.con=int(self.con/self.IMPACT_NETWORKING[self.datingStatusLevel])

            #reached the engagement level
            if self.datingStatusLevel==3 and value>0: #engagement ring ($10.000) - on credit
                self.credit+=10000
            #reached the married level
            if self.datingStatusLevel==4 and value>0: #wedding ($10.000+0.1*netWorth)
                self.credit+=10000 + self.netWorth*0.1
            #reached the single status
            if self.datingStatusLevel==0:
                self.girlfriendName="" #you have no girlfriend
                self.girlfriendFeelings=""
                self.relationScore=0
            #reached the divorce level
            if self.datingStatusLevel==5: #divorce (-10.000 - 0.5 *netWorth)    
                self.credit+=10000 + max(self.netWorth*0.5 , 1) # not less then 10.001 
                self.girlfriendFeelings="You feel kind of bitter." 
                self.relationScore=0
        self.displayStats() #display it        
            

# create a common instance of Stats() class
# stats=Stats()





