import StudentClass as sc

import datetime


def main():
    my_student = sc.Student(892021116, "Riley Richards", "02/16/1996", "Sr")

    #print("The Student is:", my_student.get_age(),"years old.")

    if my_student.classification == "Sr":
        print("11/1 thru 11/3")
        
    if my_student.classification == "Jr":
        print("11/4 thru 11/6")
    
    if my_student.classification == "S":
        print("11/7 thru 11/9")
    
    if my_student.classification == "F":
        print("11/10 thru 11/12")

main()

