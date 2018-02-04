from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Notebook")

notebook = ttk.Notebook(root, padding=0)
notebook.grid(column=0, row=0, sticky=(N, W, E, S))


#runFrame = ttk.Frame(notebook)
runFrame = ttk.Frame(notebook, padding=0)
#runFrame.grid(column=0, row=0)
ttk.Label(runFrame, text="Bri Bot").grid(column=2, row=1)

cardFrame = ttk.Frame(notebook)
#cardFrame.grid(column=0, row=0)
ttk.Label(cardFrame, text="Cards").grid(column=1, row=1)

notebook.add(runFrame, text="Run")
notebook.add(cardFrame, text="Cards")


root.mainloop()
