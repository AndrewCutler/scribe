import cv2
import click
from termcolor import colored
from .core import copy_to_clipboard, convert_to_text, load_image


def convert_image(image_data):
    extracted_text = convert_to_text(image_data)
    copy_to_clipboard(extracted_text)

    return extracted_text


def get_image_data(path):
    image_data = load_image(path)
    return image_data


@click.command()
@click.argument("path")
def run(path):
    print(path)
    image_data = get_image_data(path)
    converted = convert_image(image_data)
    print(colored("TEXT:", "blue"))
    print(converted)


if __name__ == "__main__":
    run()
