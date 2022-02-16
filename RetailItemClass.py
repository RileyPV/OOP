class RetailItem:

    def __init__(self, desc, units, price):
        self.__item_description = desc
        self.__units_in_inventory = units
        self.__price = price
        
    def set_item_description(self, desc):
        self.__item_description = desc

    def set_units_in_inventory(self, units):
        self.__units_in_inventory = units
    
    def set_price(self, price):
        self.__price = price

    def get_item_description(self):
        return self.__item_description

    def get_units_in_inventory(self):
        return self.__units_in_inventory
    def get_price(self):
        return self.__price