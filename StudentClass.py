import datetime

from datetime import date

class Student:

    def __init__(self, id, name, dob, classification):
        self.__studentID = id
        self.__name = name
        self.__date_of_birth = dob
        self.__age = 0
        self.__classification = classification


    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_age(self):
        today = date.today()
        self.__age = today.year - self.__date_of_birth

    #def registration_time(self):
       # self.__registration_time = ["Seniors" : "11/1 thru 11/3",
       #                             "Juniors" : "11/4 thru 11/6",
       #                             "Sophomores" : "11/7 thru 11/9",
       #                             "Freshman" : "11/10 thru 11/12"]


    def get_age(self,year):
        self.__age = year-2022
        return self.__age

    def get_classification(self):
        return self.__classification
