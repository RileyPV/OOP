import RetailItemClass as ri

def main():
    item1= ri.RetailItem("Jacket", 12, 59.95)
    item2= ri.RetailItem("Designer Jeans", 40, 34.95)
    item3= ri.RetailItem("Shirt", 20, 24.95)

    print(item1.get_item_description(), item1.get_units_in_inventory(), item1.get_price())
    print(item2.get_item_description(), item2.get_units_in_inventory(), item2.get_price())
    print(item3.get_item_description(), item3.get_units_in_inventory(), item3.get_price())



main()