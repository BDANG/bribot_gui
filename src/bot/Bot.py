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

        # set some of the settings flags
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

        # maintain a dictionary of products
        # because two products might vary in size but their HTML/links are the same
        # thus there is no need to load HTML for two products with different sizing
        self.products = self.parse_products_from_treeview(productTree)

        # maintain a list of Job objects which store the checkout info + products
        self.jobs = self.parse_jobs(self.products, cardTrees, self.products)

        self.test()
    def run(self):
        print("RUN")
        # init browser(s)

        # assign browser(s)

        # MP categories

        # MP links, htmls

        # MP carts

        # MP checkouts

    def parse_products_from_treeview(self, productTree):
        '''
        Method parses tkTreeview of the products into a dictionary of Product objects
        '''
        d = {}
        # iterate the product IDs in the tree
        for productID in productTree.get_children():
            productItem = productTree.item(productID)

            # init Product object
            product = Product(tkTreeValueList=productItem["values"])


            # assign products of the same key to the same value-list
            if product.get_key() not in d.keys():
                d[product.get_key()] = [product]
            else:
                d[product.get_key()].append(product)
        return d


    def parse_jobs(self, products, cardTrees, productDict):
        '''
        Method parses tkTreeview of the checkout info and combines them with Product objects
        to create a list of Job objects
        '''
        # address and card data stored in separate tkTreeviews
        addressTree = cardTrees.children["tree_address"]
        cardTree = cardTrees.children["tree_cards"]
        joblist = []
        for num, ID in enumerate(addressTree.get_children()):
            addressItem = addressTree.item(ID)
            cardItem = cardTree.item(ID)
            cardID = addressItem["values"][0]

            # init job object
            job = Job(cardID, addressItem["values"], cardItem["values"])

            # quadratically search for products that correspond to a Job
            for productkey in productDict:
                for product in productDict[productkey]:
                    if product.cardID == cardID:
                        job.productList.append(product)
            joblist.append(job)
        return joblist

    def test(self):
        '''
        Haphazard test function to check that references between product dict and jobs are maintained
        '''
        print(self.jobs[0].productList[0].get_key())
        print(self.jobs[0].productList[0])
        self.products[self.jobs[0].productList[0].get_key()][0].link = "newlink"
        for p in self.products[self.jobs[0].productList[0].get_key()]:
            print(p)
