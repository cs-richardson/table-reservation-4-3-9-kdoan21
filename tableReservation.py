#Code that checks if a user has a reservation that matches a string variable
#and tells them if they do or not

userName = input("Hello, what is your name? ")
reservationName = "Jake"
if userName == "Jake":
    print("Hello, your table is this way.")
else:
    print("Sorry, you don't have a reservation with us.")
