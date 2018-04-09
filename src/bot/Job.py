class Job:
    def __init__(self, jobID, cardTreeValues, addressTreeValues, driver=None):
        self.jobID = jobID
        #self.productlist = productlist
        #self.card = self.parse_parse_card_tree(cardTreeValues)
        #self.address = self.parse_parse_address_tree(addressTreeValues)
        self.driver = driver
