from pathlib import Path
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.ttk import *
import csv
from src.Product import Product

class ProductHandler:
    def __init__(self, tree):
        self.tree = tree
        self.PROMPT_DELETE = True

    def _add_product_to_tree(self, keywords, shoptype, size, colorKeywords, popup=None):
        '''
        Private method for adding products to the tree
        keywords and colorKeywords are comma-separated strings
        shoptype, size are "determined" strings (not very flexible)
        '''
        # add to the tree, and close the popup
        self.tree.insert("", "end", values=(keywords, shoptype, size, colorKeywords))
        if popup:
            popup.destroy()


    def add_product(self):
        '''
        Public method that handles the UI for adding a product (via popup/Toplevel)
        '''
        # create pop up for entering details
        # wip: background color?
        popup = Toplevel()
        popup.title("Add a Product")

        # wip: specify case-sensitive?
        # Keyword Entry
        Label(popup, text="Keywords (comma-separated):").grid(row=1, column=1, sticky=W)
        keywordEntry = Entry(popup, width=30)
        keywordEntry.grid(row=1, column=2, sticky=W)

        # Shop type dropdown
        Label(popup, text="Type:").grid(row=2, column=1, sticky=W)
        typeBox = Combobox(popup,
                           width=10,
                           state="readonly",
                           values=["jackets", "tops-sweaters", "sweatshirts", "t-shirts", "accessories", "shoes", "hats", "bags", "skate"])
        typeBox.grid(row=2, column=2, sticky=W)
        typeBox.set("jackets")

        # size dropdown
        Label(popup, text="Size:").grid(row=3, column=1, sticky=W)
        #self.populate_size_dropdown(popup, typeBox.get())

        # color keywords
        Label(popup, text="Color(s) (comma-separated):").grid(row=4, column=1, sticky=W)
        colorEntry = Entry(popup, width=30)
        colorEntry.grid(row=4, column=2, sticky=W)


        # Submit / add product to the tree via private method
        Button(popup,
               text="Add Card",
               command=lambda: self._add_product_to_tree(
                                                      keywordEntry.get(),
                                                      typeBox.get(),
                                                      "SIZE_FUNC",
                                                      colorEntry.get(),
                                                      popup
                                                      )
               ).grid(row=5, column=1)

        # or cancel the new product
        Button(popup, text="Cancel", command=popup.destroy).grid(row=5, column=2)

    def edit_product(self):
        itemToEdit = self.tree.focus()
        if itemToEdit != "":
            _edit_product(itemToEdit)



    def _confirm_delete(self, itemID):
        '''
        Private method for initializing a popup to confirm deletion
        '''
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


        # confirm deletion (call private method) or cancel
        Button(popup, text="Delete", command=lambda: self._delete_product(itemID, popup)).grid(row=3, column=1)
        Button(popup, text="Cancel", command=popup.destroy).grid(row=3, column=2)



    def delete_product(self):
        '''
        Public method for handling deletion of a selected product
        '''
        # determine which item was selected
        itemToDelete = self.tree.focus()

        # ensure a selected item actually exists
        if itemToDelete != "":
            if self.PROMPT_DELETE: # if true, create popup to confirm delete
                self._confirm_delete(itemToDelete)
            else: # possibly useful for future unit tests
                self.tree.delete(itemToDelete)

    def save_products(self):
        '''
        Public method for handling saving the products to csv
        '''
        # wip file extension
        filepath = filedialog.asksaveasfilename()

        # when filepath is empty, the filedialog was cancelled...do nothing by returning
        if filepath == "":
            return

        with open(filepath, "w") as f:
            fields = ["keywords", "shoptype", "size", "colors"]
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()

            # write each product as a row in csv
            for itemID in self.tree.get_children():
                item = self.tree.item(itemID)

                # handle the tree values via an object
                product = Product(tkTreeValueList=item["values"])
                writer.writerow({
                                "keywords": product.keywordTildas,
                                "shoptype": product.type,
                                "size": product.size,
                                "colors": product.colorTildas
                })

    def load_products(self):
        '''
        Public method for handling loading products saved in a csv
        '''
        filepath = filedialog.askopenfilename()

        # if the filedialog was cancelled, just return
        if filepath == "":
            return
        with open(filepath, "r") as f:
            reader = csv.DictReader(f)
            # for each row in the csv, add them to the tree
            for row in reader:
                self.tree.insert('', 'end',
                    values=Product(dictrow=row).to_tree_tuple()
                )




    def _get_next_card_num(self):
        # WIP: DANGEROUS: what if you delete a card? and get a duplicate ID??
        return len(self.tree.get_children())+1

    def _edit_product(self, itemID):
        None

    def _delete_product(self, itemID, popup=None):
        '''
        Private method for specifically deleting an item from the tree
        closes the popup when done
        '''
        self.tree.delete(itemID)
        if popup:
            popup.destroy()