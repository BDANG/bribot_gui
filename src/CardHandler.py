from pathlib import Path
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

class CardHandler:
    def __init__(self, tree):
        self.tree = tree
        self.PROMPT_DELETE = True

    def _add_card_to_tree(self, fname, lname, popup=None):

        self.tree.insert("", "end", text=self._get_next_card_num(), values=(fname, lname, "a", "ph"))

        if popup:
            popup.destroy()

    def add_card(self):
        # create pop up for entering details
        # wip: background color?
        popup = Toplevel()
        popup.title("Add a Card")

        #####################
        ##### Name Entry
        Label(popup, text="Name: ").grid(row=1, column=1, sticky=W)
        nameEntry = Entry(popup, name="entry_name", width=10)
        nameEntry.grid(row=1, column=2, sticky=W)

        #####################
        #### Email Entry
        Label(popup, text="Email: ").grid(row=2, column=1, sticky=W)
        emailEntry = Entry(popup, name="entry_email", width=10)
        emailEntry.grid(row=2, column=2, sticky=W)

        #####################
        #### Phone Entry: WIP validate format?
        Label(popup, text="Phone: ").grid(row=3, column=1, sticky=W)
        phoneEntry = Entry(popup, name="entry_phone", width=10)
        phoneEntry.grid(row=3, column=2, sticky=W)

        #####################
        #### Address Entry
        Label(popup, text="Address: ").grid(row=4, column=1, sticky=W)
        address1Entry = Entry(popup, name="entry_address1", width=10)
        address1Entry.grid(row=4, column=2, sticky=W)

        Label(popup, text="Apt / Unit: ").grid(row=5, column=1, sticky=W)
        addressAptEntry = Entry(popup, name="entry_apt", width=10)
        addressAptEntry.grid(row=5, column=2, sticky=W)

        Label(popup, text="Address: ").grid(row=6, column=1, sticky=W)
        address2Entry = Entry(popup, name="entry_address2", width=10)
        address2Entry.grid(row=6, column=2, sticky=W)

        #####################
        #### Zip Entry
        Label(popup, text="Zip: ").grid(row=7, column=1, sticky=W)
        zipEntry = Entry(popup, name="entry_zip", width=10)
        zipEntry.grid(row=7, column=2, sticky=W)

        #####################
        #### City Entry
        Label(popup, text="City: ").grid(row=8, column=1, sticky=W)
        cityEntry = Entry(popup, name="entry_city", width=10)
        cityEntry.grid(row=8, column=2, sticky=W)

        #####################
        #### State Entry
        Label(popup, text="State: ").grid(row=9, column=1, sticky=W)
        stateEntry = Entry(popup, name="entry_state", width=10)
        stateEntry.grid(row=9, column=2, sticky=W)

        #####################
        #### Country Entry
        Label(popup, text="Country: ").grid(row=10, column=1, sticky=W)
        countryBox = Combobox(popup,
                              width=10,
                              name="combobox_country",
                              state="readonly",
                              values=["USA", "Canada"])
        countryBox.grid(row=10, column=2, sticky=W)

        #Separator(popup, orient=HORIZONTAL).grid(row=12, column=1, sticky="ew")







        # Submit
        Button(popup,
               text="Add Card",
               name="button_confirm",
               command=lambda: self._add_card_to_tree(
                                                      nameEntry.get(),
                                                      nameEntry.get(),
                                                      popup
                                                      )
               ).grid(row=11, column=1)
        Button(popup, text="Cancel", command=popup.destroy).grid(row=11, column=2)

    def _confirm_delete(self, itemID):
        # init popup
        popup = Toplevel()
        popup.title("Confirm Delete")

        # contents of popup: show the card detail being deleted
        Label(popup, text="Are you sure you want to delete:\n").grid(row=1, column=1, columnspan=2)
        values = self.tree.item(itemID)["values"]
        dataStr = ""
        for value in values:
            dataStr += value+"\n"
        Label(popup, text=dataStr).grid(row=2, column=1, columnspan=2, sticky=W)


        # confirm or cancel
        Button(popup, text="Delete", command=lambda: self._delete_card(itemID, popup)).grid(row=3, column=1)
        Button(popup, text="Cancel", command=popup.destroy).grid(row=3, column=2)



    def delete_card(self):
        print(self.tree.focus())
        itemToDelete = self.tree.focus()
        if itemToDelete != "":
            if self.PROMPT_DELETE:
                self._confirm_delete(itemToDelete)
            else:
                self.tree.delete(itemToDelete)



    def _get_next_card_num(self):
        if len(self.tree.get_children()) == 0:
            return 1
        else:
            return int(self.tree.get_children()[-1].lstrip("I"))+1

    def _delete_card(self, itemID, popup=None):
        self.tree.delete(itemID)
        if popup:
            popup.destroy()
