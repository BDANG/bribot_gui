from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

class Bot(Frame):
    def __init__(self, master):
        #Frame.__init__(self, master)
        self.master = master
        self.notebook = Notebook(master)
        self.notebook.grid(column=0, row=0, sticky=(N, W, E, S))
        self._init_tabs()
        print(self.notebook.children)

    def _init_tabs(self):
        self._init_run_frame()
        self._init_products_frame()
        self._init_cards_frame()
        self._init_upgrade_frame()
        self._init_settings_frame()

    def _init_run_frame(self):
        runFrame = Frame(self.notebook, padding=0, name="run")

        Label(runFrame, text="Bri Bot").grid(row=1, column=1)

        dropDetectVar = StringVar()
        Checkbutton(runFrame,
                    text="Automatic Drop Detection",
                    variable=dropDetectVar,
                    onvalue="yes",
                    offvalue="no").grid(row=2, column=3)


        #### Init Browser Button
        browserLaunchButton = Button(runFrame, text="1. Initialize").grid(row=2, column=1)

        #### Start/Fire Button
        dropDetectorButton = Button(runFrame, text="2. Run").grid(row=2, column=2)

        #### Speed Mode
        Label(runFrame, text="Mode:").grid(row=3, column=1)

        # maintain reference?
        modeLabel = Label(runFrame, text="Free (slowest)").grid(row=3, column=2)

        self.notebook.add(runFrame, text="Run")


    def _init_products_frame(self):
        productFrame = Frame(self.notebook, padding=0, name="products")

        tree = Treeview(productFrame)#.grid(row=1, column=1)

        tree.insert('', 'end', 'widgets', text='Widget Tour')

        # Same thing, but inserted as first child:
        tree.insert('', 0, 'gallery', text='Applications')

        # Treeview chooses the id:
        id = tree.insert('', 'end', text='Tutorial')

        # Inserted underneath an existing node:
        tree.insert('widgets', 'end', text='Canvas')
        tree.insert(id, 'end', text='Tree')


        self.notebook.add(productFrame, text="Products")

    def _init_cards_frame(self):
        cardFrame = Frame(self.notebook, padding=0, name="cards")
        self.notebook.add(cardFrame, text="Cards")

    def _init_upgrade_frame(self):
        upgradeFrame = Frame(self.notebook, padding=0, name="upgrade")

        # report current speed mode
        Label(upgradeFrame, text="Current:").grid(row=1, column=1)
        # wip: referencing main page?
        Label(upgradeFrame, text="Free (Slow)").grid(row=1, column=2)

        # link redirect to upgrades
        Button(upgradeFrame, text="Purchase").grid(row=2, column=1)

        #### Upgrade code
        Label(upgradeFrame, text="Upgrade Code: ").grid(row=3, column=1)
        Text(upgradeFrame, width=15, height=1).grid(row=3, column=2)
        Button(upgradeFrame, text="Upgrade!").grid(row=3, column=3)

        self.notebook.add(upgradeFrame, text="Upgrade")


    def _init_settings_frame(self):
        settingsFrame = Frame(self.notebook, padding=0, name="settings")
        self.notebook.add(settingsFrame, text="Settings")





if __name__ == "__main__":
    root = Tk()
    root.title("Bri Bot")
    Bot(root)
    root.mainloop()
