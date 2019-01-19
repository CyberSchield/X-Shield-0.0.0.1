from tkinter import *
import time
# Creating the window

#root = Tk()

# modify the root window
def gui_disp(stat="safe"):
    root = Tk()
    root.title("Cybershield-Project-X v 1.0")
    root.geometry("800x500")

    app = Frame(root, bg="green")
    app.config(bg="green")
    app.pack(fill='both', expand='yes')
    app.pack()

    ourmessage = "System Is Safe"
    messageVar = Message(app, text=ourmessage,bd = 8 , relief = "solid" ,
                         font="Times 22 bold",fg = "white")
    messageVar.place(x=300, y=300, anchor="center")
    messageVar.pack()
    messageVar.config(bg='lightgreen')
    for i in range(5):
        if(stat == "safe"):
            app['bg'] = "green"
            ourmessage = "System Is Safe"
            messageVar['text'] = ourmessage
            messageVar['bg'] = 'lightgreen'
        else:
            app['bg'] = "red"
            ourmessage1 = "System Is Unsafe"
            messageVar['text'] = ourmessage1
            messageVar['bg'] = 'red'
    # Launching the window
        root.update_idletasks()
        root.update()
        time.sleep(2)
        stat = "fall"


safe_stat = "safe"
gui_disp(safe_stat)