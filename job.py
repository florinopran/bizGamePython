# from box import box_news, box
from display import *
from tkinter import messagebox, simpledialog
from displayOptBox import *
import random


def do_bhire(game):
    game.canvasContainer.itemconfig(game.adviserC, image=game.jobAdviser)
    game.canvasContainer.itemconfig(game.environmentC, image=game.jobEnvironment) 
    
    hideYesNoEntry(game)    
       
    def actionHire(game, opt):
        hideYesNoEntry(game)
        message="Mr. Smith:\n"
        if opt=="yes":            
            game.changeStats("energy", -20)          
            if game.job > 0:
                wage=game.job # your current salary
                if random.randint(1,2)==1: # 50% chances to receive an offer
                    x=int(game.socialSkill*0.2) # => 50 social skill = max 10% raise
                    wageRaise=min(random.randint(0,x)+1, 11) # max raise = 11% (based on socialSkills)
                    wageCut=random.randint(-wageRaise,0)                    
                    wageChange=1+(random.randint(wageCut,wageRaise))/100                    
                    wageOffer=int(wage*wageChange)
                    newEnergyLevel=random.randint(game.jobEnergy-3,game.jobEnergy+5)
                    if newEnergyLevel<30:
                        newEnergyLevel=30
                    elif newEnergyLevel>60:
                        newEnergyLevel=60
                    energyChange=newEnergyLevel-game.jobEnergy                                       
                    message+=f"You have a ${wageOffer} offer."\
                            f"\nMonthly energy needed={newEnergyLevel}(change={energyChange})"\
                             "\nWill you accept the offer?"
                    game.lAdviserBox.config(text=message)
                    def actionJobOffer(game,response):
                        hideYesNoEntry(game)
                        if response=="yes":
                            game.changeStats("job",-game.job+wageOffer)
                            game.changeStats("jobEnergy",energyChange)
                            game.changeStats("jobSalaryLevel",-game.jobSalaryLevel+wageOffer)
                            game.lAdviserBox.config(
                                text=f"Personal Recruiter Smith:\nCongratulations!"\
                                    f"\nYou now have a ${game.job} salary."
                                    f"\nYou need {game.jobEnergy}% of your monthly energy for this job."
                                            )
                        else:
                            game.lAdviserBox.config(
                                text=f"Mr. Smith:\nNo change!")
                    activateYesNo(game,actionJobOffer)    
                else:
                    game.lAdviserBox.config(text="Mr. Smith:\nThere is no offer for you!")
            else:                
                message+=f"You accepted an ${game.jobSalaryLevel} offer."\
                        f"\nEnergy needed for this job: {game.jobEnergy}."
                game.lAdviserBox.config(text=message)
                game.changeStats("job",game.jobSalaryLevel)                                     
            game.displayStats()  # refresh la scor
        elif opt=="no":
            message="Please come back if you want a job!"
            game.lAdviserBox.config(text=message)  
    
    jobTalk=1 # discussion possible    
    if game.job==0: #don't have a job
        message="Personal Recruiter Smith:"\
                 "\nDo you need a job?"                
        game.lAdviserBox.config(text=message)
    else: #don't have a job
        message="Smith, from the office:"
        if game.jobLastOffer>=game.time-1: # recently negociated
            message+=f"\nWe negociated your salary {game.time-game.jobLastOffer} month(s) ago." 
            jobTalk=0
        if game.jobSeniority<4: # low seniority
            message+=f"\nYoung man, you have only a {game.jobSeniority} months experience."\
                "\nAt least have the decency to work \n4 months before you ask for a raise." 
            jobTalk=0
    if jobTalk==0:    
        message+=f"\nJust go to work, do a good job and gain seniority."\
                                f"\n (seniority={game.jobSeniority})"\
                                f"\n (energy consumption={game.jobEnergy})"
        game.lAdviserBox.config(text=message)
    else: #Talk possible (to hire / renegociate)
        game.lAdviserBox.config(text="Smith, from the office:\nI understand that you want a better offer?")
        activateYesNo (game, actionHire)

# RESIGN (JOB)
def do_bresign(game):
    game.canvasContainer.itemconfig(game.adviserC, image=game.jobAdviser)
    game.canvasContainer.itemconfig(game.environmentC, image=game.jobEnvironment) 
    def actionResign(game, opt):
        hideYesNoEntry(game)
        message="Personal Recruiter Smith:\n"
        if opt=="yes":
            if game.job>0:
                game.changeStats("job", -game.job)
                game.changeStats("energy", -5)                
                message+="You left your job. Take care!"
            elif game.job==0:
                message+=f"You don't even have a job. Get serious!"
            game.displayStats()  # refresh la scor
        elif opt=="no":
            message+="Good choice to keep your job."
        game.lAdviserBox.config(text=message)  
    activateYesNo (game, actionResign)






