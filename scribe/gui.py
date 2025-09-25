import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
from .core import load_image, copy_to_clipboard, convert_to_text

BASE_HEIGHT = 100
BASE_WIDTH = 400
PADDING = 10

BG_COLOR = "#1a1a1a"
FG_COLOR = "#ddd"

cursor_x, cursor_y = 0, 0


def track_cursor(event):
    global cursor_x, cursor_y
    cursor_x, cursor_y = event.x, event.y


class ImageApp:
    def render_initial(self):
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

    def render_image_loaded(self):
        if not hasattr(self, 'canvas_widget'):
            self.canvas_widget = tk.Canvas(
                self.root, width=self.image.width, height=self.image.height, bg="black"
            )
            self.canvas_widget.grid(
                row=2, column=0, padx=PADDING, pady=PADDING)
        else:
            # Update existing canvas size
            self.canvas_widget.config(
                width=self.image.width, height=self.image.height)

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

    def render_image_converted(self):
        self.text_widget.configure(state=tk.NORMAL)
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(1.0, self.extracted_text.strip())
        self.text_widget.update_idletasks()
        self.text_widget.config(height=2)
        self.text_widget.unbind("<Button-1>")
        self.text_widget.bind(
            "<Button-1>", lambda ev: copy_to_clipboard(self.extracted_text))
        self.text_widget.configure(state=tk.DISABLED)

    def __init__(self, root):
        self.root = root
        self.loading = False
        self.image = None
        self.tk_image = None

        self.root.title("Scribe")
        self.root.configure(bg=BG_COLOR)

        self.style = ttk.Style(self.root)
        self.style.configure(".", background=BG_COLOR, foreground=FG_COLOR)
        self.style.configure(
            "TLabel",
            background=BG_COLOR,
            foreground=FG_COLOR,
        )
        self.style.configure("TButton", foreground=BG_COLOR)

        self.render_initial()

    def load_image(self, event=None):
        path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        if path:
            self.image = Image.open(path)
            self.label.config(text=path)
            self.image_data = load_image(path)
            self.render_image_loaded()
        else:
            raise FileNotFoundError(path)

    def convert_text(self, event=None):
        if self.image:
            if self.loading:
                return
            self.loading = True
            self.text_widget.delete(1.0, tk.END)

            self.extracted_text = convert_to_text(self.image_data)
            self.render_image_converted()
            self.image_data = None
            self.loading = False
        else:
            messagebox.showwarning("Warning", "Load an image first!")


def run():
    root = tk.Tk()
    try:
        root.iconbitmap("icon.ico")
    except tk.TclError:
        # Icon file not found, continue without icon
        pass
    root.bind("<Motion>", track_cursor)
    app = ImageApp(root)
    root.mainloop()
