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
    excludes=['tkinter', 'matplotlib', 'numpy.distutils', 'scipy', 'sklearn', 'tensorflow', 'torch'],
    noarchive=False,
)

# Build the Python archives
gui_pyz = PYZ(gui_analysis.pure)
cli_pyz = PYZ(cli_analysis.pure)

# GUI entry point
gui_exe = EXE(
    gui_pyz,
    gui_analysis.scripts,
    [],  # Empty binaries list for directory mode
    exclude_binaries=True,  # Don't include binaries in EXE
    name='scribe',
    console=False,
    onefile=False,
    icon='icon.ico',
)

# CLI entry point
cli_exe = EXE(
    cli_pyz,
    cli_analysis.scripts,
    [],  # Empty binaries list for directory mode
    exclude_binaries=True,  # Don't include binaries in EXE
    name='scribe-cli',
    console=True,    # console enabled for CLI
    bootloader_ignore_signals=False,
    strip=False,     # Disable strip to avoid startup overhead
    upx=False,       # Disable UPX compression for faster startup
    runtime_tmpdir=None,
    onefile=False,
)

# Combined Collection - both executables in one directory
combined_coll = COLLECT(
    gui_exe,
    cli_exe,
    gui_analysis.binaries,
    cli_analysis.binaries,
    gui_analysis.zipfiles,
    cli_analysis.zipfiles,
    gui_analysis.datas,
    cli_analysis.datas,
    strip=False,
    upx=False,
    name='scribe'
)