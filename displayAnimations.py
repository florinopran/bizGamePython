from PIL import Image, ImageTk
from tkinter import Label
import os

def initializeAnimations(self):
        # ----- ANIMATION
        #LOGO 
        # imageLogo = Image.open(os.path.join(os.path.dirname(__file__), "img", "logoIcon.png"))
        # imageLogo=imageLogo.resize((190,190))
        # self.photoLogo = ImageTk.PhotoImage(imageLogo)
        # self.photoLabel=Label(self.playground, image=self.photoLogo, width=155, height=155, bg="lightgrey")
        # self.photoLabel.place(x=800, y=20)

        # GOOFY PERSONA
        imageMan = Image.open(os.path.join(os.path.dirname(__file__), "img", "goofy_man.png"))
        imageMan=imageMan.resize((200,260))
        self.photoMan = ImageTk.PhotoImage(imageMan)
        self.labelGoofyMan=Label(self.playground, image=self.photoMan, width=200, height=260, bg="lightgrey")
        self.labelGoofyMan.place(x=780, y=270)

        # GOOFY PERSONA
        imageCouple = Image.open(os.path.join(os.path.dirname(__file__), "img", "goofy_couple.png"))
        self.imgCouple=imageCouple.resize((200,260))
        self.imgCouple = ImageTk.PhotoImage(self.imgCouple)


        # broker
        imgBroker = Image.open(os.path.join(os.path.dirname(__file__), "img", "broker.png"))
        self.imgBroker=imgBroker.resize((100,100))   
        self.imgBroker = ImageTk.PhotoImage(self.imgBroker)
        # bankAdviser
        imgBankAdviser = Image.open(os.path.join(os.path.dirname(__file__), "img", "bank_adviser.png"))
        self.imgBankAdviser=imgBankAdviser.resize((100,100))   
        self.imgBankAdviser = ImageTk.PhotoImage(self.imgBankAdviser)
        # bizAdviser
        imgBizAdviser = Image.open(os.path.join(os.path.dirname(__file__), "img", "biz_adviser.png"))
        self.imgBizAdviser=imgBizAdviser.resize((100,100))   
        self.imgBizAdviser = ImageTk.PhotoImage(self.imgBizAdviser)
        # scamAdviser
        imgScamAdviser = Image.open(os.path.join(os.path.dirname(__file__), "img", "scam_adviser.png"))
        self.imgScamAdviser=imgScamAdviser.resize((100,100))   
        self.imgScamAdviser = ImageTk.PhotoImage(self.imgScamAdviser)
        # image Adviser Young Girl
        imageAdviserYoungGirl = Image.open(os.path.join(os.path.dirname(__file__), "img", "rainbow_girl.png"))
        self.imageAdviserYoungGirl=imageAdviserYoungGirl.resize((100,100)).transpose(Image.FLIP_LEFT_RIGHT)   
        self.imgAdvYoungGirl = ImageTk.PhotoImage(self.imageAdviserYoungGirl) 
        # image Adviser Job
        imageAdviserJob = Image.open(os.path.join(os.path.dirname(__file__), "img", "recruiter.png"))
        self.imageAdviserJob=imageAdviserJob.resize((100,100))   
        self.imgAdvJob = ImageTk.PhotoImage(self.imageAdviserJob)  
        # image Adviser Charity Lady
        imageAdviserCharityLady = Image.open(os.path.join(os.path.dirname(__file__), "img", "charity_lady.png"))
        self.imageAdviserCharityLady=imageAdviserCharityLady.resize((100,100))   
        self.imgAdvCharityLady = ImageTk.PhotoImage(self.imageAdviserCharityLady)     
        # image Adviser Dealer
        imageAdviserDealer = Image.open(os.path.join(os.path.dirname(__file__), "img", "dealer.png"))
        self.imageAdviserDealer=imageAdviserDealer.resize((100,100))   
        self.imgAdvDealer = ImageTk.PhotoImage(self.imageAdviserDealer)  
        
                # image Adviser Scammer
        imageAdviserDrugDealer = Image.open(os.path.join(os.path.dirname(__file__), "img", "drug_dealer.png"))
        self.imageAdviserDrugDealer=imageAdviserDrugDealer.resize((100,100))   
        self.imgAdvDrugDealer = ImageTk.PhotoImage(self.imageAdviserDrugDealer) 

                        # GIRLFRIEND 1
        imageGirlfriend1 = Image.open(os.path.join(os.path.dirname(__file__), "img", "girlfriend1.png"))
        self.imageGirlfriend1=imageGirlfriend1.resize((100,100))   
        self.imgGirlfriend1 = ImageTk.PhotoImage(self.imageGirlfriend1) 

                        # GIRLFRIEND 2
        imageGirlfriend2 = Image.open(os.path.join(os.path.dirname(__file__), "img", "girlfriend2.png"))
        self.imageGirlfriend2=imageGirlfriend2.resize((100,100))   
        self.imgGirlfriend2 = ImageTk.PhotoImage(self.imageGirlfriend2) 

                        # GIRLFRIEND 3
        imageGirlfriend3 = Image.open(os.path.join(os.path.dirname(__file__), "img", "girlfriend3.png"))
        self.imageGirlfriend3=imageGirlfriend3.resize((100,100))   
        self.imgGirlfriend3 = ImageTk.PhotoImage(self.imageGirlfriend3) 

                        # GIRLFRIEND 4
        imageGirlfriend4 = Image.open(os.path.join(os.path.dirname(__file__), "img", "girlfriend4.png"))
        self.imageGirlfriend4=imageGirlfriend4.resize((100,100))   
        self.imgGirlfriend4 = ImageTk.PhotoImage(self.imageGirlfriend4) 

                        # GIRLFRIEND 5
        imageGirlfriend5 = Image.open(os.path.join(os.path.dirname(__file__), "img", "girlfriend5.png"))
        self.imageGirlfriend5=imageGirlfriend5.resize((100,100))   
        self.imgGirlfriend5 = ImageTk.PhotoImage(self.imageGirlfriend5) 


                # image Adviser Old Man
        imageAdviserOld = Image.open(os.path.join(os.path.dirname(__file__), "img", "old_man.png"))
        imageAdviserOld=imageAdviserOld.resize((100,100))
        self.imageAdviserOld=imageAdviserOld.transpose(Image.FLIP_LEFT_RIGHT)
        self.imgAdvOld = ImageTk.PhotoImage(self.imageAdviserOld)

                # image Adviser Advisers Hall
        imageAdvisersHall = Image.open(os.path.join(os.path.dirname(__file__), "img", "advisers_hall.png"))
        self.imageAdvisersHall=imageAdvisersHall.resize((100,100))
        self.imgAdvHall = ImageTk.PhotoImage(self.imageAdvisersHall)

                # call Adviser Icon (after each Rest)
        imageCallAdviserIcon = Image.open(os.path.join(os.path.dirname(__file__), "img", "call_adviser_icon.png"))
        self.imageCallAdviserIcon=imageCallAdviserIcon.resize((100,100))
        self.imgCallAdviserIcon = ImageTk.PhotoImage(self.imageCallAdviserIcon)

                # place Adviser Image        
        self.lAdviser=Label(self.playground, image=self.imgAdvHall, width=100, height=100, bg="lightgrey")
        self.lAdviser.place(x=560, y=428)

                        # xMark (used to exit the window)
        xMarkimage = Image.open(os.path.join(os.path.dirname(__file__), "img", "xMark.png"))
        self.xMark=xMarkimage.resize((25,25))   
        self.xMark = ImageTk.PhotoImage(self.xMark) 