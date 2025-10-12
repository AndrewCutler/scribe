; Scribe Installer Script for NSIS
; This script creates a Windows installer for the Scribe application

;--------------------------------
; General

; The name of the installer
Name "Scribe"

; The file to write
OutFile "ScribeSetup.exe"

; The default installation directory
InstallDir "$PROGRAMFILES\Scribe"

; Registry key to check for directory (so if you install again, it will 
; overwrite the old one automatically)
InstallDirRegKey HKLM "Software\Scribe" "Install_Dir"

; Request application privileges for Windows Vista
RequestExecutionLevel admin

;--------------------------------
; Version Information

VIProductVersion "1.0.0.0"
VIAddVersionKey "ProductName" "Scribe"
VIAddVersionKey "CompanyName" "Scribe"
VIAddVersionKey "LegalCopyright" "© 2024 Scribe"
VIAddVersionKey "FileDescription" "Scribe Installer"
VIAddVersionKey "FileVersion" "1.0.0.0"

;--------------------------------
; Interface Settings

!define MUI_ABORTWARNING

; Include the Modern UI
!include "MUI2.nsh"

;--------------------------------
; Pages

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "LICENSE.txt"
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

;--------------------------------
; Languages

!insertmacro MUI_LANGUAGE "English"

;--------------------------------
; Installer Sections

Section "Scribe (required)" SecMain

  SectionIn RO

  ; Set output path to the installation directory.
  SetOutPath $INSTDIR

  ; Copy all files from dist/scribe/ to installation directory
  File /r "dist\scribe\*"

  ; Write the installation path into the registry
  WriteRegStr HKLM SOFTWARE\Scribe "Install_Dir" "$INSTDIR"

  ; Write the uninstall keys for Windows
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Scribe" "DisplayName" "Scribe"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Scribe" "UninstallString" '"$INSTDIR\uninstall.exe"'
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Scribe" "NoModify" 1
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Scribe" "NoRepair" 1
  WriteUninstaller "uninstall.exe"

  ; Create desktop shortcut for GUI
  CreateShortCut "$DESKTOP\Scribe.lnk" "$INSTDIR\scribe.exe"

  ; Create start menu shortcuts
  CreateDirectory "$SMPROGRAMS\Scribe"
  CreateShortCut "$SMPROGRAMS\Scribe\Scribe.lnk" "$INSTDIR\scribe.exe"
  CreateShortCut "$SMPROGRAMS\Scribe\Scribe CLI.lnk" "$INSTDIR\scribe-cli.exe"
  CreateShortCut "$SMPROGRAMS\Scribe\Uninstall.lnk" "$INSTDIR\uninstall.exe"

SectionEnd

;--------------------------------
; Uninstaller

Section "Uninstall"

  ; Remove registry keys
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Scribe"
  DeleteRegKey HKLM SOFTWARE\Scribe

  ; Remove files and uninstaller
  RMDir /r "$INSTDIR"

  ; Remove shortcuts, if any
  Delete "$DESKTOP\Scribe.lnk"
  RMDir /r "$SMPROGRAMS\Scribe"

SectionEnd
