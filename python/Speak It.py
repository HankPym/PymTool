import tkinter as tk
from tkinter import ttk
from sayit import sayit

# create the main/root window
root = tk.Tk()
root.title('Speak It!')
root.iconbitmap('C:/Users/lesfi/OneDrive/Code/python/images/f.ico')   # the icon used by the program

# set variables
window_width = 300
window_height = 100
messageText = tk.StringVar()

# get the screen dimensions and find the center points
screen_width = root.winfo_screenwidth()
center_x = int(screen_width/2 - window_width / 2)
screen_height = root.winfo_screenheight()
center_y = int(screen_height/2 - window_height / 2)

# set the size of the window based on the screen dimenstions
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# set the opaqueness of the window
root.attributes('-alpha', 0.85)

# function to get and process the entered text
def speakMessage(event):       
    msg = messageText.get()
    if (msg == 'quit' or msg == '' or msg == 'exit'):    # exit the program
        root.quit()
    else:
        sayit(msg)
        textEntry.delete(0,'end') # clear the entry field after speaking the text

# bind the Enter key so that it executes the speakMessage function
root.bind('<Return>',speakMessage) 

# create the label for the entry field
textLabel = ttk.Label(root, text="Enter your message:")
textLabel.pack(fill='x', expand=True)

# create the entry field
textEntry = ttk.Entry(root, textvariable=messageText)
textEntry.pack(fill='x', expand=True)
textEntry.focus()

### Old button method for playing text
# exitButton = ttk.Button(root, text='Speak it!', command=login_clicked)
# exitButton.pack(ipadx=5, ipady=5, expand=True )

root.mainloop()
