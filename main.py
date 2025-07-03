import customtkinter as ctk
from buttonFrame import ButtonFrame
from editPanel import EditPanel
# from CTkMessagebox import CTkMessagebox
# from tkinter import filedialog
# from PIL import Image

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")

        # Initialize variables
        self.img = None
        self.tk_img = None

        # frame for buttons
        btn_frame = ButtonFrame(self, self)
        btn_frame.pack(side='top', fill='x')

        # Main content frame
        self.main_frame = ctk.CTkFrame(self, fg_color='white')
        self.main_frame.pack(fill='both', expand=True)

        # Canvas to display image
        self.canvas = ctk.CTkLabel(self.main_frame, text=" ", fg_color="black")
        self.canvas.pack(padx=10, pady=10, expand=True)

        # Edit panel (initially hidden)
        self.edit_panel = EditPanel(self.main_frame, self)
        self.edit_panel.pack(side='right', fill='y', padx=10, pady=10)
        self.edit_panel.pack_forget()  # hide initially

if __name__ == "__main__":
    app = App()
    app.mainloop()
