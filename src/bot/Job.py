class Job:
    def __init__(self, jobID, addressTreeValues, cardTreeValues, driver=None):
        self.jobID = jobID
        #self.productlist = productlist
        self.address = self.parse_address_tree(addressTreeValues)
        self.card = self.parse_card_tree(cardTreeValues)
        self.driver = driver

    def parse_address_tree(self, treeValues):
        '''
        Convert a list of tk tree values into a dictionary with proper keys.
        WIP: input validation?
        '''
        # ["cardID", "name", "email", "phone", "address1", "apt", "address2", "zip", "city", "state", "country"]
        return {"name": treeValues[1],
                "email": treeValues[2],
                "phone": treeValues[3],
                "address1": treeValues[4],
                "apt": treeValues[5],
                "address2": treeValues[6],
                "zip": treeValues[7],
                "city": treeValues[8],
                "state": treeValues[9],
                "country": treeValues[10]}

    def parse_card_tree(self, treeValues):
        # ["cardID", "number", "month", "year", "cvv"]
        return {"number": treeValues[0],
                "month": treeValues[1],
                "year": treeValues[2],
                "cvv": treeValues[3]}
