def user_input():

    while True:
        try:
            print("     WELCOME TO THE BMI CALCULATOR! ")
            weight_kg = float(input("Enter your weight in kilograms: "))
            height_m = float(input("Enter your height in meters: "))
            if weight_kg > 0 and height_m > 0:
                return weight_kg, height_m
            else:
                print("Please enter valid positive values for weight and height.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

if __name__ == "__main__":
    
    weight, height = user_input()
    bmi_result = calculate_bmi(weight, height)
    bmi_category = classify_bmi(bmi_result)

    print(f"\nYour BMI is: {bmi_result}")
    print(f"Your BMI classification is: {bmi_category}")
