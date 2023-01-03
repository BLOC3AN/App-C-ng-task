from tkinter import *
from tkinter.ttk import *
import tkinter
#Tạo cửa ổ chính của UI
windown = Tk()
windown.title("Lười quá nên viết App này")
windown.iconbitmap("avatar.ico")


#Thêm label đầu
lbl = tkinter.Label(windown, text="Nhập số vào đây", fg="red", font=("Time New Roman", 20))
lbl.grid(column= 0 , row= 0 )

#Thêm label cuối
lbl2 = tkinter.Label(windown, text="Kết quả là:", fg="black", font=("Time New Roman", 20))
lbl2.grid(column= 0, row= 2 )


#Thêm textbox
txt = Entry(windown, width=20)
txt.grid(column=0, row=1)

n = 0
def handleButton():
    global n
    try:
        k = int(txt.get())
        if k == 0 :
            n = 0
        else:
            n = n + k
        lbl2.configure(text="Kết quả là:" + str(n))
        txt.delete(0, tkinter.END)

    except:
        lbl2.configure(text="Hãy nhập số ")
        txt.delete(0, tkinter.END)
        pass
    return

# Reset
def reset():
    global n
    txt.delete(0, tkinter.END)
    lbl2.configure(text="Kết quả là:")
    n = 0
    return

#thêm Button
btn = Button(windown, text="Submit", command=handleButton)

#Nút Reset
btn2 = Button(windown, text="Reset", command=reset)
btn2.grid(column=1, row=2)

# #Thêm combobox
# combo = Combobox(windown)
# combo['values'] = ("Bạn 1", "Bạn 2", "Bạn 3")
# combo.grid(column=0, row=2)

windown.mainloop()