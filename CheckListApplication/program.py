from tkinter import *
# from PIL import ImageTk , Image
# from tkinter.filedialog import *
import tkinter.messagebox
root = Tk()

#setting หน้าจอโปรแกรม
root.title("Calculate Program")
root.iconbitmap(r'D:\Tkinker Kongsaksayam\CheckList Asset\check.ico')
root.geometry("300x300+600+300") #ปรับขนาด
root.resizable(1,0) #เปลี่ยนขนาดได้ 1 = เปลี่ยนได้ 0 = เปลี่ยนไม่ได้
root.config(bg="#EEF5FF")
font =("Arial",15)

#setting frame
input_frame = Frame(root,bg="#FAE5E2")
input_frame.pack(fill=X , expand=True)

output_frame = Frame(root,bg="#f9d6d4")
output_frame.pack(fill=X , expand=True)

button_frame = Frame(root,bg="#A7767C")
button_frame.pack(fill=X , expand=True)

#setting attribute @ input_frame
input = StringVar() #ประกาศตัวแปร
inputdata = Entry(input_frame,textvariable=input,bg="white")
inputdata.config(font=font)
inputdata.grid(row=0,column=0,padx=5,pady=5,ipadx=5,ipady=5)


#setting attribute @output_frame
showdata = Listbox(output_frame,width=25,height=8,font=font,bg="white",fg="black")
showdata.grid(row=0,column=0,padx=5,pady=5)

#setting def @input_frame
def addData():
    ad = input.get()
    if ad == "":
        tkinter.messagebox.showerror("Error","You did not fill yet")
    else:
        ad = ad.encode('utf-8')
        print(ad)
        inputdata.delete(0,END)
        showdata.insert(END,ad)

#setting def@button_frame
def removeData():
    showdata.delete(ANCHOR) #ANCHOR คือสามารถเลือกตัวให้โปรแกรมลบได้
    
def clearData():
    showdata.delete(0,END)
    
    

# Button @input_frame
addBut = Button(input_frame,text="Add",bg="#E6B5B8",command=addData)
addBut.grid(row=0,column=1,padx=5,pady=10,ipadx=5,ipady=5)

#Button @button_frame
btnRemove = Button(button_frame,text="Delete",bg="#E6B5B8",command=removeData)
btnRemove.grid(row=0,column=0,padx=5,pady=2,ipadx=25,ipady=3)

btnClear = Button(button_frame,text="Clear",bg="#E6B5B8",command=clearData)
btnClear.grid(row=0,column=1,padx=5,pady=2,ipadx=25,ipady=3)

d = Button(button_frame,text="Close",bg="#E6B5B8",command=root.destroy)
d.grid(row=0,column=2,padx=2,pady=5,ipadx=25,ipady=3)

root.mainloop() 

