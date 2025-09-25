# Scribe

Scribe is a powerful OCR (Optical Character Recognition) application that extracts text from images using EasyOCR. It provides both a command-line interface (CLI) and a graphical user interface (GUI) for different use cases.

## Features

- **High Accuracy OCR**: Uses EasyOCR with GPU acceleration for fast and accurate text extraction
- **Image Processing**: Automatically enhances images with resizing, sharpening, and noise reduction
- **Dual Interface**: Both CLI and GUI options for different workflows
- **Clipboard Integration**: Automatically copies extracted text to clipboard
- **Multiple Image Formats**: Supports PNG, JPG, JPEG, BMP, and GIF files
- **Confidence Scoring**: Shows confidence levels for each detected text segment

## Installation

### Prerequisites

- Python 3.7+
- CUDA-compatible GPU (recommended for better performance)
- Required Python packages:
  - `easyocr`
  - `opencv-python`
  - `pyperclip`
  - `termcolor`
  - `click`
  - `pillow`

### Install Dependencies

```bash
pip install easyocr opencv-python pyperclip termcolor click pillow
```

### Build Executables (Optional)

The project includes PyInstaller spec files for building standalone executables:

```bash
# Build CLI executable
pyinstaller cli_optimized.spec

# Build GUI executable  
pyinstaller gui_entry.spec

# Build both
pyinstaller build.spec
```

## Usage

### Command Line Interface (CLI)

The CLI application is perfect for batch processing, automation, and quick text extraction from command line.

#### Basic Usage

```bash
python cli_entry.py path/to/image.png
```

#### Features

- **Simple Command**: Just provide the image path as an argument
- **Automatic Processing**: Loads, enhances, and processes the image automatically
- **Real-time Feedback**: Shows progress with colored terminal output
- **Confidence Display**: Displays confidence percentage for each detected text segment
- **Clipboard Integration**: Automatically copies the final extracted text to clipboard

#### Example Output

```
Initializing OCR engine...
OCR engine ready.
Image found.
Image processed.
Converting to text...
Hello World (95.23%)
This is a test (87.45%)
Conversion done.
Text copied to clipboard.
TEXT:
Hello World This is a test
```

### Graphical User Interface (GUI)

The GUI application provides an intuitive visual interface for interactive text extraction.

#### Launching the GUI

```bash
python gui_entry.py
```

#### Features

- **Drag & Drop Interface**: Click to load images through a file dialog
- **Image Preview**: View the loaded image before processing
- **Interactive Workflow**: 
  1. Click "Click to load an image" to select an image file
  2. Click "Click to convert to text" to extract text
  3. Click the extracted text to copy it to clipboard
- **Visual Feedback**: Clear status messages guide you through the process
- **Modern Dark Theme**: Clean, professional interface

#### Supported Image Formats

- PNG
- JPG/JPEG
- BMP
- GIF

## How It Works

### Image Processing Pipeline

1. **Image Loading**: Loads the image using OpenCV
2. **Enhancement**: 
   - Converts to grayscale
   - Resizes image (2x scale for better OCR accuracy)
   - Applies Gaussian blur and sharpening filters
3. **OCR Processing**: Uses EasyOCR with word beam search decoder
4. **Text Extraction**: Combines all detected text segments
5. **Clipboard Integration**: Automatically copies result to system clipboard

### OCR Engine

- **Engine**: EasyOCR with English language support
- **GPU Acceleration**: Automatically uses GPU when available
- **Decoder**: Word beam search for improved accuracy
- **Confidence Scoring**: Provides confidence levels for each text detection

## Project Structure

```
scribe/
├── scribe/
│   ├── __init__.py
│   ├── core.py          # Core OCR functionality
│   ├── cli.py           # CLI interface
│   └── gui.py           # GUI interface
├── cli_entry.py         # CLI entry point
├── gui_entry.py         # GUI entry point
├── build.spec           # PyInstaller spec for building
├── cli_optimized.spec   # Optimized CLI build
└── gui_entry.spec       # GUI build spec
```

## Development

### Running from Source

```bash
# CLI
python -m scribe.cli path/to/image.png

# GUI
python -m scribe.gui
```

### Building Executables

```bash
# Install PyInstaller
pip install pyinstaller

# Build optimized CLI
pyinstaller cli_optimized.spec

# Build GUI
pyinstaller gui_entry.spec
```

## Performance Tips

- **GPU Usage**: Ensure CUDA is properly installed for GPU acceleration
- **Image Quality**: Higher resolution images generally produce better results
- **Image Preprocessing**: The application automatically enhances images, but clean, well-lit images work best
- **Text Orientation**: Ensure text is horizontal for best results

## Troubleshooting

### Common Issues

1. **CUDA/GPU Issues**: If GPU initialization fails, the application will fall back to CPU processing
2. **Image Loading**: Ensure the image file exists and is in a supported format
3. **Memory Usage**: Large images may require significant memory; consider resizing very large images

### Error Messages

- `"Image found."` - Successfully loaded image
- `"OCR engine ready."` - OCR engine initialized successfully
- `"Text copied to clipboard."` - Text extraction completed and copied

## License

This project is open source. Please check the license file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## Support

For issues, questions, or contributions, please use the project's issue tracker.