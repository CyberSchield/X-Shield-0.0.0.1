from tkinter import *
import time
global stat
# Creating the window
#root = Tk()

# modify the root window
stat = 'safe'
shut_var = 1
root = Tk()
root.title("Cybershield-Project-X v 1.0")
root.geometry("800x500")

def cl():
    global stat
    stat = 'close'

app = Frame(root, bg="green")
app.config(bg="AntiqueWhite3")
app.pack(fill='both', expand='yes')

ourmessage = "System Is Safe"
messageVar = Message(app, text=ourmessage,bd = 8 , relief = "solid" ,
                         font="Times 22 bold",fg = "white")
messageVar.place( x = 400 , y = 150 , anchor="center",width = 400,height=250)
messageVar.config(bg='lightgreen')

button = Button(app, text="Shutdown the system",bd=5 , relief = "solid",
                           font="Times 18 bold",fg = "red", )
button.place( x = 400 , y = 450 , anchor="center")
button.config( command= lambda : cl() )
stat = "safe"
while(True):
    print(stat)
    if(stat == "safe"):
        ourmessage = "System Is Safe"
        messageVar['text'] = ourmessage
        messageVar['bg'] = 'lightgreen'

    elif(stat == "close"):
        ourmessage3 = "Shutting Down in 15 Seconds"
        messageVar['text'] = ourmessage3
        messageVar['bg'] = 'gold'
        if(shut_var == 2):
            time.sleep(15)
            break
        shut_var += 1

    else:
        ourmessage1 = "System Is Unsafe"
        messageVar['text'] = ourmessage1
        messageVar['bg'] = 'red'
# Launching the window
    root.update_idletasks()
    root.update()
