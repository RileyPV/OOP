import CarClass as c

def main():

    my_car = c.Car(1969, "Chevrolet")

    for count in range (5):
        my_car.accelerate()
        print("The current speed of the car is:",my_car.get_speed(),"MPH")
    
    for count in range (5):
        my_car.brake()
        print("The current speed of the car is:",my_car.get_speed(),"MPH")

main()