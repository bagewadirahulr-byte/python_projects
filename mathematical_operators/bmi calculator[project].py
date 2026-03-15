# CREATE A CALCULATOR TO TEST SOMEONE'S BMI USING MATHEMATICAL OPERATORS IN PYTHON
# we know the formula ;
height = input("Enter Height : ")
weight = input("Enter Weight : ")
print("\n")
print("height = " + str(height))
print("weight = " + str(weight))
height = int(height)
weight = int(weight)
print("bmi = weight / (height ** 2)")
bmi = weight / (height ** 2)
print("bmi = " + str(bmi))