def calculate_bmi(feet, inches, weight):
    height_inches = (feet * 12) + inches
    bmi = (weight / (height_inches ** 2)) * 703  

    if bmi < 18.5:
        category = "Underweight"
    elif bmi <= 24.9:  
        category = "Normal weight"
    elif bmi <= 29.9:  
        category = "Overweight"
    else:
        category = "Obese"


    return round(bmi, 1), category
