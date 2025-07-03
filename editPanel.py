import customtkinter as ctk
# from PIL import ImageEnhance

class EditPanel(ctk.CTkFrame):
    def __init__(self, master, main_app):
        super().__init__(master)
        self.main_app = main_app

        # Brightness slider
        ctk.CTkLabel(self, text="Brightness").pack()
        self.brightness_slider = ctk.CTkSlider(self, from_=50, to=150)
        self.brightness_slider.set(1.0)  # default brightness
        self.brightness_slider.pack(pady=5)

        self.edit_panel_visible = False
