# -*- mode: python ; coding: utf-8 -*-

# CLI Analysis for directory-based build (faster startup)
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

# Build the Python archive
cli_pyz = PYZ(cli_analysis.pure)

# CLI entry point (directory-based - much faster startup)
cli_exe = EXE(
    cli_pyz,
    cli_analysis.scripts,
    [],
    exclude_binaries=True,
    name='scribe-cli',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,
)

# Collect all files into a directory
cli_coll = COLLECT(
    cli_exe,
    cli_analysis.binaries,
    cli_analysis.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='scribe-cli',
)

