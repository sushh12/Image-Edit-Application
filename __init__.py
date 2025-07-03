import customtkinter as ctk
from tkinter import filedialog
# from tkinter import messagebox
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("500x500")

def upload_img():
    file = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )

    if file:
        img = Image.open(file)
        img = img.resize((400,400))
        img_ctk = ctk.CTkImage(light_image=img, dark_image=img, size=(300,300))

        image_label.configure(image=img_ctk, text="")
        image_label.image = img_ctk


# Layout

upload_btn = ctk.CTkButton(root, text="Upload", command=upload_img)
upload_btn.pack(pady=20)

save_btn = ctk.CTkButton(root, text="Save Image")
save_btn.place(relx=0.5, rely=0.9, anchor='s')

image_label = ctk.CTkLabel(root, text="")
image_label.pack()

root.mainloop()

