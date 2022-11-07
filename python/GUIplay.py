import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from gtts import gTTS
from playsound import playsound

root = tk.Tk()
root.title('Fystems')
root.iconbitmap('./images/f.ico')

window_width = 300
window_height = 200
message = tk.StringVar()


# get the screen dimensions and find the center points
screen_width = root.winfo_screenwidth()
center_x = int(screen_width/2 - window_width / 2)
screen_height = root.winfo_screenheight()
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# set opaqueness
root.attributes('-alpha', 0.85)

def Text_to_speech(msg):
    speech = gTTS(text = msg)
    speech.save('GUIplay.mp3')
    playsound('GUIplay.mp3')

def login_clicked():
    # callback when the login button clicked
    msg = message.get()
    if (msg == 'quit' or msg == ''):
        root.quit()
    else:
        # yourMsg = f'Your entry: {msg}'
        # showinfo(
        #    title='Information',
        #    message=yourMsg)
        
        Text_to_speech(msg)
        email_entry.delete(0,'end')


email_label = ttk.Label(root, text="Message:")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(root, textvariable=message)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

exit_button = ttk.Button(root, text='Apply', command=login_clicked)
exit_button.pack(ipadx=5, ipady=5, expand=True )

root.mainloop()
