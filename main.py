def calculate_BMI(weight,height):
     return weight / (height ** 2)

def get_category(BMI):
    if BMI < 18.5:
        return "UNDERWEIGHT"
    elif BMI < 25:
        return "NORMAL"
    elif BMI < 30:
        return "OVERWEIGHT"
    else:
        return "OBESITY"

def get_advice(category):
    if category == "UNDERWEIGHT":
        return "You should eat more healthy food."
    elif category == "NORMAL":
        return "You are healthy. Keep it up!"
    elif category == "OVERWEIGHT":
        return "Try to exercise regularly."
    else:
        return "It is better to consult a doctor."

#---Code to actually run the program---

w = float(input("Enter your weight (kg): "))
h = float(input("Enter your height (m): "))

bmi = calculate_BMI(w, h)
category = get_category(bmi)

print(f"\nBMI: {bmi: .2f}")
print(f"Health Category: {category}")
print(f"Advice: {get_advice(category)}")
print("\nStay healthy!")
print ("This project is for basic health awareness.")