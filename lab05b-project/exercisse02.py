def BMI_calculation(height, weight):
    BMI = weight_kg / (height_m ** 2)
    return BMI
weight_kg=float(input("weight:"))
height_m=float(input("height:"))

def BMI_category(BMI_value):
    if BMI_value < 18.5:
        return "Underweight"
    elif BMI_value < 25:
        return "Normal"
    elif BMI_value < 30:
        return "Overweight"
    elif BMI_value > 30:
        return "Obed"



print(f"BMI:{BMI_calculation(height_m,weight_kg):1f}")
print(f"BMI_category:{BMI_category(BMI_calculation)}")

