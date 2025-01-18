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

        if stat=="relationScore": # not important
            self.relationScore+=value   
            self.adjustGirlfriendFeelings()  
                                   
        
        if stat=="datingStatusLevel": # important 
            def becomeSingle():
                self.datingStatusLevel=0
                self.status=self.STATUS_OPTIONS[self.datingStatusLevel] #change status to single
                self.girlfriendName="" # no more girlfriend
                self.relationScore=0  # no relation       
                self.girlfriendFeelings="Single and ready to mingle😎"                
            def newGirlfriend():
                self.datingStatusLevel+=value #change dating status level  
                self.status=self.STATUS_OPTIONS[self.datingStatusLevel] #change status eg. dating a college girl
                self.girlfriendName=random.choice(constants.GIRLFRIEND_NAMES)
                self.relationScore=11 # new relation
                self.girlfriendFeelings=self.RELATION_BENCHMARKS[10] 
            def downgradeRelation():
                self.datingStatusLevel+=value #downgrade dating status level  
                self.status=self.STATUS_OPTIONS[self.datingStatusLevel] #change status eg. dating a college girl
                # self.grilfriendName   = no change
                # self.relationScore    = no change
                # self.girlfriendFeelings modified from relation score 
            def upgradeRelation():
                self.datingStatusLevel+=value #upgrade dating status level  
                self.status=self.STATUS_OPTIONS[self.datingStatusLevel] #change status eg. dating a college girl
                # self.grilfriendName   = no change
                # self.relationScore    = no change
                # self.girlfriendFeelings modified from relation score 
            def divorce():
                self.datingStatusLevel=5 #downgrade dating status level  
                self.status=self.STATUS_OPTIONS[self.datingStatusLevel] #change status to divorced
                self.girlfriendName   = ""
                self.relationScore    = 0
                self.girlfriendFeelings = "You feel kind of bitter."
                #divorce (-10.000 - 0.5 *netWorth)    
                self.credit+=10000 + max(self.netWorth*0.5 , 1) # not less then 10.001 
            def engage():
                self.datingStatusLevel=3 # reach engagement level  
                self.status=self.STATUS_OPTIONS[self.datingStatusLevel] #change status eg. dating a college girl
                # self.grilfriendName   = no change
                # self.relationScore    = no change
                self.girlfriendFeelings = "You feel kind of bitter."
                self.credit+=10000 #engagement ring
            def marry():
                self.datingStatusLevel=4 # marry level  
                self.status=self.STATUS_OPTIONS[self.datingStatusLevel] #change status eg. dating a college girl
                self.grilfriendName   = ""
                self.relationScore    = 0
                self.girlfriendFeelings = "You feel kind of bitter."                
                self.credit+=10000 + self.netWorth*0.1 #wedding ($10.000+0.1*netWorth)
            
            modifyOnce=0
            # New girlfriend? (from single)                    
            if self.datingStatusLevel==0 and value==1 and modifyOnce==0: 
                modifyOnce=1
                newGirlfriend()  
            
            # Upgrade girlfriend relation? (from 1)                    
            if self.datingStatusLevel==1 and value==1 and modifyOnce==0: # advance, but not engage 
                modifyOnce=1
                upgradeRelation()  
            
            # New girlfriend? (from divorced)              
            if self.datingStatusLevel==5 and value==1 and modifyOnce==0: 
                modifyOnce=1
                self.datingStatusLevel=0 # start all over again (from single)
                newGirlfriend()  

            #break up (but not married <4) => become single
            elif self.datingStatusLevel>0 and self.datingStatusLevel<4 and\
                  self.datingStatusLevel==-value and modifyOnce==0:     
                modifyOnce=1
                becomeSingle()   
            
            #break up (divorce) => become single
            elif self.datingStatusLevel>0 and self.datingStatusLevel==4 and\
                  self.datingStatusLevel==-value and modifyOnce==0:   
                modifyOnce=1  
                divorce() 

            #downgrade with 1 level (but not married <4) => don't become single
            elif self.datingStatusLevel>0 and self.datingStatusLevel<4 and \
                    value==-1 and modifyOnce==0:
                modifyOnce=1
                downgradeRelation()                             
                
            #Old girlfriend (upgrade/downgrade)
            if self.datingStatusLevel==2 and value==1 and modifyOnce==0: #engagement
                modifyOnce=1
                engage()

            if self.datingStatusLevel==3 and value==1 and modifyOnce==0: #marry
                modifyOnce=1
                marry()                      
            
            # change in connections (only if value!=0)     
            if value>0: #increase connections due to relation
                self.con=int(self.con*self.IMPACT_NETWORKING[self.datingStatusLevel])
            if value<0: #decrease connections due to breakup
                self.con=int(self.con/self.IMPACT_NETWORKING[self.datingStatusLevel])

        self.displayStats() #display it        
            

# create a common instance of Stats() class
# stats=Stats()





