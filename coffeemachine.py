money = 550
water = 400
milk = 540
coffee = 120
cups = 9


def buy():
    global money, water, milk, coffee, cups
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    choice = input()
    if choice == "1":
        if water >= 250 and coffee >= 16 and cups > 0:
            water = water - 250
            coffee = coffee - 16
            cups = cups - 1
            money = money + 4
            print("I have enough resources, making you a coffee!")
        else:
            is_posible(250, 0, 16)
    elif choice == "2":
        if water >= 350 and milk >= 75 and coffee >= 20 and cups > 0:
            water = water - 350
            coffee = coffee - 20
            milk = milk - 75
            cups = cups - 1
            money = money + 7
            print("I have enough resources, making you a coffee!")
        else:
            is_posible(350, 75, 20)

    elif choice == "3":
        if water >= 200 and milk >= 100 and coffee >= 12 and cups > 0:
            water = water - 200
            coffee = coffee - 12
            milk = milk - 100
            cups = cups - 1
            money = money + 6
            print("I have enough resources, making you a coffee!")
        else:
            is_posible(200, 100, 12)

    elif choice == "back":
        return


def is_posible(water_need, milk_need, coffe_need):
    global water, milk, coffee, cups
    if water < water_need:
        print("Sorry, not enough water!")
    elif coffee < coffe_need:
        print("Sorry, not enough coffee!")
    elif milk < milk_need:
        print("Sorry, not enough milk!")
    elif cups < 1:
        print("Sorry, not enough cups!")


def take():
    global money
    print("I gave you ${}".format(money))
    money = 0


def state():
    global water, milk, coffee, cups, money
    print("The coffee machine has:")
    print("{} of water".format(water))
    print("{} of milk".format(milk))
    print("{} of coffee beans".format(coffee))
    print("{} of disposable cups".format(cups))
    print("{} of money".format(money))


def fill():
    global water, milk, coffee, cups
    print("Write how many ml of water do you want to add:")
    water = water + int(input())
    print("Write how many ml of milk do you want to add:")
    milk = milk + int(input())
    print("Write how many grams of coffee beans do you want to add:")
    coffee = coffee + int(input())
    print("Write how many cups of coffee do you want to add:")
    cups = cups + int(input())


while True:
    print("Write action (buy, fill, take, remaining, exit):")
    choice = input()

    if choice == "buy":
        buy()
    elif choice == "fill":
        fill()
    elif choice == "take":
        take()
    elif choice == "remaining":
        state()
    elif choice == "exit":
        break
