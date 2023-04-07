from tkinter import *
import tkinter as bro
from tkinter import ttk
from tkinter import messagebox




#making the main window


root=bro.Tk()
root.title("THE BRO'S HOUSE")
root.config(background="light green")
root.geometry("800x600")
root.resizable (0,0)


heading=Label(root,text="THE BRO'S WEAR",font="algerian 45",bg="orange").pack(side=TOP)
f=Label(root,text="\n\nwe deals in all type of mens wear".upper(),font="times 15",background="light green").pack(side=TOP)
s=Label(root,text="\n1.shirts".upper(),font="Snap  22",background="light green").pack(side=TOP)
t=Label(root,text="2.pants".upper(),font="Snap  22",background="light green").pack(side=TOP)
y=Label(root,text="3.shorts".upper(),font="Snap  22",background="light green").pack(side=TOP)
u=Label(root,text="4.trousers".upper(),font="Snap  22",background="light green").pack(side=TOP)
Z=Label(root,text="\n\n\npress the button of your choice".upper(),background="light green",font="Bahnschrift 18").pack(side=TOP)


def exiting():
    messagebox.showinfo(title="THANKS FOR SHOPPING",message="THANK YOU FOR VISITING THE BROS'S WEAR! \n          credits:M HUZAIFA ARSHAD".upper())
    root.destroy()

def shirts():
    top=Toplevel()
    top.geometry("500x400")
    top.resizable(0, 0)
    l0=Label(top,text="THE BRO'S WEAR",font="algerian  18").pack(side=TOP)
    l1=Label(top,text=" which shirt you want!".upper(),font="times 18").place(x=10,y=60)
    shir=ttk.Combobox(top)
    shir['values']=('full sleeves'.upper(),'half sleeves'.upper(),'t-shirt'.upper(),'sleeveless'.upper())
    shir.current()
    shir.place(x=300,y=103)
    l2 = Label(top, text="  how much do you want!".upper(), font="times 18").place(x=10, y=150)
    quantity=Entry(top,bd=5)
    quantity.place(x=310,y=190)
    l3 = Label(top, text=" WHICH SIZE YOU WANT SIR!".upper(), font="times 18").place(x=10, y=245)
    shir1=ttk.Combobox(top)
    shir1['values']=('SMALL'.upper(),'MEDIUM'.upper(),'LARGE'.upper(),'X-LARGE'.upper())
    shir1.current()
    shir1.place(x=300,y=280)

    def BILL1():
        root1=bro.Tk()
        root1.configure(background="orange")
        root1.geometry("400x300")
        root1.resizable(0, 0)
        
        
        l0=Label(root1,text="THE BRO'S WEAR",font="algerian  18").pack(side=TOP)
        la=Label(root1,text="shirt type:   ".upper(),font="algerian 14").place(x=30,y=65)
        l1=Label(root1,text=shir.get(),font="times 14").place(x=150,y=65)
        l2=Label(root1,text="QUANTITY:    ".upper(),font="algerian 14").place(x=30,y=115)
        l3=Label(root1,text=quantity.get(),font="times 14").place(x=150,y=115)
        l4=Label(root1,text="SIZE :    ".upper(),font="algerian 14").place(x=30,y=165)
        l5=Label(root1,text=shir1.get(),font="times 14").place(x=150,y=165)
        l6=Label(root1,text="YOUR TOTAL IS:   ",font="algerian 14").place(x=30,y=205)
        
        if shir.get() == "FULL SLEEVES" and shir1.get() == "SMALL":
            q=(int(quantity.get())*250)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "FULL SLEEVES" and shir1.get() == "MEDIUM":
            q=(int(quantity.get())*350)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "FULL SLEEVES" and shir1.get() == "LARGE":
            q=(int(quantity.get())*550)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "FULL SLEEVES" and shir1.get() == "X-LARGE":
            q=(int(quantity.get())*700)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
          
        if shir.get() == "HALF SLEEVES" and shir1.get() == "SMALL":
            q=(int(quantity.get())*250)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "HALF SLEEVES" and shir1.get() == "MEDIUM":
            q=(int(quantity.get())*350)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "HALF SLEEVES" and shir1.get() == "LARGE":
            q=(int(quantity.get())*550)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "HALF SLEEVES" and shir1.get() == "X-LARGE":
            q=(int(quantity.get())*700)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
          
        if shir.get() == "T-SHIRT" and shir1.get() == "SMALL":
            q=(int(quantity.get())*250)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "T-SHIRT" and shir1.get() == "MEDIUM":
            q=(int(quantity.get())*350)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "T-SHIRT" and shir1.get() == "LARGE":
            q=(int(quantity.get())*550)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "T-SHIRT" and shir1.get() == "X-LARGE":
            q=(int(quantity.get())*700)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
            
        if shir.get() == "SLEEVELESS" and shir1.get() == "SMALL":
            q=(int(quantity.get())*250)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "SLEEVELESS" and shir1.get() == "MEDIUM":
            q=(int(quantity.get())*350)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "SLEEVELESS" and shir1.get() == "LARGE":
            q=(int(quantity.get())*550)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "SLEEVELESS" and shir1.get() == "X-LARGE":
            q=(int(quantity.get())*700)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
            
        def paid():
            root1.destroy()
            
            
        b1=Button(root1,text="paid",command=paid,padx=30,pady=10,bd=6).pack(side=BOTTOM)
       
    
    b=Button(top,text="BILL",command=BILL1,font="algerian 10",padx=30,pady=10,bd=6).place(x=280,y=350)
    b2=Button(top,text="EXIT",command=top.destroy,font="algerian 10",padx=30,pady=7,bd=6).place(x=70,y=355)    

def pants():
    top=Toplevel()
    top.geometry("500x400")
    top.resizable(0, 0)
    l0=Label(top,text="THE BRO'S WEAR",font="algerian  18").pack(side=TOP)
    l1=Label(top,text=" which type of pant you want!".upper(),font="times 18").place(x=10,y=60)
    shir=ttk.Combobox(top)
    shir['values']=('jeans'.upper(),'leather'.upper(),'casual wear'.upper(),'dress pant'.upper())
    shir.current()
    shir.place(x=300,y=103)
    l2 = Label(top, text="  how much do you want!".upper(), font="times 18").place(x=10, y=150)
    quantity=Entry(top,bd=5)
    quantity.place(x=310,y=190)
    l3 = Label(top, text="what is your size !".upper(), font="times 18").place(x=15, y=245)
    shir1=ttk.Combobox(top)
    shir1['values']=('SMALL'.upper(),'MEDIUM'.upper(),'LARGE'.upper(),'X-LARGE'.upper())
    shir1.current()
    shir1.place(x=300,y=280)

    def BILL2():
        root1=bro.Tk()
        root1.configure(background="orange")
        root1.geometry("400x300")
        root1.resizable(0, 0)
        
        l0=Label(root1,text="THE BRO'S WEAR",font="algerian  18").pack(side=TOP)
        la=Label(root1,text="pant type:   ".upper(),font="algerian 14").place(x=30,y=65)
        l1=Label(root1,text=shir.get(),font="times 14").place(x=150,y=65)
        l2=Label(root1,text="QUANTITY:    ".upper(),font="algerian 14").place(x=30,y=115)
        l3=Label(root1,text=quantity.get(),font="times 14").place(x=150,y=115)
        l4=Label(root1,text="SIZE :    ".upper(),font="algerian 14").place(x=30,y=165)
        l5=Label(root1,text=shir1.get(),font="times 14").place(x=150,y=165)
        l6=Label(root1,text="YOUR TOTAL IS:   ",font="algerian 14").place(x=30,y=205)
        
        if shir.get() == "JEANS" and shir1.get() == "SMALL":
            q=(int(quantity.get())*250)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "JEANS" and shir1.get() == "MEDIUM":
            q=(int(quantity.get())*350)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "JEANS" and shir1.get() == "LARGE":
            q=(int(quantity.get())*550)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "JEANS" and shir1.get() == "X-LARGE":
            q=(int(quantity.get())*700)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
          
        if shir.get() == "LEATHER" and shir1.get() == "SMALL":
            q=(int(quantity.get())*250)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "LEATHER" and shir1.get() == "MEDIUM":
            q=(int(quantity.get())*350)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "LEATHER" and shir1.get() == "LARGE":
            q=(int(quantity.get())*550)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "LEATHER" and shir1.get() == "X-LARGE":
            q=(int(quantity.get())*700)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
          
        if shir.get() == "CASUAL WEAR" and shir1.get() == "SMALL":
            q=(int(quantity.get())*250)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "CASUAL WEAR" and shir1.get() == "MEDIUM":
            q=(int(quantity.get())*350)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "CASUAL WEAR" and shir1.get() == "LARGE":
            q=(int(quantity.get())*550)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "CASUAL WEAR" and shir1.get() == "X-LARGE":
            q=(int(quantity.get())*700)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
            
        if shir.get() == "DRESS PANT" and shir1.get() == "SMALL":
            q=(int(quantity.get())*250)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "DRESS PANT" and shir1.get() == "MEDIUM":
            q=(int(quantity.get())*350)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "DRESS PANT" and shir1.get() == "LARGE":
            q=(int(quantity.get())*550)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "DRESS PANT" and shir1.get() == "X-LARGE":
            q=(int(quantity.get())*700)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
            
        def paid():
            root1.destroy()
            
            
        b1=Button(root1,text="paid",command=paid,padx=30,pady=10,bd=6).pack(side=BOTTOM)
       
    
    b=Button(top,text="BILL",command=BILL2,font="algerian 10",padx=30,pady=10,bd=6).place(x=280,y=350)
    b2=Button(top,text="EXIT",command=top.destroy,font="algerian 10",padx=30,pady=7,bd=6).place(x=70,y=355)

def tr():
    top=Toplevel()
    top.geometry("500x400")
    top.resizable(0, 0)
    l0=Label(top,text="THE BRO'S WEAR",font="algerian  18").pack(side=TOP)
    l1=Label(top,text=" which item you  want!".upper(),font="times 18").place(x=10,y=60)
    shir=ttk.Combobox(top)
    shir['values']=('3d shorts'.upper(),'bermuda shorts'.upper(),'tight trouser'.upper(),'stylish trouser'.upper())
    shir.current()
    shir.place(x=300,y=103)
    l2 = Label(top, text="  how many do you want!".upper(), font="times 18").place(x=10, y=150)
    quantity=Entry(top,bd=5)
    quantity.place(x=310,y=190)
    l3 = Label(top, text="what is your size !".upper(), font="times 18").place(x=15, y=245)
    shir1=ttk.Combobox(top)
    shir1['values']=('SMALL'.upper(),'MEDIUM'.upper(),'LARGE'.upper(),'X-LARGE'.upper())
    shir1.current()
    shir1.place(x=300,y=280)

    def BILL2():
        root1=bro.Tk()
        root1.configure(background="yellow")
        root1.geometry("400x300")
        root1.resizable(0, 0)
        
        l0=Label(root1,text="THE BRO'S WEAR",font="algerian  18").pack(side=TOP)
        la=Label(root1,text="item type:   ".upper(),font="algerian 14").place(x=30,y=65)
        l1=Label(root1,text=shir.get(),font="times 14").place(x=150,y=65)
        l2=Label(root1,text="QUANTITY:    ".upper(),font="algerian 14").place(x=30,y=115)
        l3=Label(root1,text=quantity.get(),font="times 14").place(x=150,y=115)
        l4=Label(root1,text="SIZE :    ".upper(),font="algerian 14").place(x=30,y=165)
        l5=Label(root1,text=shir1.get(),font="times 14").place(x=150,y=165)
        l6=Label(root1,text="YOUR TOTAL IS:   ",font="algerian 14").place(x=30,y=205)
        
        if shir.get() == "3d shorts".upper() and shir1.get() == "SMALL":
            q=(int(quantity.get())*250)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "3d shorts".upper() and shir1.get() == "MEDIUM":
            q=(int(quantity.get())*350)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "3d shorts".upper() and shir1.get() == "LARGE":
            q=(int(quantity.get())*550)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "3d shorts".upper() and shir1.get() == "X-LARGE":
            q=(int(quantity.get())*700)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
          
        if shir.get() == "bermuda shorts".upper() and shir1.get() == "SMALL":
            q=(int(quantity.get())*250)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "bermuda shorts".upper() and shir1.get() == "MEDIUM":
            q=(int(quantity.get())*350)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "bermuda shorts".upper() and shir1.get() == "LARGE":
            q=(int(quantity.get())*550)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "bermuda shorts".upper() and shir1.get() == "X-LARGE":
            q=(int(quantity.get())*700)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
          
        if shir.get() == "tight trouser".upper() and shir1.get() == "SMALL":
            q=(int(quantity.get())*250)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "tight trouser".upper() and shir1.get() == "MEDIUM":
            q=(int(quantity.get())*350)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "tight trouser".upper() and shir1.get() == "LARGE":
            q=(int(quantity.get())*550)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "tight trouser".upper() and shir1.get() == "X-LARGE":
            q=(int(quantity.get())*700)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
            
        if shir.get() == "stylish trouser".upper() and shir1.get() == "SMALL":
            q=(int(quantity.get())*250)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "stylish trouser".upper() and shir1.get() == "MEDIUM":
            q=(int(quantity.get())*350)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "stylish trouser".upper() and shir1.get() == "LARGE":
            q=(int(quantity.get())*550)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "stylish trouser".upper() and shir1.get() == "X-LARGE":
            q=(int(quantity.get())*700)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
            
        def paid():
            root1.destroy()
            
            
        b1=Button(root1,text="paid",command=paid,padx=30,pady=10,bd=6).pack(side=BOTTOM)
       
    
    b=Button(top,text="BILL",command=BILL2,font="algerian 10",padx=30,pady=10,bd=6).place(x=280,y=350)
    b2=Button(top,text="EXIT",command=top.destroy,font="algerian 10",padx=30,pady=7,bd=6).place(x=70,y=355)
def watches():
    top=Toplevel()
    top.geometry("500x400")
    top.resizable(0, 0)
    
    l0=Label(top,text="THE BRO'S WEAR",font="algerian  18").pack(side=TOP)
    l1=Label(top,text=" which type of watch you want!".upper(),font="times 18").place(x=10,y=60)
    shir=ttk.Combobox(top)
    shir['values']=('digital watch'.upper(),'stylish leather watch'.upper(),'waterproof'.upper(),'casual-watch'.upper())
    shir.current()
    shir.place(x=300,y=103)
    l2 = Label(top, text="  how much do you want!".upper(), font="times 18").place(x=10, y=150)
    quantity=Entry(top,bd=5)
    quantity.place(x=310,y=190)
    l3 = Label(top, text="what is your size !".upper(), font="times 18").place(x=15, y=245)
    shir1=ttk.Combobox(top)
    shir1['values']=("kidz".upper(),"boys".upper(),"men".upper())
    shir1.current()
    shir1.place(x=300,y=280)

    def BILL2():
        root1=bro.Tk()
        root1.configure(background="light yellow")
        root1.geometry("400x300")
        root1.resizable(0, 0)
        
        l0=Label(root1,text="THE BRO'S WEAR",font="algerian  18").pack(side=TOP)
        la=Label(root1,text="watch type:   ".upper(),font="algerian 14").place(x=30,y=65)
        l1=Label(root1,text=shir.get(),font="times 14").place(x=150,y=65)
        l2=Label(root1,text="QUANTITY:    ".upper(),font="algerian 14").place(x=30,y=115)
        l3=Label(root1,text=quantity.get(),font="times 14").place(x=150,y=115)
        l4=Label(root1,text="SIZE :    ".upper(),font="algerian 14").place(x=30,y=165)
        l5=Label(root1,text=shir1.get(),font="times 14").place(x=150,y=165)
        l6=Label(root1,text="YOUR TOTAL IS:   ",font="algerian 14").place(x=30,y=205)
        
        if shir.get() == "digital watch".upper() and shir1.get() == "kidz".upper():
            q=(int(quantity.get())*250)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "digital watch".upper() and shir1.get() == "boys".upper():
            q=(int(quantity.get())*350)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "digital watch".upper() and shir1.get() == "men".upper():
            q=(int(quantity.get())*550)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)

          
        if shir.get() == "stylish leather watch".upper() and shir1.get() == "kidz".upper():
            q=(int(quantity.get())*250)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "stylish leather watch".upper() and shir1.get() == "boys".upper():
            q=(int(quantity.get())*350)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "stylish leather watch".upper() and shir1.get() == "men".upper():
            q=(int(quantity.get())*550)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)

        if shir.get() == "waterproof".upper() and shir1.get() == "kidz".upper():
            q=(int(quantity.get())*250)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "waterproof".upper() and shir1.get() == "boys".upper():
            q=(int(quantity.get())*350)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "waterproof".upper() and shir1.get() == "men".upper():
            q=(int(quantity.get())*550)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
            
        if shir.get() == "casual-watch".upper() and shir1.get() == "kidz".upper():
            q=(int(quantity.get())*250)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "casual-watch".upper() and shir1.get() == "boys".upper():
            q=(int(quantity.get())*350)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)
        elif shir.get() == "casual-watch".upper() and shir1.get() == "men".upper():
            q=(int(quantity.get())*550)
            l7=Label(root1,text=q,font="times 14").place(x=180,y=205)


            
        def paid():
            root1.destroy()
            
            
        b1=Button(root1,text="paid",command=paid,padx=30,pady=10,bd=6).pack(side=BOTTOM)
       
    
    b=Button(top,text="BILL",command=BILL2,font="algerian 10",padx=30,pady=10,bd=6).place(x=280,y=350)
    b2=Button(top,text="EXIT",command=top.destroy,font="algerian 10",padx=30,pady=7,bd=6).place(x=70,y=355)

    
    



b1=Button(root,text="SHIRTS",command=shirts,padx=20,pady=30,bd=5,font="times 12").place(x=16,y=480)
b2=Button(root,text="PANTS",command=pants,padx=20,pady=30,bd=5,font="times 12").place(x=160,y=480)
b3=Button(root,text="SHORTS \n& \nTROUSERS",command=tr,padx=20,pady=25,bd=6,font="times 12").place(x=300,y=470)
b4=Button(root,text="WATCHES",command=watches,padx=15,pady=30,bd=7,font="times 12").place(x=470,y=480)
b5=Button(root,text="FINISH SHOPPING",command=exiting,padx=5,pady=30,bd=6,font="times 12").place(x=630,y=480)


root.mainloop()

