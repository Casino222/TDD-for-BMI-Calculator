from bmi_calculator import calculate_bmi

def main():
    print("BMI Calculator")
    feet = int(input("Enter height (feet): "))
    inches = int(input("Enter height (inches): "))
    weight = float(input("Enter weight (lbs): "))

    bmi, category = calculate_bmi(feet, inches, weight)
    print(f"BMI: {bmi}, Category: {category}")

if __name__ == "__main__":
    main()
