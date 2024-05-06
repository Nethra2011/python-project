weight=float(input("Enter your weight"))
height=float(input("Enter your height"))
BMI=weight/(height*2)
if BMI <= 18.5:
    print("underweight")
elif (BMI > 18.5) and (BMI < 24.9):
    print("normal")
elif (BMI > 25) and (BMI < 29.9):
    print("obesity")
else:
    print("severe obesity")

