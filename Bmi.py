height=54 
weight=55
bmi=weight/(height*height)*703
print("BMI is",bmi)
if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<24.9:
    print("Normal weight")
elif bmi>=25 and bmi<29.9:
    print("Overweight")
else:
    print("Obesity")    
