# -*- mode: python ; coding: utf-8 -*-

# GUI Analysis
gui_analysis = Analysis(
    ["gui_entry.py"],
    pathex=[],
    binaries=[],
    datas=[('icon.ico', '.')],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

# CLI Analysis
cli_analysis = Analysis(
    ["cli_entry.py"],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['easyocr', 'cv2', 'pyperclip', 'termcolor', 'click', 'PIL', 'PIL.Image', 'PIL.ImageTk'],
    hookspath=[],
    runtime_hooks=[],
    excludes=['tkinter', 'matplotlib', 'numpy.distutils'],
    noarchive=False,
)

# Build the Python archives
gui_pyz = PYZ(gui_analysis.pure)
cli_pyz = PYZ(cli_analysis.pure)

# GUI entry point
gui_exe = EXE(
    gui_pyz,
    gui_analysis.scripts,
    gui_analysis.binaries,
    gui_analysis.datas,
    [],
    name='scribe',
    console=False,
    icon='icon.ico'
)

# CLI entry point
cli_exe = EXE(
    cli_pyz,
    cli_analysis.scripts,
    cli_analysis.binaries,
    cli_analysis.datas,
    [],
    name='scribe-cli',
    console=True,    # console enabled for CLI
    bootloader_ignore_signals=False,
    strip=True,      # Strip debug info for faster startup
    upx=True,        # Compress for smaller size
    runtime_tmpdir=None,
)
