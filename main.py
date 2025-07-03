import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image
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
          
    
          
if __name__ == "__main__":
    app = App()
    app.mainloop()
