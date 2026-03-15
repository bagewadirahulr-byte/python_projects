# Use if else and elif to upgrade the BMI calculator to give
weight = float(input("Please enter your weight: "))
height = float(input("Please enter your height: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    # instead of using elif bmi >= 18.5 and bmi < 25: we can use this and simple.
    print("normal weight")
else:
    print("overweight")