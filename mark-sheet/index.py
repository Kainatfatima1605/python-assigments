name = input ("enter your name  :")
percentage  = int(input("enter your percentage  :"))
if percentage >= 90:
    print("Garde = 'A+'")
if percentage >= 80:
    print("Garde =' Aone'")
if percentage >= 70:
    print("Garde = 'A'")  
if percentage >= 60:
    print("Garde = 'B'") 
if percentage >= 50:
    print("Garde = 'c'") 
if percentage >= 40:
    print("Garde = 'D'") 
else:
    print("fail")
    
    num = int(input("enter a number to print its table:  "))
for i in range (1,11):
    print(f" {num} x {i} = {num*i}")