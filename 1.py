def get_input(prompt):
    return input(prompt)
def calculate_grade(score):
    return "Pass" if score >= 60 else "Fail"
def display_result(name, grade):
    print(f"{name}: {grade}")


while True:
    name = get_input("Name: ")
    if name.lower() == "q":
        break

    score = float(get_input("Score: "))
    grade = calculate_grade(score)
    display_result(name, grade)

    # 询问是否结束
    again = input("Do you want to play again? (y/n): ")
    if again.lower() != "y":
        break

