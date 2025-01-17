from PIL import Image, ImageTk
from tkinter import Label, Canvas
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
        imageMan=imageMan.resize((180,230)).convert("RGBA")
        self.personaSingle = ImageTk.PhotoImage(imageMan)


        # GOOFY PERSONA
        imageCouple = Image.open(os.path.join(os.path.dirname(__file__), "img", "goofy_couple.png"))
        self.imgCouple=imageCouple.resize((200,230)).convert("RGBA")
        self.personaCouple = ImageTk.PhotoImage(self.imgCouple)

        # LOGO
        tempImgLogo = Image.open(os.path.join(os.path.dirname(__file__), "img", "logo_image.png"))
        tempImgLogo=tempImgLogo.resize((130,42)).convert("RGBA")
        self.imgLogo = ImageTk.PhotoImage(tempImgLogo)

        # ************************ ADVISERS ************************************

        # broker
        imgBroker = Image.open(os.path.join(os.path.dirname(__file__), "img", "broker.png"))
        self.imgBroker=imgBroker.resize((100,100))   
        self.brokerAdviser = ImageTk.PhotoImage(self.imgBroker)
        # bankAdviser
        imgBankAdviser = Image.open(os.path.join(os.path.dirname(__file__), "img", "bank_adviser.png"))
        self.imgBankAdviser=imgBankAdviser.resize((100,100))   
        self.bankAdviser = ImageTk.PhotoImage(self.imgBankAdviser)
        # businessAdviser
        imgBizAdviser = Image.open(os.path.join(os.path.dirname(__file__), "img", "biz_adviser.png"))
        self.imgBizAdviser=imgBizAdviser.resize((100,100))   
        self.businessAdviser = ImageTk.PhotoImage(self.imgBizAdviser)
        # scamAdviser
        imgScamAdviser = Image.open(os.path.join(os.path.dirname(__file__), "img", "scam_adviser.png"))
        self.imgScamAdviser=imgScamAdviser.resize((100,100))   
        self.scamAdviser = ImageTk.PhotoImage(self.imgScamAdviser)
        # image Adviser Job
        imageAdviserJob = Image.open(os.path.join(os.path.dirname(__file__), "img", "recruiter.png"))
        self.imageAdviserJob=imageAdviserJob.resize((100,100))   
        self.jobAdviser = ImageTk.PhotoImage(self.imageAdviserJob)  
        # image Adviser Charity Lady
        imageAdviserCharityLady = Image.open(os.path.join(os.path.dirname(__file__), "img", "charity_lady.png"))
        self.imageAdviserCharityLady=imageAdviserCharityLady.resize((100,100))   
        self.charityLadyAdviser = ImageTk.PhotoImage(self.imageAdviserCharityLady)     
        # image Adviser Drug Dealer
        imageAdviserDrugDealer = Image.open(os.path.join(os.path.dirname(__file__), "img", "drug_dealer.png"))
        self.imageAdviserDrugDealer=imageAdviserDrugDealer.resize((100,100))   
        self.drugDealerAdviser = ImageTk.PhotoImage(self.imageAdviserDrugDealer) 
        # image Adviser Old Man
        imageAdviserOld = Image.open(os.path.join(os.path.dirname(__file__), "img", "old_man.png"))
        imageAdviserOld=imageAdviserOld.resize((100,100))
        self.imageAdviserOld=imageAdviserOld.transpose(Image.FLIP_LEFT_RIGHT)
        self.oldManAdviser = ImageTk.PhotoImage(self.imageAdviserOld)
                # image Adviser Advisers Hall
        # imageAdvisersHall = Image.open(os.path.join(os.path.dirname(__file__), "img", "advisers_hall.png"))
        # self.imageAdvisersHall=imageAdvisersHall.resize((100,100))
        # self.imgAdvHall = ImageTk.PhotoImage(self.imageAdvisersHall)
        # call Adviser Icon (after each Rest)
        imageCallAdviserIcon = Image.open(os.path.join(os.path.dirname(__file__), "img", "call_adviser_icon.png"))
        self.imageCallAdviserIcon=imageCallAdviserIcon.resize((100,100))
        self.callAdviser = ImageTk.PhotoImage(self.imageCallAdviserIcon)
        # image Adviser Young Girl
        imageAdviserYoungGirl = Image.open(os.path.join(os.path.dirname(__file__), "img", "rainbow_girl.png"))
        self.imageAdviserYoungGirl=imageAdviserYoungGirl.resize((100,100)).transpose(Image.FLIP_LEFT_RIGHT).convert("RGBA")   
        self.youngGirlAdviser = ImageTk.PhotoImage(self.imageAdviserYoungGirl) 
        # image Adviser Dealer
        imageAdviserDealer = Image.open(os.path.join(os.path.dirname(__file__), "img", "dealer.png"))
        self.imageAdviserDealer=imageAdviserDealer.resize((100,100)).convert("RGBA")   
        self.dealerAdviser = ImageTk.PhotoImage(self.imageAdviserDealer) 





        # ************************ G I R L F R I E N D  ************************************

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


        # ************************   E N V I R O N M E N T S ************************************
        # image club environment - JPG
        clubEnvironmentImage = Image.open(os.path.join(os.path.dirname(__file__), "img", "club_environment.jpg"))
        clubEnvironmentImage=clubEnvironmentImage.resize((515,220)).convert("RGBA")
        self.clubEnvironment = ImageTk.PhotoImage(clubEnvironmentImage)

        # image socialize environment
        socializeEnvironmentImage = Image.open(os.path.join(os.path.dirname(__file__), "img", "socialize_environment.png"))
        socializeEnvironmentImage=socializeEnvironmentImage.resize((515,220)).convert("RGBA")
        self.socializeEnvironment = ImageTk.PhotoImage(socializeEnvironmentImage)

        # image bedroom environment
        bedroomEnvironmentImage = Image.open(os.path.join(os.path.dirname(__file__), "img", "bedroom_environment.jpg"))
        bedroomEnvironmentImage=bedroomEnvironmentImage.resize((515,220)).convert("RGBA")
        self.bedroomEnvironment = ImageTk.PhotoImage(bedroomEnvironmentImage)

         # image backstreet environment
        backstreetEnvironmentImage = Image.open(os.path.join(os.path.dirname(__file__), "img", "backstreet_environment.jpg"))
        backstreetEnvironmentImage=backstreetEnvironmentImage.resize((515,220)).convert("RGBA")
        self.backstreetEnvironment = ImageTk.PhotoImage(backstreetEnvironmentImage)

         # image casino environment
        casinoEnvironmentImage = Image.open(os.path.join(os.path.dirname(__file__), "img", "casino_environment.jpg"))
        casinoEnvironmentImage=casinoEnvironmentImage.resize((515,220)).convert("RGBA")
        self.casinoEnvironment = ImageTk.PhotoImage(casinoEnvironmentImage)

         # image charity environment
        charityEnvironmentImage = Image.open(os.path.join(os.path.dirname(__file__), "img", "charity_environment.jpg"))
        charityEnvironmentImage=charityEnvironmentImage.resize((515,220)).convert("RGBA")
        self.charityEnvironment = ImageTk.PhotoImage(charityEnvironmentImage)

         # image job environment
        jobEnvironmentImage = Image.open(os.path.join(os.path.dirname(__file__), "img", "job_environment.png"))
        jobEnvironmentImage=jobEnvironmentImage.resize((515,220)).convert("RGBA")
        self.jobEnvironment = ImageTk.PhotoImage(jobEnvironmentImage)

         # image business environment
        businessEnvironmentImage = Image.open(os.path.join(os.path.dirname(__file__), "img", "business_environment.jpg"))
        businessEnvironmentImage=businessEnvironmentImage.resize((515,220)).convert("RGBA")
        self.businessEnvironment = ImageTk.PhotoImage(businessEnvironmentImage)

         # image bank environment
        bankEnvironmentImage = Image.open(os.path.join(os.path.dirname(__file__), "img", "bank_environment.png"))
        bankEnvironmentImage=bankEnvironmentImage.resize((515,220)).convert("RGBA")
        self.bankEnvironment = ImageTk.PhotoImage(bankEnvironmentImage)

         # image stock environment
        stockEnvironmentImage = Image.open(os.path.join(os.path.dirname(__file__), "img", "stock_environment.png"))
        stockEnvironmentImage=stockEnvironmentImage.resize((515,220)).convert("RGBA")
        self.stockEnvironment = ImageTk.PhotoImage(stockEnvironmentImage)

        # ************************   End of environments ************************************
        


        


        # Create Canvas (Enivornment , Advise , Persona)
        self.canvasContainer = Canvas(self.playground, width=515, height=260, highlightthickness=0, background="lightgray")
        self.canvasContainer.place(x=455, y=310)
        self.canvasLogo=Canvas(self.playground, width=253, height=70, highlightthickness=0, background="lightgrey")
        self.canvasLogo.place(x=1,y=1)
        # self.canvasLogo.lift()
        # ************************    Set Logo Image   **************************************
        self.logoC=self.canvasLogo.create_image(17, 17, image=self.imgLogo, anchor="nw")
        # ***********************************************************************************  
        # ************************    Set initial Enivornment Image   ***********************
        self.environmentC=self.canvasContainer.create_image(0, 0, image=self.bedroomEnvironment, anchor="nw")
        # ***********************************************************************************   
        #              
        # ****************************    Set initial Adviser Image   ***********************
        self.adviserC=self.canvasContainer.create_image(70,120, image=self.oldManAdviser, anchor="nw")
        # self.lAdviser=Label(self.playground, image=self.imgAdvDealer, width=100, height=100)
        # self.lAdviser.place(x=560, y=428)   
        # ***********************************************************************************      
        # ****************************    Set initial Persona Image   ***********************
        self.personaC=self.canvasContainer.create_image(325,0, image=self.personaSingle, anchor="nw")
 
        # *********************************************************************************** 






                        # xMark (used to exit the window)
        xMarkimage = Image.open(os.path.join(os.path.dirname(__file__), "img", "xMark.png"))
        self.xMark=xMarkimage.resize((25,25))   
        self.xMark = ImageTk.PhotoImage(self.xMark) 


        #  # Create a Canvas widget
        # self.canvas = Canvas(width=540, height=200, bg="blue")
        # self.canvas.lower()
        # self.canvas.place(x=450, y=350)