from tkinter import *
from tkinter import ttk
import tkinter.font
from PIL import Image, ImageTk

root=Tk()
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.title("TASK #3")

bg = Image.open("wallhaven1.png")
bg = bg.resize((1366, 720), Image.ANTIALIAS)
test = ImageTk.PhotoImage(bg)

l1=tkinter.Label(image=test)
l1.image = test
l1.place(x=0, y=0)

def caesar():
    s=txt.get()
    k=3
    l=[]
    l[:0]=s
    n=len(l)
    text=['']*n

    for i in range(n):
        m=i
        if m+k>=n:
            m=m-n
        elif m+k<0:
            m=m+n
        text[m+k]=l[i]
    anstag=Label(root, font= font1, relief='sunken', bd=3, text='Ans: ')
    anstag.place(x=1050,y=150)
    ans=Label(root, font= font1,width=20, relief='sunken', bd=3, text=''.join(text))
    ans.place(x=1150,y=150)
    key=Label(root, font= font1, width=30, relief='sunken', bd=3, text='Key: 3')
    key.place(x=1050,y=250)
    #print (''.join(text))
    #print(w)

def playfair():
    source=txt.get()
    l=len(source)
    keyArr=["infos","ecabd","ghklm","pqrtu","vwxyz"]
    r1=r2=c1=c2=s=0
    ans=['']*l
    for i in range(0,l-1,2):
        for j in keyArr:
            if source[i] in j:
                r1=keyArr.index(j)
                c1=j.index(source[i])
            if source[i+1] in j:
                r2=keyArr.index(j)
                c2=j.index(source[i+1])
        
        if r1==r2:
            ans[i]=keyArr[r1][(c1+1)%5]
            ans[i+1]=keyArr[r2][(c2+1)%5]
        elif c1==c2:
            ans[i]=keyArr[(r1+1)%5][c1]
            ans[i+1]=keyArr[(r2+1)%5][c2]
        else:
            ans[i]=keyArr[r1][c2]
            ans[i+1]=keyArr[r2][c1]
    
    anstag=Label(root, font= font1, relief='sunken', bd=3, text='Ans: ')
    anstag.place(x=1050,y=150)
    answer=Label(root, font= font1,width=20, relief='sunken', bd=3, text=''.join(ans))
    answer.place(x=1150,y=150)
    key=Label(root, font= font1, width=30, relief='sunken', bd=3, text='Key: Infosec')
    key.place(x=1050,y=250)

'''def decrypt():
    s=txt.get()
    k=3
    l=[]
    l[:0]=s
    n=len(l)
    text=['']*n

    for i in range(n):
        m=i
        #if m-k<=0:
         #   m=m-n
        #elif m-k<0:
         #   m=m+n
        text[m-k]=l[i]
    anstag=Label(root, font= font1, relief='sunken', bd=3, text='Ans: ')
    anstag.place(x=1050,y=150)
    ans=Label(root, font= font1, relief='sunken', bd=3, text=''.join(text))
    ans.place(x=1150,y=150)
    #print (''.join(text))'''



s=tkinter.IntVar()

#Widgets

txt=tkinter.StringVar()

font1 = tkinter.font.Font( family = "Comic Sans MS", size = 10, weight = "bold")
l2=Label(root, font= font1, relief='sunken', bd=3, text='Add Text to Encrypt/Decrypt')
l2.place(x=50,y=150)

w0=Entry(root, textvariable=txt, bd=5, width=30)
w0.place(x=270,y=150)


w1=Button(root, text='Caesar Encryption', font=font1, width='20', bd=5, activebackground='#edddd5', activeforeground='#edddd5' , command=caesar)
w1.place(x=125, y=300)

w2=Button(root, text='Playfair Encryption', font=font1, width='20', bd=5, activebackground='#edddd5', activeforeground='#edddd5' , command=playfair)
w2.place(x=125, y=350)

'''w4=Radiobutton(root, text='Encrypt', variable=v, value=1, font=font1, width='20', bd=5, activebackground='#edddd5', activeforeground='#edddd5')
w4.place(x=125, y=200)

w5=Radiobutton(root, text='Decrypt',variable=v, value=2, font=font1, width='20', bd=5, activebackground='#edddd5', activeforeground='#edddd5')
w5.place(x=125, y=250)'''

#print(w)
root.mainloop()
