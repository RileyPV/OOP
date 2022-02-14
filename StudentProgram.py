import StudentClass as sc

def main():
    my_student=sc.Student

    date_of_birth=input("What is the student's date of birth?")
    print("The Student is:", my_student.get_age(),"years old.")

    classification = input("What is your classification?")
    if classification == "Senior":
        print("11/1 thru 11/3")
        
    if classification == "Junior":
        print("11/4 thru 11/6")
    
    if classification == "Sophomore":
        print("11/7 thru 11/9")
    
    if classification == "Freshman":
        print("11/10 thru 11/12")

main()

