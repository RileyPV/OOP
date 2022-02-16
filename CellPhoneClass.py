from pyexpat import model


class CellPhone:

    def __init__(self, manufacturer, model, price):
        self.__manufact = manufacturer
        self.__model = model
        self.__retail_price = price

    def set_manufact(self,name_man):
        self.__manufact = name_man

    def set_model(self,model_num):
        self.__model = model_num

    def set_retail_price(self,retail_price):
        self.__retail_price = retail_price

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price
