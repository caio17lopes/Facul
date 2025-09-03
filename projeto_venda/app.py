import customtkinter as ctk
from login import Login

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

if __name__ == "__main__":
    login = Login()
    login.mainloop()
