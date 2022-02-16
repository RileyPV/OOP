import CellPhoneClass as cp

def main():
    my_cellphone = cp.CellPhone("Apple", 11, 900)

    print(my_cellphone.get_manufact(),my_cellphone.get_model(),my_cellphone.get_retail_price())

main()