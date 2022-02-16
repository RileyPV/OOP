class Car:

    def __init__(self,year,make):
        self.__year_model = year
        self.__make = make
        self.__speed = 0

    def accelerate(self):
    #add 5 to the speed data each time it is called
        self.__speed += 5
    
    def brake(self):
    #subtract 5 from the speed data each time it is called
        self.__speed -= 5
    
    def get_speed(self):
        return self.__speed