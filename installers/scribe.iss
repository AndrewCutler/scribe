; Generates installer for Windows. Requires Inno.
; https://jrsoftware.org/isinfo.php

[Setup]
AppName=Scribe
AppVersion=1.0
DefaultDirName={pf}\Scribe
DefaultGroupName=Scribe
OutputDir=dist
OutputBaseFilename=scribe_installer
ArchitecturesInstallIn64BitMode=x64
PrivilegesRequired=admin

[Files]
Source: "..\dist\scribe\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\Scribe"; Filename: "{app}\scribe.exe"
Name: "{group}\Scribe CLI"; Filename: "{app}\scribe-cli.exe"

[Tasks]
Name: "addtopath"; Description: "Add Scribe to PATH"; Flags: unchecked

[Run]
Filename: "{app}\scribe.exe"; Description: "Launch Scribe"; Flags: nowait postinstall skipifsilent

[Registry]
; Adds install dir to PATH if user selects that option
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; \
ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}"; Tasks: addtopath; Flags: preservestringtype
