def calculate_bmi(feet, inches, weight):
    height_inches = (feet * 12) + inches
    bmi = (weight / (height_inches ** 2)) * 703  

    bmi = round(bmi, 1)  

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category
