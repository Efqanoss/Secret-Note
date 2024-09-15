import customtkinter as ck
import os
from PIL import Image
import efo_crypt

# pictures
file = os.path.dirname(os.path.abspath(__file__))
ic = os.path.join(file, 'photos', "icon.ico")
bg_1 = os.path.join(file, 'photos', "photo1.png")
bg_image = Image.open(bg_1)
bG = ck.CTkImage(bg_image, size=(100, 100))


# label bg
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
window.mainloop()
