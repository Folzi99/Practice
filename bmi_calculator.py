name = input("Name: ")

height_m = input("Height: ")
h_1_m = float(height_m)

weight_kg = input("Weight: ")
w_1_kg = float(weight_kg)

bmi = (w_1_kg / (h_1_m ** 2))
print("BMI: ")

print(bmi)
if bmi > 18.5 and bmi < 25:
    print(name, "is normal weight")
else:
    if bmi > 25:
        print(name, "is overweight")
    else:
        print(name, " is underweight")
