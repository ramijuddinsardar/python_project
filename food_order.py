# This is a simple food order program. It will take the order from the user and calculate the total bill.

menu = {
    "pizza" : 40,
    "pasta" : 50,
    "burger" : 60,
    "salad" : 70,
    "coffee" : 80,
}

print("Welcome to our resturent.")
print("Our food menu:-\npizza : 40\npasta : 50\nburger : 60\nsalad : 70\ncoffee : 80")

item = ()
bill = 0

while True:
    item = input("Please type what you want to order or press 'q' to quite : ")
    if item in menu:
        bill += menu[item]
        print(f"Your {item} has been added succesfully")
        print(f"your current bill is {bill}")
    elif item == "q":
        print(f"Thank you for puchasing.\nyour total bil is {bill} ")
        break
    else:
        print(f"Your {item} is not avalable.")