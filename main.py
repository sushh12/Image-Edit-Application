import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image, ImageEnhance, ImageFilter
from tkinter import filedialog

from buttonFrame import ButtonFrame
from editPanel import EditPanel

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        
        self.img = None
        
        # frame for buttons
        btn_frame = ButtonFrame(self, self)
        btn_frame.pack(side='top', fill='x')

        # Main content frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill='both', expand=True)

        # Canvas to display image
        self.canvas = ctk.CTkLabel(self.main_frame, text=" ")
        self.canvas.pack(padx=10, pady=10, expand=True)

        # Edit panel (initially hidden)
        self.edit_panel = EditPanel(self.main_frame, self)
        self.edit_panel.pack(side='right', fill='y', padx=10, pady=10)
        self.edit_panel.pack_forget()  # hide initially
        
        
    def open_img(self):
      file_path = filedialog.askopenfilename(
          title="Select an image",
          filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
      )
      
      if file_path:
          self.img = Image.open(file_path)
          self.display_img()
          
    def display_img(self):
      if self.img:
          disp_img = self.img.copy()
          disp_img.thumbnail((500,500))
          self.tk_img = CTkImage(light_image=disp_img, size=disp_img.size)
          self.canvas.configure(image=self.tk_img)
          
    def apply_edits(self, edits):
        if not self.img:
            return

        img = self.img.copy()

        # Apply brightness
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(edits["Brightness"])

        # Apply contrast
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(edits["Contrast"])

        # Exposure - approximate by adjusting brightness again
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(edits["Exposure"])

        # Saturation
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(edits["Saturation"])

        # Sharpness
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(edits["Sharpness"])

        # Highlights - no direct PIL method; approximate by adjusting brightness of bright areas:
        # For a simple approach, let's blend with a brightened version controlled by Highlights slider
        if edits["Highlights"] > 0:
            bright = img.point(lambda p: min(255, int(p * (1 + edits["Highlights"])))
                              )
            img = Image.blend(img, bright, alpha=0.5)

        self.edited_img = img
        self.show_edited_img()

    def show_edited_img(self):
        disp_img = self.edited_img.copy()
        disp_img.thumbnail((500, 500))
        self.tk_img = CTkImage(light_image=disp_img, size=disp_img.size)
        self.canvas.configure(image=self.tk_img)
        
          
    
          
if __name__ == "__main__":
    app = App()
    app.mainloop()
