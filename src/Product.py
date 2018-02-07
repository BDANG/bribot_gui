class Product:
    '''
    The class represents product/supreme item objects
    Currently maintain the necessary data to represent products (keywords, size, color, type, etc)
    additional methods are currently for data-formatting purposes
    '''
    def __init__(self, tkTreeValueList=None, dictrow=None):
        '''
        Two ways to construct a product:
        1. via ttk.TreeView.item value list
        2. via a dict from csv reading
        '''
        if tkTreeValueList:
            # a string with tildas in between keywords, (tilda-delimited)
            # primarily for file output
            self.keywordTildas = self.tilda_keywords(tkTreeValueList[0])

            # a non-flexible string that represents shop type
            # i.e. "jackets", "top_sweaters", "accessories"
            self.type = tkTreeValueList[1]

            # a non-flexible string that represents product size
            self.size = tkTreeValueList[2]

            # a string with tildas between colors (tilda-delimited)
            # primarily for file output
            self.colorTildas = self.tilda_keywords(tkTreeValueList[3])

            # a list of strings (keywords)
            self.keywordList = self.parse_keywords_to_list(tkTreeValueList[0])

            # a list of strings (colors)
            self.colorList = self.parse_keywords_to_list(tkTreeValueList[3])
        if dictrow: # see above for variable description
            self.keywordTildas = dictrow["keywords"]
            self.type = dictrow["shoptype"]
            self.size = dictrow["size"]
            self.colorTildas = dictrow["colors"]

            self.keywordList = dictrow["keywords"].split("~")
            self.colorList = dictrow["colors"].split("~")

    def tilda_keywords(self, keywordsCommaStr):
        '''
        Converts keyword comma string ("Hanes, Boxers")
        into tilda-delimtied ("Hanes~Boxers")
        '''
        splits = keywordsCommaStr.split(",")
        returnStr = ""
        for keyword in splits:
            returnStr+=keyword.strip()+"~"
        return returnStr[:-1]


    def parse_keywords_to_list(self, keywordsCommaStr):
        '''
        converts keyword comma string ("Hanes, Boxers")
        into a list of strings (["Hanes", "Boxers"])
        '''
        splits = keywordsCommaStr.split(",")
        newList = []
        for keyword in splits:
            newList.append(keyword.strip())
        return newList

    def to_tree_tuple(self):
        '''
        Converts a Product instance into a tuple of strings
        primarily for inserting into tk.Treeview
        '''
        keywordCommaStr = ""
        for keyword in self.keywordList:
            keywordCommaStr += keyword+", "
        keywordCommaStr = keywordCommaStr[:-2]

        colorCommaStr = ""
        for color in self.colorList:
            colorCommaStr += color+", "
        colorCommaStr = colorCommaStr[:-2]

        return (keywordCommaStr, self.type, self.size, colorCommaStr)
