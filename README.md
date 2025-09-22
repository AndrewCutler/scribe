## For devs

### GUI app
#### To run
In root directory, `watchmedo auto-restart --patterns='scribe/gui.py;scribe/core.py' --recursive -- python gui_entry.py`

#### To build
`pyinstaller --onefile gui_entry.py`

### CLI app
#### To run
In root directory, `python cli.py [path_to_image]`

#### To build
`pyinstaller --onefile cli_entry.py`
