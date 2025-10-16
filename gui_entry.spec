# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['gui_entry.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'timeit',
        'torch',
        'torch._utils_internal',
        'torch._strobelight.compile_time_profiler',
        'torch._strobelight.cli_function_profiler',
        'easyocr',
        'cv2',
        'pyperclip',
        'termcolor',
        'click'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='gui_entry',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
