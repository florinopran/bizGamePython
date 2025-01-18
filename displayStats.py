class DisplayStats():
    
    def __init__(self):
        # Initialize all game-related stats
        self.time = 1
        self.energy = 100
        self.cash = 100
        self.job = 0        
        self.credit = 0
        self.deposit = 200
        self.biz = 0
        self.con = 1
        self.randant = 0
        self.bizval = 0
        self.gameOn = 1
        self.cocainePP = 0.1
        self.cocaineMin = 500
        self.warning = 0
        self.bizSkill = 1
        self.scamSkill = 1
        self.socialSkill = 1 
        self.EXP_MAINTENANCE    =[600,750,1000,1200,1500,750]
        self.EXP_NETWORKING     =[ 50, 65,130,150, 300,100]
        self.EXP_MEDICAL        =[ 50, 75,150,175, 200,100]

        self.stock = 0 # Total investition (shares)
        self.stockTotalInvestment=0      # =self.stock * value when bought
        self.stockIndexRV=100.00    # stock index real value (how much it should be) - updated in engine
        self.stockIndexMV=100.00    # stock index market value (how much currently is) - updated in engine
        self.stockNormalPerformance=0.05 # stock performance (it's actually a random -1 to 5%)

        #bank
        self.interest=0.02   
    

        #job
        self.jobSeniority=0 # time worked (updated in engine)
        self.jobLastOffer=1 # moment you asked for an offer (update in job, based on self.time)
        self.jobSalaryLevel=1000 # if you resign, you keep your job salary level (updated in job)    
        self.jobEnergy=45 # job energy consumption (may vary between 30pp and 60pp)


        #relations
        self.IMPACT_NETWORKING  =[ 1.00 , 1.05 , 1.25 , 1.50 , 2.00 , 1.50]
        self.STATUS_OPTIONS = [
            "single", "dating a college girl", "dating a lady",
            "engaged", "married", "divorced"
        ]
        self.RELATION_BENCHMARKS = {
        0: "Nobody loves you",    
        10: "is just hanging around \nwith you",
        20: "is starting to care \nfor you",
        30: "enjoys your company \ndeeply",
        40: "feels truly comfortable \nwith you",
        50: "loves you",
        60: "loves and respects you",
        70: "loves and support you",
        80: "cherishes \nyour relationship",
        90: "is deeply devoted \nto you",
        100: "adores you \ncompletely"
        }
        self.girlfriendName=""
        self.girlfriendFeelings=""
        self.datingStatusLevel=0
        self.relationScore=0
        self.status = self.STATUS_OPTIONS[self.datingStatusLevel]

        

        self.opt = None

        # how much do you actually worth
        self.netWorth=self.cash+self.stockTotalInvestment+self.deposit+self.bizval-self.credit 
        
