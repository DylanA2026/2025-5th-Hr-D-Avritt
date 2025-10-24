#Name: Dylan Avritt
#Class: 5th Hour
#Assignment: HW11

#1. Go to the link below and convert the code into pseudocode in comments, then code the flowchart completely:
#https://adacomputerscience.org/images/content/computer_science/design_and_development/program_design/figures/ada_cs_design_flow_ifelseif.svg

#import random library

#Make temperature variable, give it a value (random from 1 to 30)

#Make if statement that checks if temp is more than 20
#   - If more, print it's hot
#   - If less, go to next if statement

#Make if statement that checks if temp is more than 10
#   - If more, print it's mild
#   - If less, print it's cold

#Print thank you, and end the code


#Code goes here:
import random



temp = random.randint(1,30)

if temp > 20 :
    print("Its Hot")
if temp > 10 and temp < 20 :
    print("Its Mild")
if temp < 10 :
    print("Its Cold")

print("Thank You")