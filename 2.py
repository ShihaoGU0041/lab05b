while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0 or age > 120:
            print("Please enter a realistic age")
            continue
        break
    except ValueError:
        print("That's not a valid number. Please try again.")

print(f"You are {age} years old")