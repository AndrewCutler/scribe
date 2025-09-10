# file: image_app.py
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageEnhance, ImageTk
import easyocr
import cv2
import pyperclip

# TODO: Use grid() with rowconfigure / columnconfigure
# .geometry(), grid_rowconfigure() etc.

BASE_HEIGHT = 100
BASE_WIDTH = 400
PADDING = 10


# reader = easyocr.Reader(["en"])
reader = easyocr.Reader(["en"], gpu=True)


class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scribe")
        self.root.geometry(f"{BASE_WIDTH}x{BASE_HEIGHT}")

        # GUI elements
        self.label = tk.Label(root, text="No image loaded")
        self.label.pack(pady=10)

        self.load_btn = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_btn.pack(pady=5)

        self.image = None
        self.tk_image = None

    def load_image(self):
        path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        if path:
            self.image = Image.open(path)
            self.label.config(text=path)
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

            resized = cv2.resize(img, None, fx=2, fy=2)
            sharpened = resized
            sharpened = cv2.GaussianBlur(resized, (0, 0), 3)
            sharpened = cv2.addWeighted(resized, 1.5, sharpened, -0.5, 0)
            cv2.imwrite("temp.png", sharpened)

            self.gray_btn = tk.Button(
                root, text="Convert to text", command=self.convert_text
            )
            self.gray_btn.pack(pady=5)

            self.root.geometry(
                f"{max(self.image.width, BASE_WIDTH)}x{max(self.image.height, BASE_HEIGHT)}"
            )

            self.canvas = tk.Canvas(
                root, width=self.image.width, height=self.image.height, bg="grey"
            )
            self.canvas.pack(padx=10, pady=10)

            self.display_image(self.image)

    def display_image(self, img):
        # Resize to fit canvas
        # img_resized = ImageOps.contain(img, (img.height, img.width))
        # self.tk_image = ImageTk.PhotoImage(img_resized)
        # TODO: fix sizing
        self.tk_image = ImageTk.PhotoImage(img)
        # print(f"Image dimensions: {img.width}x{img.height}")
        #
        # self.canvas.create_image(img.width, img.height, image=self.tk_image)
        # self.canvas.create_image((50, 50), image=tk_image)
        self.canvas.create_image((img.width / 2, img.height / 2), image=self.tk_image)

        self.root.geometry(
            f"{max(img.width + PADDING * 2, BASE_WIDTH)}x{max(img.height + BASE_HEIGHT + PADDING * 2, BASE_HEIGHT)}"
        )

    def convert_text(self):
        if self.image:
            result = reader.readtext("temp.png", decoder="wordbeamsearch")

            if not hasattr(self, "text_widget"):
                self.text_widget = tk.Text(
                    self.root, height=8, wrap=tk.WORD, cursor="hand2"
                )
                self.text_widget.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

                def callback(event):
                    pyperclip.copy(self.extracted_text)

                self.text_widget.bind("<Button-1>", callback)
            self.text_widget.delete(1.0, tk.END)

            self.extracted_text = ""
            for bbox, text, confidence in result:
                print(f"{text} ({confidence*100:.2f}%)")
                self.extracted_text += text + " "

            self.text_widget.insert(1.0, self.extracted_text.strip())

            self.root.geometry(
                f"{max(self.image.width + PADDING * 2, BASE_WIDTH)}x{max(self.image.height + BASE_HEIGHT + 200, BASE_HEIGHT)}"
            )

            # delete temp.png
        else:
            messagebox.showwarning("Warning", "Load an image first!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()
