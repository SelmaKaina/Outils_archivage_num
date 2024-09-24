import binascii
from tkinter.filedialog import askopenfilename, askdirectory
from pathlib import Path

input("Choisir un fichier")
file = askopenfilename()

with open(file, 'rb') as f:
    hexdata = binascii.hexlify(f.read())

hexdata = str(hexdata)
hexdata = hexdata[2:-1]

input("Choisir la destination")
repository = askdirectory()

file = Path(file)
file_name = file.stem

destination = repository + '/' + str(file_name) + '.txt'

with open(destination, 'w') as text_file:
    text_file.write(str(hexdata))