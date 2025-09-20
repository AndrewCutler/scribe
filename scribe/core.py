import easyocr
import cv2
import pyperclip
from termcolor import colored

reader = easyocr.Reader(["en"], gpu=True)

def copy_to_clipboard(extracted_text):
    pyperclip.copy(extracted_text)
    print(colored("Text copied to clipboard.", "green"))


def convert_image_to_text(image_data):
    print(colored("Converting to text...", "yellow"))
    result = reader.readtext(image_data, decoder="wordbeamsearch")

    extracted_text = ""
    for bbox, text, confidence in result:
        print(f"{text} ({confidence*100:.2f}%)")
        extracted_text += text + " "

    print(colored("Conversion done.", "green"))

    copy_to_clipboard(extracted_text)

    return extracted_text


def load_image(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    print(colored("Image found.", "green"))
    resized = cv2.resize(img, None, fx=2, fy=2)
    sharpened = resized
    sharpened = cv2.GaussianBlur(resized, (0, 0), 3)
    sharpened = cv2.addWeighted(resized, 1.5, sharpened, -0.5, 0)
    image_data = sharpened
    print(colored("Image processed.", "green"))
    return image_data