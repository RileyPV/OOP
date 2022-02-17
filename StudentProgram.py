import StudentClass as sc

import datetime


def main():
    my_student = sc.Student(892021116, "Riley Richards", 10/12/1996, "Sr")
    today = (datetime.date.today().year)
    #print(today)
    #year = my_student.get_date_of_birth()
   # print(year)
    #dob = int(dob.split('/')[2])
    age = today - 1996
    print (age)
    
    #print("The Student is:", my_student.get_age(),"years old.")

    if my_student.get_classification() == "Sr":
        print("11/1 thru 11/3")
        
    if my_student.get_classification() == "Jr":
        print("11/4 thru 11/6")
    
    if my_student.get_classification() == "S":
        print("11/7 thru 11/9")
    
    if my_student.get_classification() == "F":
        print("11/10 thru 11/12")

main()

