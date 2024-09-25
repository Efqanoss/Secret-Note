import os
from CustomTkinterMessagebox import *
from efo_crypt import decrypt, encrypt
import customtkinter as ck
from PIL import Image

# pictures
file = os.path.dirname(os.path.abspath(__file__))
ic = os.path.join(file, 'photos', "icon.ico")
bg_1 = os.path.join(file, 'photos', "photo1.png")
bg_image = Image.open(bg_1)
bG = ck.CTkImage(bg_image, size=(100, 100))


def allo():
    try:
        pas = int(password.get())
    except:
        CTkMessagebox.messagebox(title="ERROR",text="Paswword just be numbers")
    wor = (tx_box.get("1.0", ck.END))
    c = encrypt(word=wor, key=pas)

    if cb_1.get() == 0:
        try:
            with open("secret.txt", 'a') as file:
                file.write("Title:" f"{title_1.get()}" "\n" f"{c}" "\n\n")
        except:
            with open("secret.txt", 'w') as file:
                file.write("Title:" f"{title_1.get()}" "\n" f"{c}" "\n\n")
    else:
        CTkMessagebox.messagebox(title="Decryp", text=f"{decrypt(word=wor, key=pas)}")


# widgets
def l_bg():
    label = ck.CTkLabel(window, image=bG, text="")
    label.place(x=210, y=0)


# window
ck.set_appearance_mode("dark")
window = ck.CTk()
window.configure(bg="black")
window.title("secret note")
window.iconbitmap(ic)
window.minsize(500, 500)
window.maxsize(500, 500)
l_bg()
# checbox
t = ck.IntVar()
cb_1 = ck.CTkCheckBox(window, text="", variable=t, onvalue=0, offvalue=1)
cb_1.place(x=190, y=80)
cb_2 = ck.CTkCheckBox(window, text="", variable=t, onvalue=1, offvalue=0)
cb_2.place(x=290, y=80)
# checbox text

lb_1 = ck.CTkLabel(window, text="Encrypt")
lb_1.place(x=140, y=80)
lb_2 = ck.CTkLabel(window, text="Decrypt")
lb_2.place(x=320, y=80)
# entry_title
lb_3 = ck.CTkLabel(window, text="Title")
lb_3.place(x=160, y=130)

title_1 = ck.CTkEntry(window, width=100, height=20)
title_1.place(x=200, y=130)

# title_password
lb_4 = ck.CTkLabel(window, text="password")
lb_4.place(x=65, y=360)

password = ck.CTkEntry(window, width=250)
password.place(x=125, y=360)

# textbox
tx_box = ck.CTkTextbox(window, width=250, height=150)
tx_box.place(x=125, y=190)
lb_5 = ck.CTkLabel(window, text="word")
lb_5.place(x=90, y=190)
# button
button = ck.CTkButton(window, text="Run", command=allo)
button.place(x=180, y=400)

window.mainloop()
