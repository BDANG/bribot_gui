from pathlib import Path
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

class Cards:
    def __init__(self, tree):
        self.tree = tree



    def _add_card_to_tree(self, fname, lname, popup=None):

        self.tree.insert("", "end", text=self._get_next_card_num(), values=(fname, lname, "a", "ph"))

        if popup:
            popup.destroy()

    def addCard(self):
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

    def _get_next_card_num(self):
        # WIP: DANGEROUS: what if you delete a card? and get a duplicate ID??
        return len(self.tree.get_children())+1
