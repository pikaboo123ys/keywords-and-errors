try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Age cannot be negative.")
        raise ValueError
    else:
        if age % 2 == 0:
            print("The age entered is even.")
        else:
            print("The age entered is odd.")

except ValueError:
    print("Invalid input! Please enter a valid number for age.")
