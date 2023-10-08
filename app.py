from customtkinter import *

class Main(CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("360x435")
        self.resizable(False,False)
        self.rowconfigure(1,weight=1)
        self.columnconfigure(0,weight=1)
        self.opButtonColors="#cc9a0f"
        self.hoverColor="black"
        self.textVar="0"
        self.operator=""
        self.firstValue="0"
    
        self.label=CTkLabel(self,text=self.textVar,anchor="e",fg_color="#544f52",corner_radius=10,height=75,font=CTkFont("Impact",35))
        self.label.grid(row=0,column=0,padx=10,pady=10,sticky="ew")
        
        self.lowerFrame=CTkFrame(self,border_width=0,fg_color="transparent")
        self.lowerFrame.grid(row=1,column=0,padx=10,sticky="nsew")
        self.lowerFrame.rowconfigure(3,weight=1)
        self.lowerFrame.columnconfigure(4,weight=1)
        
        self.button9=CTkButton(self.lowerFrame,text="9",fg_color="blue",hover_color=self.hoverColor,width=75,height=75,font=CTkFont("Impact",35),command=lambda :self.pressNumber("9"))
        self.button9.grid(row=0,column=2,padx=5,pady=5)
        
        self.button8=CTkButton(self.lowerFrame,text="8",fg_color="blue",hover_color=self.hoverColor,width=75,height=75,font=CTkFont("Impact",35),command=lambda :self.pressNumber("8"))
        self.button8.grid(row=0,column=1,padx=5,pady=5)
        
        self.button7=CTkButton(self.lowerFrame,text="7",fg_color="blue",hover_color=self.hoverColor,width=75,height=75,font=CTkFont("Impact",35),command=lambda :self.pressNumber("7"))
        self.button7.grid(row=0,column=0,padx=5,pady=5)
        
        self.buttonSum=CTkButton(self.lowerFrame,text="+",fg_color=self.opButtonColors,hover_color=self.hoverColor,width=75,height=75,font=CTkFont("Impact",50),command=self.pressSum)
        self.buttonSum.grid(row=0,column=3,padx=5,pady=5)
        
        self.button6=CTkButton(self.lowerFrame,text="6",fg_color="blue",hover_color=self.hoverColor,width=75,height=75,font=CTkFont("Impact",35),command=lambda :self.pressNumber("6"))
        self.button6.grid(row=1,column=2,padx=5,pady=5)
        
        self.button5=CTkButton(self.lowerFrame,text="5",fg_color="blue",hover_color=self.hoverColor,width=75,height=75,font=CTkFont("Impact",35),command=lambda :self.pressNumber("5"))
        self.button5.grid(row=1,column=1,padx=5,pady=5)
        
        self.button4=CTkButton(self.lowerFrame,text="4",fg_color="blue",hover_color=self.hoverColor,width=75,height=75,font=CTkFont("Impact",35),command=lambda :self.pressNumber("4"))
        self.button4.grid(row=1,column=0,padx=5,pady=5)
        
        self.buttonMin=CTkButton(self.lowerFrame,text="-",fg_color=self.opButtonColors,hover_color=self.hoverColor,width=75,height=75,font=CTkFont("Impact",50),command=self.pressMin)
        self.buttonMin.grid(row=1,column=3,padx=5,pady=5)
        
        self.button3=CTkButton(self.lowerFrame,text="3",fg_color="blue",hover_color=self.hoverColor,width=75,height=75,font=CTkFont("Impact",35),command=lambda :self.pressNumber("3"))
        self.button3.grid(row=2,column=2,padx=5,pady=5)
        
        self.button2=CTkButton(self.lowerFrame,text="2",fg_color="blue",hover_color=self.hoverColor,width=75,height=75,font=CTkFont("Impact",35),command=lambda :self.pressNumber("2"))
        self.button2.grid(row=2,column=1,padx=5,pady=5)
        
        self.button1=CTkButton(self.lowerFrame,text="1",fg_color="blue",hover_color=self.hoverColor,width=75,height=75,font=CTkFont("Impact",35),command=lambda :self.pressNumber("1"))
        self.button1.grid(row=2,column=0,padx=5,pady=5)
        
        self.buttonDiv=CTkButton(self.lowerFrame,text="/",fg_color=self.opButtonColors,hover_color=self.hoverColor,width=75,height=75,font=CTkFont("Arial",50),command=self.pressDiv)
        self.buttonDiv.grid(row=2,column=3,padx=5,pady=5)
        
        self.buttonClr=CTkButton(self.lowerFrame,text="C",fg_color=self.opButtonColors,hover_color=self.hoverColor,width=75,height=75,font=CTkFont("Arial",35),command=self.pressC)
        self.buttonClr.grid(row=3,column=0,padx=5,pady=5)
        
        self.button0=CTkButton(self.lowerFrame,text="0",fg_color="blue",hover_color=self.hoverColor,width=75,height=75,font=CTkFont("Impact",35),command=lambda :self.pressNumber("0"))
        self.button0.grid(row=3,column=1,padx=5,pady=5)
                
        self.buttonRes=CTkButton(self.lowerFrame,text="=",fg_color=self.opButtonColors,hover_color=self.hoverColor,width=75,height=75,font=CTkFont("Impact",35),command=self.pressRes)
        self.buttonRes.grid(row=3,column=2,padx=5,pady=5)
        
        self.buttonMul=CTkButton(self.lowerFrame,text="X",fg_color=self.opButtonColors,hover_color=self.hoverColor,width=75,height=75,font=CTkFont("Arial",35),command=self.pressMul)
        self.buttonMul.grid(row=3,column=3,padx=5,pady=5)
        
        def press1(event):
            self.pressNumber("1")
        def press2(event):
            self.pressNumber("2")
        def press3(event):
            self.pressNumber("3")
        def press4(event):
            self.pressNumber("4")
        def press5(event):
            self.pressNumber("5")
        def press6(event):
            self.pressNumber("6")
        def press7(event):
            self.pressNumber("7")
        def press8(event):
            self.pressNumber("8")
        def press9(event):
            self.pressNumber("9")
        def press0(event):
            self.pressNumber("0")
        def pressDot(event):
            self.pressNumber(".")
        def pressPlus(event):
            self.pressSum()
        def pressMinus(event):
            self.pressMin()
        def pressDivide(event):
            self.pressDiv()
        def pressMulti(event):
            self.pressMul()
        def pressClear(event):
            self.pressC()
        def pressEnter(event):
            self.pressRes()
        def pressBack(event):
            self.pressBack()
            
        self.bind("1",press1)
        self.bind("2",press2)
        self.bind("3",press3)
        self.bind("4",press4)
        self.bind("5",press5)
        self.bind("6",press6)
        self.bind("7",press7)
        self.bind("8",press8)
        self.bind("9",press9)
        self.bind("0",press0)
        self.bind("+",pressPlus)
        self.bind("-",pressMinus)
        self.bind("/",pressDivide)
        self.bind("*",pressMulti)
        self.bind("c",pressClear)
        self.bind(".",pressDot)
        self.bind("<BackSpace>",pressBack)
        self.bind("<Return>",pressEnter)
        
    def pressNumber(self,n):
        if self.textVar=="0" or self.textVar=="0.0":
            self.textVar=n
            self.label.configure(text=self.textVar)
        elif n==".":
            if "." not in self.textVar:
                self.textVar=self.textVar+n
                self.label.configure(text=self.textVar)
        else:
            self.textVar=self.textVar+n
            self.label.configure(text=self.textVar)
            
        self.changeButtonColorWhenPressed(n)
        self.label.configure(font=CTkFont("Impact",25)if len(self.textVar)>19 else CTkFont("Impact",35))
        
    def pressBack(self):
        if self.textVar != "0":
            self.textVar=self.textVar[:-1]
            self.label.configure(text=self.textVar)
        self.changeButtonColorWhenPressed("clear")
        
    def pressC(self):
        self.textVar="0"
        self.firstValue="0"
        self.label.configure(text=self.textVar)
        self.changeButtonColor("clear")
        self.changeButtonColorWhenPressed("clear")
        
    def pressSum(self):
        self.changeButtonColor("+")
        self.changeButtonColorWhenPressed("clear")
        if self.operator != "+":
            self.operator="+"
            self.firstValue=self.textVar
            self.textVar="0"
            self.label.configure(text=self.textVar)
        
    def pressMin(self):
        self.changeButtonColor("-")
        self.changeButtonColorWhenPressed("clear")
        if self.operator != "-":
            self.operator="-"
            self.firstValue=self.textVar
            self.textVar="0"
            self.label.configure(text=self.textVar)
    
    def pressDiv(self):
        self.changeButtonColor("/")
        self.changeButtonColorWhenPressed("clear")
        if self.operator != "/":
            self.operator="/"
            self.firstValue=self.textVar
            self.textVar="0"
            self.label.configure(text=self.textVar)
    
    def pressMul(self):
        self.changeButtonColor("*")
        self.changeButtonColorWhenPressed("clear")
        if self.operator != "*":
            self.operator="*"
            self.firstValue=self.textVar
            self.textVar="0"
            self.label.configure(text=self.textVar)
        
    def pressRes(self):
        if self.operator=="+":
            self.textVar=str(float(self.textVar)+float(self.firstValue))
        if self.operator=="-":
            self.textVar=str(float(self.firstValue)-float(self.textVar))
        if self.operator=="/":
            if self.textVar =="0" or self.firstValue=="0":
                print("Cannot divided by zero")
            else:
                self.textVar=str(float(self.firstValue)/float(self.textVar))
        if self.operator=="*":
            self.textVar=str(float(self.textVar)*float(self.firstValue))
            
        self.operator=""
        self.label.configure(font=CTkFont("Impact",25)if len(self.textVar)>19 else CTkFont("Impact",35))       
        self.label.configure(text=self.textVar)
        self.changeButtonColor("clear")
        self.changeButtonColorWhenPressed("clear")
        
    def changeButtonColor(self,button):
        self.buttonSum.configure(fg_color="red" if button=="+" else self.opButtonColors)
        self.buttonMin.configure(fg_color="red" if button=="-" else self.opButtonColors)
        self.buttonDiv.configure(fg_color="red" if button=="/" else self.opButtonColors)
        self.buttonMul.configure(fg_color="red" if button=="*" else self.opButtonColors)
    
    def changeButtonColorWhenPressed(self,number):
        color="transparent"
        self.button0.configure(fg_color=color if number =="0" else "blue")
        self.button1.configure(fg_color=color if number =="1" else "blue")
        self.button2.configure(fg_color=color if number =="2" else "blue")
        self.button3.configure(fg_color=color if number =="3" else "blue")
        self.button4.configure(fg_color=color if number =="4" else "blue")
        self.button5.configure(fg_color=color if number =="5" else "blue")
        self.button6.configure(fg_color=color if number =="6" else "blue")
        self.button7.configure(fg_color=color if number =="7" else "blue")
        self.button8.configure(fg_color=color if number =="8" else "blue")
        self.button9.configure(fg_color=color if number =="9" else "blue")
    
app=Main()
app.mainloop()