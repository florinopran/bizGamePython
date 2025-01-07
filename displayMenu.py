from tkinter import Label, Button

def initializeMenu(self, bank, biz, job, personal, stock, engine): 

    # main labels (general stats)
    self.lstats=Label(text="BizGame", width=10, background="lightgrey", foreground="#4F4F4F",
                        font=("Segoe UI", 11, "bold"))
    self.lstats.place(x=20, y=30)
    self.lenergy=Label(text=f"Energy: {self.energy}", foreground="darkgreen", 
                        font=("Segoe UI", 8,"bold"), anchor="w")
    self.lenergy.place(x=170, y=30)
    self.lcash=Label(text=f"Cash: {self.cash:.2f}", foreground="darkgreen", 
                        font=("Segoe UI", 8,"bold"), anchor="w")
    self.lcash.place(x=320, y=30)
    self.lnetworth=Label(text=f"Net worth: {self.netWorth:.2f}", foreground="darkgreen", 
                        font=("Segoe UI", 8,"bold"), anchor="w")
    self.lnetworth.place(x=440, y=30)
    self.ltime=Label(text=f"Year {(self.time-1)//12+1}. Month {(self.time-1)%12+1}", 
                     foreground="darkgreen", font=("Segoe UI", 8,"bold"), anchor="w")
    self.ltime.place(x=620, y=30)
    
    # secondary labels (describing buttons)
    self.llaborFix=Label(text="🏢 LABOR", width=15, background="darkgrey",  
                            font=("Segoe UI", 8, "bold"))  # LABOR --> Job
    self.llaborFix.place(x=20, y=70)
    self.ljob=Label(text=f"Job: {self.job}", width=15, foreground="darkgreen", 
                    font=("Segoe UI", 8,"bold"), anchor="w")
    self.ljob.place(x=20, y=110)
    self.lstockFix=Label(text="💹 STOCK", background="darkgrey", width=15, 
                            font=("Segoe UI", 8, "bold"))  # STOCK --> Investments
    self.lstockFix.place(x=170, y=70)
    self.lstock=Label(text=f"Stocks: {self.stock}", width=15, foreground="darkgreen", 
                    font=("Segoe UI", 8,"bold"), anchor="w")
    self.lstock.place(x=170, y=110)
    self.lbanksFix=Label(text="🏛️ BANKS", background="darkgrey", width=15, 
                            font=("Segoe UI", 8, "bold"))  # BANKS --> Credits / Deposits
    self.lbanksFix.place(x=320, y=70)
    self.lcredit=Label(text=f"Credits: {self.credit}", width=15, foreground="darkgreen", 
                    font=("Segoe UI", 8,"bold"), anchor="w")
    self.lcredit.place(x=320, y=110)
    self.ldeposit=Label(text=f"Deposits: {int(self.deposit)}", width=15, foreground="darkgreen", 
                    font=("Segoe UI", 8,"bold"), anchor="w")
    self.ldeposit.place(x=320, y=140)
    self.lbusinessFix=Label(text="💡 BUSINESS", background="darkgrey", width=15, 
                            font=("Segoe UI", 8, "bold"))  # BUSINESS --> Level
    self.lbusinessFix.place(x=470, y=70)
    self.lbiz=Label(text=f"level: {self.biz}", width=15, foreground="darkgreen", 
                    font=("Segoe UI", 8,"bold"), anchor="w")
    self.lbiz.place(x=470, y=110)
    self.lsocialFIX=Label(text="🎭 SOCIAL", background="darkgrey", width=15, 
                            font=("Segoe UI", 8, "bold"))  # SOCIAL --> Connexions
    self.lsocialFIX.place(x=620, y=70)
    self.lcon=Label(text=f"Connexions: {self.con}", width=15, foreground="darkgreen", 
                    font=("Segoe UI", 8,"bold"), anchor="w")
    self.lcon.place(x=620, y=110)


            # ----- BUTTONS ------
    # ----- LABOR MARKET: (1) Hire / (2) Resign
    # hire  (20E or 40E/week)  
    self.labelbhire=Label(text="20⚡", width=6, background="lightgreen", foreground="darkred")   
    self.labelbhire.place(x=20,y=180)   
    self.bhire = Button(text=" JOB", width=8, font=("Segoe UI", 8),
                            command=lambda: job.do_bhire(self))   
    self.bhire.place(x=80, y=180)

    # resign  
    self.labelbenergy=Label(text=" 5⚡", width=6, background="lightgreen", foreground="darkred")   
    self.labelbenergy.place(x=20,y=220)  
    self.bresign = Button(text="RESIGN", width=8, font=("Segoe UI", 8),
                            command=lambda: job.do_bresign(self))
    self.bresign.place(x=80, y=220)

    # ----- STOCK MARKET: (1) Invest / (2) Sell
    # invest
    self.labelbinvest=Label(text="10⚡", width=6, background="lightgreen", foreground="darkred")   
    self.labelbinvest.place(x=170,y=180) 
    self.binvest = Button(text="Invest", width=8, font=("Segoe UI", 8),
                            command=lambda: stock.do_binvest(self))
    self.binvest.place(x=230, y=180)
    # sell
    self.labelbsell=Label(text="10⚡", width=6, background="lightgreen", foreground="darkred")   
    self.labelbsell.place(x=170,y=220) 
    self.bsell = Button(text="Sell", width=8, font=("Segoe UI", 8),
                            command=lambda: stock.do_bsell(self))
    self.bsell.place(x=230, y=220)

    # ----- BANK: (1) credit / (2) deposit / (3) withdraw
    # credit
    self.labelbcredit=Label(text="25⚡", width=6, background="lightgreen", foreground="darkred")   
    self.labelbcredit.place(x=320,y=180) 
    self.bcredit = Button(text="Credit", width=8, font=("Segoe UI", 8),
                            command=lambda: bank.do_bcredit(self))
    self.bcredit.place(x=380, y=180)

    # deposit
    self.labelbdeposit=Label(text=" 5⚡", width=6, background="lightgreen", foreground="darkred")   
    self.labelbdeposit.place(x=320,y=220) 
    self.bdeposit = Button(text="Deposit", width=8, font=("Segoe UI", 8),
                            command=lambda: bank.do_bdeposit(self)) 
    self.bdeposit.place(x=380, y=220)

    # withdraw
    self.labelbwithdraw=Label(text=" 5⚡", width=6, background="lightgreen", foreground="darkred")   
    self.labelbwithdraw.place(x=320,y=260) 
    self.bwithdraw = Button(text="Withdraw", width=8, font=("Segoe UI", 8),
                                command=lambda: bank.do_bwithdraw(self))   
    self.bwithdraw.place(x=380, y=260)

    # ----- BUSINESS ARENA
    self.labelbstart=Label(text="35⚡", width=6, background="lightgreen", foreground="darkred")   
    self.labelbstart.place(x=470,y=180) 
    self.bstart = Button(text="Start-Up", width=8, font=("Segoe UI", 8),
                            command=lambda: biz.do_bstart(self,engine))
    self.bstart.place(x=530, y=180)

    self.labelbexpand=Label(text="20⚡", width=6, background="lightgreen", foreground="darkred")   
    self.labelbexpand.place(x=470,y=220) 
    self.bexpand = Button(text="Expand", width=8, font=("Segoe UI", 8),
                            command=lambda: biz.do_bexpand(self,engine))  
    self.bexpand.place(x=530, y=220)

    self.labelbboost=Label(text="20⚡", width=6, background="lightgreen", foreground="darkred")   
    self.labelbboost.place(x=470,y=260) 
    self.bboost = Button(text="Boost", width=8, font=("Segoe UI", 8),
                            command=lambda: biz.do_bboost(self,engine))
    self.bboost.place(x=530, y=260)

    self.labelbscam=Label(text="20⚡", width=6, background="lightgreen", foreground="darkred")   
    self.labelbscam.place(x=470,y=300) 
    self.bscam = Button(text="Scam", width=8, font=("Segoe UI", 8),
                            command=lambda: biz.do_bscam(self,engine))
    self.bscam.place(x=530, y=300)

    self.labelbexit=Label(text="20⚡", width=6, background="lightgreen", foreground="darkred")   
    self.labelbexit.place(x=470,y=340) 
    self.bexit = Button(text="Exit", width=8, font=("Segoe UI", 8),
                            command=lambda: biz.do_bexit(self, engine))
    self.bexit.place(x=530, y=340)

    self.labelbmaster=Label(text="30⚡", width=6, background="lightgreen", foreground="darkred")   
    self.labelbmaster.place(x=470,y=380) 
    self.bmaster = Button(text="Master", width=8, font=("Segoe UI", 8),
                            command=lambda: biz.do_btrain(self, engine))
    self.bmaster.place(x=530, y=380)

    # ----- SOCIAL ARENA 
    self.labelbrest=Label(text="+70⚡", width=6, background="lightgreen", foreground="darkgreen")   
    self.labelbrest.place(x=620,y=180)   
    self.brest = Button(text="Rest", width=8, font=("Segoe UI", 8),
                            command=lambda: personal.do_brest(self, engine))
    self.brest.place(x=680, y=180)

    self.labelbgamble=Label(text=" 5⚡", width=6, background="lightgreen", foreground="darkred")   
    self.labelbgamble.place(x=620,y=220) 
    self.bgamble = Button(text="Gamble", width=8, font=("Segoe UI", 8),
                            command=lambda: personal.do_bgamble(self))
    self.bgamble.place(x=680, y=220)

    self.labelbclub=Label(text="10⚡", width=6, background="lightgreen", foreground="darkred")   
    self.labelbclub.place(x=620,y=260) 
    self.bclub = Button(text="Club", width=8, font=("Segoe UI", 8),
                            command=lambda: personal.do_bclub(self))
    self.bclub.place(x=680, y=260)

    self.labelbcharity=Label(text="20⚡", width=6, background="lightgreen", foreground="darkred")   
    self.labelbcharity.place(x=620,y=300) 
    self.bcharity = Button(text="Charity", width=8, font=("Segoe UI", 8),
                            command=lambda: personal.do_bcharity(self))
    self.bcharity.place(x=680, y=300)

    self.labelbcocaine=Label(text="+50⚡", width=6, background="lightgreen", foreground="darkgreen")   
    self.labelbcocaine.place(x=620,y=340) 
    self.bcocaine = Button(text="Cocaine", width=8, font=("Segoe UI", 8),
                            command=lambda: personal.do_bcocaine(self))
    self.bcocaine.place(x=680, y=340)

    self.labelbsocialize=Label(text="+15⚡", width=6, background="lightgreen", foreground="darkred")   
    self.labelbsocialize.place(x=620,y=380) 
    self.bsocialize = Button(text="Socialize", width=8, font=("Segoe UI", 8),
                            command=lambda: personal.do_btrain(self, engine))
    self.bsocialize.place(x=680, y=380)


    # ----- RETIRMENT: (1) retire / (2) vacation
    self.labelbretire=Label(text="-100⚡", width=6, background="lightgreen", foreground="darkred")   
    self.labelbretire.place(x=770,y=180) 
    self.bretire = Button(text="Retire", width=8, font=("Segoe UI", 8),
                            command=lambda: personal.do_bretire(self,engine))
    self.bretire.place(x=830, y=180)

    self.labelbskip=Label(text="+100⚡", width=6, background="lightgreen", foreground="darkgreen")   
    self.labelbskip.place(x=770,y=220) 
    self.bskip = Button(text="2w Rest", width=8, font=("Segoe UI", 8),
                            command=lambda: personal.do_bvacation(self, engine))
    self.bskip.place(x=830, y=220)