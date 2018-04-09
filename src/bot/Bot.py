from ..Product import Product
from .Job import Job
class Bot:
    def __init__(self):
        # mode such as Free, Personal, Pro, etc
        self.mode = None

        # a Settings object
        self.settings = None

        # a list of Job objects
        self.jobs = None

        # a dict of Product objects
        self.products = None


    def init(self, settingsObject, dropDetectStr, productSearchStr, autoCheckoutStr, productTree, cardTrees):
        self.settings = settingsObject
        if dropDetectStr == "yes":
            self.settings.DROP_DETECT = True
        else:
            self.settings.DROP_DETECT = False
        if productSearchStr == "yes":
            self.settings.PRODUCT_SEARCH = True
        else:
            self.settings.PRODUCT_SEARCH = False
        if autoCheckoutStr == "yes":
            self.settings.AUTO_CHECKOUT = True
        else:
            self.settings.AUTO_CHECKOUT = False

        self.products = self.parse_products_from_treeview(productTree)

        self.jobs = self.parse_jobs(self.products, cardTrees)

        print("INIT")
    def run(self):
        print("RUN")

    def parse_products_from_treeview(self, productTree):
        d = {}
        for productID in productTree.get_children():
            productItem = productTree.item(productID)
            print(productItem["values"])
            product = Product(tkTreeValueList=productItem["values"])
            if product.get_key() not in d.keys():
                d[product.get_key()] = [product]
            else:
                d[product.get_key()].append(product)
        return d


    def parse_jobs(self, products, cardTrees):
        addressTree = cardTrees.children["tree_address"]
        cardTree = cardTrees.children["tree_cards"]
        joblist = []
        for num, ID in enumerate(addressTree.get_children()):
            addressItem = addressTree.item(ID)
            cardItem = cardTree.item(ID)
            cardID = addressItem["values"][0]
            print(addressItem["values"], cardItem["values"])
            joblist.append(Job(cardID, addressItem["values"], cardItem["values"]))
