items_list=[]

while True:
    choice= int(input("1:add itrm \n2:remove items \n3:List all products \n4:Total cost \npress any key to exit "))
    if choice  == 1:
        name =input("enter the item name:")
        price = float(input("enter the price:"))
        quantity =int(input("enter the quantity:"))
        items ={
            'name': name,
            'price': price,
            'quantity': quantity}
        items_list.append(items)
        print("items addes to cart sucessfully")
    elif choice == 2:
        choice_name = input("enter the items on remove:")
        is_product_found= False
        for i in items_list:
            if choice_name ==items:
                items_list.remove(i)
                is_product_found=True
            if is_product_found:
                print("items remove sucessfully")
            else:
                print("items not found in the cart")
    elif choice ==3:
        for i in items_list:
            print(f"name: {1['name']},price:{i['price']},quantity:{i['quantity']},totals:{i['price']*['quantity']}")
    elif choice ==4:
        total_amount=0
        for i in items_list:
            total_price=i['price']*i['quantity']
            total_amount =total_price + total_amount
            price(f"total amount:{total_amount}")
    else:
        print("thank you for shopping with us")
        break
                    