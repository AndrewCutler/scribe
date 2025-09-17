# file: image_app.py
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageEnhance, ImageTk
import easyocr
import cv2
import pyperclip

BASE_HEIGHT = 100
BASE_WIDTH = 400
PADDING = 10

BG_COLOR = "#1a1a1a"
FG_COLOR = "#ddd"

# reader = easyocr.Reader(["en"])
reader = easyocr.Reader(["en"], gpu=True)

cursor_x, cursor_y = 0, 0


def track_cursor(event):
    global cursor_x, cursor_y
    cursor_x, cursor_y = event.x, event.y


class ImageApp:
    def __init__(self, root):
        self.root = root
        self.loading = False
        self.image = None
        self.tk_image = None

        self.root.title("Scribe")
        self.root.configure(bg=BG_COLOR)

        self.label = ttk.Label(self.root, text="No image loaded")
        self.label.grid(row=0, column=0, pady=PADDING)

        self.text_widget = tk.Text(
            self.root,
            bg=FG_COLOR,
            fg=BG_COLOR,
            insertbackground="yellow",
            cursor="hand2",
            height=2,
        )
        self.text_widget.grid(row=1, column=0, padx=PADDING, pady=PADDING)
        self.text_widget.insert(tk.END, "Click to load an image")
        self.text_widget.configure(state=tk.DISABLED)
        self.text_widget.bind("<Button-1>", self.load_image)

        self.style = ttk.Style(self.root)
        self.style.configure(".", background=BG_COLOR, foreground=FG_COLOR)
        self.style.configure(
            "TLabel",
            background=BG_COLOR,
            foreground=FG_COLOR,
        )
        self.style.configure("TButton", foreground=BG_COLOR)

    def load_image(self, event=None):
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
            self.image_data = sharpened

            self.canvas_widget = tk.Canvas(
                root, width=self.image.width, height=self.image.height, bg="black"
            )
            self.canvas_widget.grid(row=2, column=0, padx=PADDING, pady=PADDING)

            # TODO: fix sizing
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.canvas_widget.create_image(
                (self.image.width / 2, self.image.height / 2), image=self.tk_image
            )

            self.text_widget.configure(state=tk.NORMAL)
            self.text_widget.delete(1.0, tk.END)
            self.text_widget.insert("end", "Click to convert to text")
            self.text_widget.configure(state=tk.DISABLED)
            self.text_widget.unbind("<Button-1>")
            self.text_widget.bind("<Button-1>", self.convert_text)

    def convert_text(self, event=None):
        if self.image:
            if self.loading:
                return
            self.loading = True
            result = reader.readtext(self.image_data, decoder="wordbeamsearch")
            self.text_widget.delete(1.0, tk.END)

            self.extracted_text = ""
            for bbox, text, confidence in result:
                print(f"{text} ({confidence*100:.2f}%)")
                self.extracted_text += text + " "

            def copy_to_clipboard(event=None):
                pyperclip.copy(self.extracted_text)
                load_another_button_widget = tk.Button(
                    self.root, text="Load another image", command=self.load_image
                )
                load_another_button_widget.grid(
                    row=1, column=0, padx=PADDING, pady=PADDING
                )
                self.text_widget.grid(row=2)
                self.canvas_widget.grid(row=3)

            self.text_widget.configure(state=tk.NORMAL)
            self.text_widget.delete(1.0, tk.END)
            self.text_widget.insert(1.0, self.extracted_text.strip())
            self.text_widget.update_idletasks()
            self.text_widget.config(height=2)
            self.text_widget.unbind("<Button-1>")
            self.text_widget.bind("<Button-1>", copy_to_clipboard)
            self.text_widget.configure(state=tk.DISABLED)

            copy_to_clipboard()
            self.image_data = None
            self.loading = False
        else:
            messagebox.showwarning("Warning", "Load an image first!")


if __name__ == "__main__":
    root = tk.Tk()
    root.bind("<Motion>", track_cursor)
    app = ImageApp(root)
    root.mainloop()
