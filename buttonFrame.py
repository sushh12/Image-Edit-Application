import customtkinter as ctk

class ButtonFrame(ctk.CTkFrame):
    def __init__(self, master, main_app):
        super().__init__(master)
        self.main_app = main_app

        # BUTTONS
        ctk.CTkButton(self, text="Open", width=10, hover=True, hover_color="Red", command=self.main_app.open_img).grid(row=0, column=0)
        ctk.CTkButton(self, text="Edit", width=10, hover=True, hover_color="Red").grid(row=0, column=1)
        ctk.CTkButton(self, text="Save", width=10, hover=True, hover_color="Red").grid(row=0, column=2)