import tkinter
import tkinter.messagebox

window = tkinter.Tk()


window.title("BMI 계산기")
window.geometry("640x400+100+100")
window.resizable(False, False)

he = tkinter.StringVar()
we = tkinter.StringVar()

def btn_click() :
    h_value = float(he.get())
    w_value = float(we.get())
    h_value = h_value * 0.01
    result = w_value / (h_value * h_value)
    tkinter.messagebox.showinfo("결과", result)

label=tkinter.Label(window, text="체칠량지수 계산기", relief="solid", fg="red")
label.config(font=("Arial", 25))
label.pack()

#이게 텍스트 label
heightlabel = tkinter.Label(window, text="신장")
heightlabel.config(font=("Arial", 24))
heightlabel.place(x=30, y=70)

#이게 입력창 entry
heightentry = tkinter.Entry(window, textvariable=he)
heightentry.place(x=120, y=81)

wlabel = tkinter.Label(window, text="체중")
wlabel.config(font=("Arial", 24))
wlabel.place(x=30, y=160)

wentry = tkinter.Entry(window, textvariable=we)
wentry.place(x=120, y=171)


btn = tkinter.Button(window, text="확인", width=10, height=5, command = btn_click)
btn.place(x=30, y=250)



window.mainloop()

