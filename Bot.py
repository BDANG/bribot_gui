from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from src.Settings import Settings
from src.CardHandler import CardHandler
from src.ProductHandler import ProductHandler

class Bot(Frame):
    def __init__(self, master):
        #Frame.__init__(self, master)
        self.master = master
        self.notebook = Notebook(master)
        self.notebook.grid(column=0, row=0, sticky=(N, W, E, S))
        self._init_tabs()
        #print(self.notebook.children)

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
                    offvalue="no").grid(row=2, column=1)

        productSearchVar = StringVar()
        Checkbutton(runFrame,
                    text="Automatic Product Search",
                    variable=productSearchVar,
                    onvalue="yes",
                    offvalue="no").grid(row=2, column=2)

        checkoutVar = StringVar()
        Checkbutton(runFrame,
                    text="Automatic Checkout",
                    variable=checkoutVar,
                    onvalue="yes",
                    offvalue="no").grid(row=2, column=3)


        #### Init Browser Button
        browserLaunchButton = Button(runFrame, text="1. Initialize").grid(row=3, column=1)

        #### Start/Fire Button
        dropDetectorButton = Button(runFrame, text="2. Run").grid(row=3, column=2)

        #### Speed Mode
        Label(runFrame, text="Mode:").grid(row=4, column=1)

        # maintain reference?
        modeLabel = Label(runFrame, text="Free (slowest)").grid(row=4, column=2)

        self.notebook.add(runFrame, text="Run")


    def _init_products_frame(self):
        productFrame = Frame(self.notebook, padding=0, name="products")

        tree = Treeview(productFrame,
                        name="tree_products",
                        columns=["cardID", "keywords", "type", "size", "color"],
                        displaycolumns=["cardID", "keywords", "type", "size", "color"],
                        show="headings")
        tree.heading("cardID", text="Using Card")
        tree.heading("keywords", text="Keywords")
        tree.heading("type", text="Type")
        tree.heading("size", text="Size")
        tree.heading("color", text="Color Keywords")

        tree.grid(row=2, columns=1, columnspan=6)


        # insert dummy data for now
        tree.insert('', 'end', values=("1", "Box Logo", "sweatshirts", "Medium", "Black, Red"))
        tree.insert('', 'end', values=("1", "Hanes, Boxers", "accessories", "Small", "White"))

        # special class for handling the product GUI functions (adding, editing, deleting, saving, loading)
        productHandler = ProductHandler(tree)

        # button for adding new products
        Button(productFrame, name="button_add_product", text="Add", command=lambda: productHandler.add_product()).grid(row=1, column=1, sticky=W)

        # button for editing products
        Button(productFrame, name="button_edit_product", text="Edit", command=lambda: productHandler.edit_product()).grid(row=1, column=2, sticky=W)

        # button for deleting products, WIP: disable when no cards to delete
        Button(productFrame, name="button_delete_product", text="Delete", command=lambda: productHandler.delete_product()).grid(row=1, column=3, sticky=W)

        # button for saving products
        Button(productFrame, name="button_save_product", text="Save", command=lambda: productHandler.save_products()).grid(row=1, column=4, sticky=W)

        # button for loading products
        Button(productFrame, name="button_load_product", text="Load", command=lambda: productHandler.load_products()).grid(row=1, column=5, sticky=W)


        self.notebook.add(productFrame, text="Products")

    def _init_cards_frame(self):
        cardFrame = Frame(self.notebook, padding=0, name="cards")


        # Treeview (Table) of card data
        tree = Treeview(cardFrame,
                        name="tree_cards",
                        columns=["fname", "lname", "email", "phone"],
                        displaycolumns="#all")
        tree.heading("#0", text="ID Number")
        tree.heading("fname", text="First Name")
        tree.heading("lname", text="Last Name")
        tree.heading("email", text="Email")
        tree.heading("phone", text="Phone")
        tree.grid(row=2, columns=1, columnspan=5)

        # insert dummy data for now
        tree.insert('', 'end', text="1", values=("Brian", "Dang", "abc@abc.com", "412-111-2222"))
        tree.insert('', 'end', text="2", values=("Brian2", "Dang", "xyz@xyz.com", "412-222-3333"))

        cardHandler = CardHandler(tree)

        # button for adding new cards
        Button(cardFrame, name="button_add_card", text="Add", command=lambda: cardHandler.add_card()).grid(row=1, column=1, sticky=W)

        # button for deleting cards, WIP: disable when no cards to delete
        Button(cardFrame, name="button_delete_card", text="Delete", command=lambda: cardHandler.delete_card()).grid(row=1, column=2, sticky=W)

        # button for saving cards
        Button(cardFrame, name="button_save_cards", text="Save", command=lambda: print("TERRIBLE")).grid(row=1, column=3, sticky=W)

        # button for loading cards
        Button(cardFrame, name="button_load_cards", text="Load", command=lambda: print("TERRIBLE")).grid(row=1, column=4, sticky=W)

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
        Text(upgradeFrame, width=15, height=0.8).grid(row=3, column=2)
        Button(upgradeFrame, text="Upgrade!").grid(row=3, column=3)

        self.notebook.add(upgradeFrame, text="Upgrade")


    def _init_settings_frame(self):
        '''
        Handles the necessary operations required to initialize the settings tab.
        1. Loads previous settings if they exist, otherwise intialize to default
        2. Save any changes to allow persistence of settings.
        3. Restore default settings.
        '''
        # maintain a frame for everything in the settings tab
        settingsFrame = Frame(self.notebook, padding=0, name="settings")

        # load existing settings, otherwise intialize default values
        self.settings = Settings().load_from_file("settings.txt")

        #### Refresh settings
        ### Minimum Refresh Speed
        Label(settingsFrame, text="Minimum Drop Refresh (seconds):").grid(row=1,column=1, sticky=W)
        minRefreshEntry = Entry(settingsFrame, name="entry_min_refresh", width=4, takefocus=0)
        minRefreshEntry.grid(row=1, column=2, sticky=W)

        # set the value according to exisiting settings, or defaults
        minRefreshEntry.delete(0, END)
        minRefreshEntry.insert(0, self.settings.MIN_REFRESH)


        ### Maximum Refresh Speed
        Label(settingsFrame, text="Maximum Drop Refresh (seconds):").grid(row=2,column=1, sticky=W)
        maxRefreshEntry = Entry(settingsFrame, name="entry_max_refresh", width=4, takefocus=0)
        maxRefreshEntry.grid(row=2, column=2, sticky=W)

        # set the value according to exisiting settings, or defaults
        maxRefreshEntry.delete(0, END)
        maxRefreshEntry.insert(0, self.settings.MAX_REFRESH)

        #### Delay settings
        ### Checkout Delay
        Label(settingsFrame, text="Checkout Delay (seconds):").grid(row=3, column=1, sticky=W)
        checkoutDelayEntry = Entry(settingsFrame, name="entry_checkout_delay", width=4, takefocus=0)
        checkoutDelayEntry.grid(row=3, column=2, sticky=W)

        # set the value according to existing settings, or defaults
        checkoutDelayEntry.delete(0, END)
        checkoutDelayEntry.insert(0, self.settings.CHECKOUT_DELAY)


        #### Default/Save operations
        ### Restoring to defaults
        # call a function and pass the entries that will be reset, overrides existing settings file
        Button(settingsFrame,
               text="Restore Default",
               takefocus=0,
               command=lambda: self.settings.reset_to_default("settings.txt",
                                                              settingsFrame.children["entry_min_refresh"],
                                                              settingsFrame.children["entry_max_refresh"],
                                                              settingsFrame.children["entry_checkout_delay"])
               ).grid(row=4, column=1, sticky=W)

        ### Saving the current settings for persistence
        # call a function that haphazardly writes to a file
        Button(settingsFrame,
               text="Save",
               takefocus=0,
               command=lambda: self.settings.save_to_file(
                                             "settings.txt",
                                             minRefreshEntry.get(),
                                             maxRefreshEntry.get(),
                                             checkoutDelayEntry.get())
               ).grid(row=4, column=3, sticky=E)

        self.notebook.add(settingsFrame, text="Settings")





if __name__ == "__main__":
    root = Tk()
    root.title("Bri Bot")
    Bot(root)
    root.mainloop()
