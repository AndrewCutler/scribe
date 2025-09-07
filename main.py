# file: image_app.py
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageOps


class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cross-Platform Image POC")
        self.root.geometry("600x500")

        # GUI elements
        self.label = tk.Label(root, text="No image loaded")
        self.label.pack(pady=10)

        self.canvas = tk.Canvas(root, width=500, height=400, bg="gray")
        self.canvas.pack()

        self.load_btn = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_btn.pack(pady=5)

        self.gray_btn = tk.Button(
            root, text="Convert to Grayscale", command=self.convert_gray
        )
        self.gray_btn.pack(pady=5)

        self.resize_btn = tk.Button(root, text="Resize 50%", command=self.resize_image)
        self.resize_btn.pack(pady=5)

        self.image = None
        self.tk_image = None

    def load_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        if path:
            self.image = Image.open(path)
            self.display_image(self.image)
            self.label.config(text=path)

    def display_image(self, img):
        # Resize to fit canvas
        img_resized = ImageOps.contain(img, (500, 400))
        self.tk_image = ImageTk.PhotoImage(img_resized)
        self.canvas.create_image(250, 200, image=self.tk_image)

    def convert_gray(self):
        if self.image:
            gray = self.image.convert("L")
            self.display_image(gray)
            self.image = gray
        else:
            messagebox.showwarning("Warning", "Load an image first!")

    def resize_image(self):
        if self.image:
            w, h = self.image.size
            resized = self.image.resize((w // 2, h // 2))
            self.display_image(resized)
            self.image = resized
        else:
            messagebox.showwarning("Warning", "Load an image first!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()
