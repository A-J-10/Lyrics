from tkinter import *
from lyrics_extractor import SongLyrics

def get_lyrics():
    extract_lyrics = SongLyrics("AIzaSyACdwn8EO-bLdVZ2l4A9LCyjKofHaOOMDY","a4669763c468b41ad")	
    temp = extract_lyrics.get_lyrics(str(e.get()))
    res = temp['lyrics']
    result_text.config(state=NORMAL)
    result_text.delete("1.0", END)
    result_text.insert(END, res)
    result_text.config(state=DISABLED)

master = Tk()
master.title("Ankit's Application")
master.configure(bg='light grey')

result_frame = Frame(master)
result_frame.grid(row=3, column=0, columnspan=3)
Label(master, text="Enter Song name : ",bg="light grey").grid(row=0, sticky=W)
result_label = Label(result_frame, text="Result:", bg="light grey")
result_label.pack(side=LEFT)

scrollbar = Scrollbar(result_frame)
scrollbar.pack(side=RIGHT, fill=Y)

result_text = Text(result_frame, width=50, height=10, yscrollcommand=scrollbar.set)
result_text.pack(side=LEFT, fill=BOTH)
result_text.config(state=DISABLED)

scrollbar.config(command=result_text.yview)

e = Entry(master, width=50)
e.grid(row=0, column=1)

b = Button(master, text="Show", command=get_lyrics, bg="Cyan")
b.grid(row=0, column=2, columnspan=2, padx=5, pady=5)
def changeOnHover(button, colorOnHover, colorOnLeave):
 
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
 
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))
changeOnHover(b, "Orange", "cyan")
mainloop()

