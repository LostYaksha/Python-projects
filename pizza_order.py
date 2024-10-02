def pizza_order():
    pizza_list = []
    topping_list = []

    while True:
        pizza = input('What pizza would you like: ')
        toppings = input('What extra toppings do you want? ')

        pizza_list.append(pizza)
        topping_list.append(toppings)

        next_order = input('Do you want to order another pizza? (y/n) ')
        if next_order != 'y':
            break

    pizza_list_count = len(pizza_list)
    topping_list_count = len(topping_list)
    price = (pizza_list_count * 10) + (topping_list_count * 1)
    print('Your pizza orders are: ', pizza_list)
    print('Your extra toppings are: ', topping_list)
    print(f'Total price is £{price}.')


pizza_order()
