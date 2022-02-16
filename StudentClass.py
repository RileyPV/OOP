import datetime

class Student:

    def __init__(self, id, name, dob, classification):
        self.__studentID = id
        self.__name = name
        self.__date_of_birth = dob
        self.__classification = classification
        
    def age(self):
        self.__age = 0

    #def registration_time(self):
       # self.__registration_time = ["Seniors" : "11/1 thru 11/3",
       #                             "Juniors" : "11/4 thru 11/6",
       #                             "Sophomores" : "11/7 thru 11/9",
       #                             "Freshman" : "11/10 thru 11/12"]


    def get_age(self):
        return self.__age

    def get_classification(self):
        return self.__classification
