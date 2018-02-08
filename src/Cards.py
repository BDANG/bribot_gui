from pathlib import Path
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

class Cards:
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

        # First Name Entry
        Label(popup, text="First Name:").grid(row=1, column=1, sticky=W)
        fnameEntry = Entry(popup, width=10)
        fnameEntry.grid(row=1, column=2, sticky=W)

        # Last Name Entry
        Label(popup, text="Last Name:").grid(row=2, column=1, sticky=W)
        lnameEntry = Entry(popup, width=10)
        lnameEntry.grid(row=2, column=2, sticky=W)

        # Submit
        Button(popup,
               text="Add Card",
               command=lambda: self._add_card_to_tree(
                                                      fnameEntry.get(),
                                                      lnameEntry.get(),
                                                      popup
                                                      )
               ).grid(row=3, column=1)
        Button(popup, text="Cancel", command=popup.destroy).grid(row=3, column=2)

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
