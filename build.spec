# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ["cli_entry.py"],
    pathex=[],
    binaries=[],
    datas=[('icon.ico', '.')],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

# Build the Python archive
pyz = PYZ(a.pure)

# GUI entry point
gui_exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='scribe',
    console=False,
    icon='icon.ico'
)

# CLI entry point
cli_exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='scribe-cli',
    console=True,    # console enabled for CLI
)
