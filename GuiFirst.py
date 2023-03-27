import tkinter

window = tkinter.Tk()

window.title("Gui program by imjaewan")
window.geometry("640x400+100+100")
window.resizable(False, False)

def btnclick() :
    label.config(font=("Arial", 40))
    label.config(text="안산공업고등학교 컴퓨터과")
    label.config(fg="indigo")

label = tkinter.Label(window, text="안산공업고등학교")
label.pack()

button = tkinter.Button(window, text="확인", command=btnclick)
button.pack()
window.mainloop()



