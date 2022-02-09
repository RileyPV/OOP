class CellPhone:

    def __init__(self,name_man,model_num,retail_price):
        self.__manufact = name_man
        self.__model = model_num
        self.__retail_price = retail_price

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
