from tkinter import *
import tkinter as tk
import tkinter.font as font

root = tk.Tk()
root.title('Reset Password')
root.geometry('657x510+350+100')

# Show background
image_background = tk.PhotoImage(file='C:\images\Reset Password\imagebg.png', height=510, width=657)
Label(root,image=image_background, borderwidth=0).place(x=0,y=0)

#button
image_button = tk.PhotoImage(file='C:\images\Reset Password\change_button.png', height=30, width=105)
change_pass_button = Button(image=image_button,borderwidth=0)
change_pass_button.place(x=185, y=360)

#textbox
text_password = Text(root)
text_password.configure(
            borderwidth=0,
            font="{inter} 11 {}",
            foreground="#727272",
            height=10,
            width=50)
text_password.place(
    anchor='nw',
    height=20,
    width=224,
    x=128,
    y=223
)

text_confirm_new_password = Text(root)
text_confirm_new_password.configure(
    borderwidth=0,
    font='{inter} 11 {}',
    foreground='#727272',
    height=10,
    width=50
)

text_confirm_new_password.place(
    anchor='nw',
    height=20,
    width=224,
    x=128,
    y=295
)



root.mainloop()