import click
from termcolor import colored


def convert_image(image_data):
    from .core import convert_to_text, copy_to_clipboard  # Import here to avoid slow startup
    extracted_text = convert_to_text(image_data)
    copy_to_clipboard(extracted_text)

    return extracted_text


def get_image_data(path):
    from .core import load_image  # Import here to avoid slow startup
    image_data = load_image(path)
    return image_data


@click.command()
@click.argument("path")
def run(path):
    print(colored("Scribe CLI starting...", "cyan"))
    print(f"Processing: {path}")
    image_data = get_image_data(path)
    converted = convert_image(image_data)
    print(colored("TEXT:", "blue"))
    print(converted)


if __name__ == "__main__":
    run()
