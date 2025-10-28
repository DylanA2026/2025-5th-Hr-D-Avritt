#Name: Dylan Avritt
#Class: 5th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be given a number as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

#Code Here:

print("hello world!")

height = int(input("How tall are you? (In Inches)"))
weight = int(input("How much do you weigh? (In Pounds)"))

print("Your height is ", height, "inches and Your weight is ", weight, "pounds")
Correct_Info = input("Is this info correct? (Y/N)")
if Correct_Info == "N":
    print("Please change your info and try again.!")
    exit()
else :
    print("Thank you!")

bmi_Number = weight / (height**2) * 703
print("Your BMI is", bmi_Number)

if bmi_Number >= 29.9 :
    print("You are Obese")
elif bmi_Number >= 25 and bmi_Number <= 30 :
    print("You are Overweight")
elif 18.5 <= bmi_Number < 25 :
    print("You are Normal Weight")
else:
    print("You are Underweight")