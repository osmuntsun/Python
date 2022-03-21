import tkinter as tk 

win=tk.Tk() #建立主視窗
win.title("寶寶群") #視窗開頭

btn = tk.Button(text="名單") #按鈕 按鈕名稱
btn.pack()

win.geometry("400x200") #寬x高
win.minsize()


win.mainloop() #常駐主視窗

